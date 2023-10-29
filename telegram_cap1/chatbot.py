import threading
import json
import pandas as pd
import tensorflow as tf
import torch
import schedule
import time
import datetime

from BotServer import BotServer
from Preprocess2 import Preprocess2
from FindAnswer import FindAnswer
from IntentModel import IntentModel
from create_embedding_data import CreateEmbeddingData
from logging import handlers
import logging

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
        tf.config.experimental.set_virtual_device_configuration(gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=4096)])
    
    except RuntimeError as e:
        print(e)


LogFormatter = logging.Formatter('%(asctime)s,%(message)s')

LogHandler = handlers.TimedRotatingFileHandler(filename='C:/capstone/chatlog/chatbot.log', when ='midnight',
interval=1, encoding='utf-8')
LogHandler.setFormatter(LogFormatter)
LogHandler.suffix = "%Y%m%d"

Logger = logging.getLogger()
Logger.setLevel(logging.ERROR)
Logger.addHandler(LogHandler)

n=0

#전처리 객체 생성
p = Preprocess2(word2index_dic='C:/capstone/chatbot2_dic.bin',  userdic='C:/capstone/user_dic.tsv')
print("텍스트 전처리가 로드 완료")

intent = IntentModel(model_name='C:/capstone/intent_model.h5', preprocess=p)
print("의도 파악 모델 로드 완료")

df = pd.read_excel('C:/capstone/질문 답변 데이터 '+str(n+10)+'주차.xlsx')
print("엑셀 파일 로드 완료")

create_embedding_data = CreateEmbeddingData(df=df, preprocess=p)
create_embedding_data.create_pt_file()
embedding_data = torch.load('C:/capstone/embedding_data.pt')
print("임베딩 pt 파일 갱신 및 로드 완료")


def to_client(conn, addr):
    try:
        # 데이터 수신
        read = conn.recv(2048) # 수신 데이터가 있을 때까지 블로킹
        print('======================')
        print('Connection from: %s' % str(addr))

        if read is None or not read:
            # 클라이언트 연결이 끊어지거나 오류가 있는 경우
            print('클라이언트 연결 끊어짐')
            exit(0)  # 스레드 강제 종료

        # json 데이터로 변환
        global query
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']
        print(query)

        # 의도 파악
        intent_pred = intent.predict_class(query)
        intent_name = intent.labels[intent_pred]

        # 답변 검색
        f = FindAnswer(df=df, embedding_data=embedding_data ,preprocess=p)
        selected_qes, score, answer, imageUrl, query_intent = f.search(query, intent_name)

        if score < 0.5:
            answer = "부정확한 질문이거나 답변할 수 없습니다."
            imageUrl = "없음"
            # 사용자 질문, 예측 의도, 선택된 질문, 선택된 질문 의도, 유사도 점수
            Logger.error(f"{query},{intent_name},{selected_qes},{query_intent},{score}")

        send_json_data_str = {
            "Query": selected_qes,
            "Answer": answer,
            "imageUrl": imageUrl,
            "Intent": intent_name
        }
        message = json.dumps(send_json_data_str) # json객체 문자열로 반환
        conn.send(message.encode()) # 응답 전송

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    port = 5050
    listen = 1000
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start...")
    query = None

    while True:
        schedule.run_pending()
        time.sleep(1)
        conn, addr = bot.ready_for_client()
        client = threading.Thread(target=to_client, args=(
            conn,
            addr,
        ))
        client.start()
      
        now = datetime.datetime.now()
        if now.weekday() == 2 and query =="질문 답변 데이터 업로드":
            intent = IntentModel(model_name='C:/capstone/intent_model.h5', preprocess=p)
            print("의도 파악 모델 로드 완료")
            n += 1
            df = pd.read_excel('C:/capstone/질문 답변 데이터 '+str(n+10)+'주차.xlsx')
            print("엑셀 파일 로드 완료")
            create_embedding_data = CreateEmbeddingData(df=df, preprocess=p)
            create_embedding_data.create_pt_file()
            embedding_data = torch.load('C:/capstone/embedding_data.pt')
            print("임베딩 pt 파일 갱신 및 로드 완료")

import threading
import json
import schedule
import time
from BotServer import BotServer
from create_cnn import createcnn


def to_client(conn, addr):
    global query  # Define query globally
    try:
        # 데이터 수신
        read = conn.recv(1024) # 수신 데이터가 있을 때까지 블로킹
        print('======================')
        print('Connection from: %s' % str(addr))

        if read is None or not read:
            # 클라이언트 연결이 끊어지거나 오류가 있는 경우
            print('클라이언트 연결 끊어짐')
            exit(0)  # 스레드 강제 종료

        # json 데이터로 변환
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']
        print(query)
        message = "ai 학습 완료했습니다."
        conn.send(message.encode())

        if query == '/intentlearning':
            createcnn()
            print("Model training is completed.")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    port = 6060
    listen = 1000
    bot = BotServer(port, listen)
    bot.create_sock()
    print("Learning bot start...")
    query = '/intentlearning'

    while True:
        schedule.run_pending()
        time.sleep(1)
        conn, addr = bot.ready_for_client()
        client = threading.Thread(target=to_client, args=(
            conn,
            addr,
        ))
        client.start()
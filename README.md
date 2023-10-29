# 한밭대학교 컴퓨터공학과 EduBot팀

**팀 구성**
- 20181624 신희관 
- 20187098 이지형
- 20207131 조윤선

## <u>Teamate</u> Project Background
- ### 필요성
  - 학습에 어려움이 있는 학생들에게 개인별 맞춤형 학습 서비스를 제공함으로써 학습능력 향상
  - 학생이 원하면 언제든 시공간의 제약을 받지 않고 부족한 부분을 도움 받을 수 있도록 챗봇을 개발하여 학습 적응 지원
- ### 기존 해결책의 문제점
  - 기존의 프로그래밍 언어 관련 수업에서는 학생 개개인의 역량과 이해도 차이로 인해 편차가 크게 발생하는 문제가 존재
  - 학생들을 지도할 때 1:1로 살피고 개별 피드백을 해주는 것이 중요하지만 현실적으로 어려움 이러한 문제를 해결하기위해 챗봇 개발을 목표로함
  
## System Design
  - ### System Requirements
    - 사용자가 챗봇에 파이썬 이론에 관한 질문을 하면 답변된 Q&A 데이터에서 적절한 답변을 추출 후 답변 
    - 모바일, 웹 환경 모두 챗봇 환경 지원
    - 파이썬 코딩 실습 환경 제공을 위한 온라인 저지 구축

  - ### System Architecture
  ![image01](https://github.com/HBNU-SWUNIV/come-capstone23-edubot/assets/52690408/628faea1-c0f2-4cf9-a609-44d634dfeb75)   
  
## 💻 Tech Stack
<h4> Platforms & Languages </h4>

<div align="left">
	<img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white"> 
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
    <img src="https://img.shields.io/badge/mariaDB-003545?style=for-the-badge&logo=mariaDB&logoColor=white">
    <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white">
    <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white">
	
</div>

<h4> Tools </h4>
<div align=left>
	<img src="https://img.shields.io/badge/Intellij%20IDE-000000?style=flat&logo=intellijidea&logoColor=white" />
	<img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white"/>
    <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
</div>
  
## Conclusion
  - 컴퓨터공학과 1학년 파이썬 수업에서 학생들에게 질문을 받아 답변해주며 5000개 이상의 Q&A 데이터를 확보하고 모델 학습에 사용함
  - 학생들은 시공간의 제약 없이 각자의 학습 속도와 이해 수준에 맞게 질문을 할 수 있게 되었고, 원하는 질문에 대한 답을 얻을 수 있게 되었음
  - 해당 챗봇 시스템은 프로그래밍 수업뿐만 아니라 다양한 학습 환경에서 유용하게 활용될 수 있음
  - 모바일, 웹 환경 모두 사용이 가능하며 웹에서는 간단한 온라인저지를 통해 간단한 코딩 실습 공간으로 이용 가능
  
## Project Outcome
- ### 2023년 한국전기전자학회 학술대회
<img width="638" alt="스크린샷 2023-10-26 오후 4 31 51" src="https://github.com/HBNU-SWUNIV/come-capstone23-edubot/assets/124351914/67837f59-04ab-4a13-b096-5e854e31b133">

- ### App, Web
![mobile](https://github.com/HBNU-SWUNIV/come-capstone23-edubot/assets/124351914/fa8bae85-7c38-4b3c-97be-2ca8d8019da3)
<img width="1107" alt="KakaoTalk_Photo_2023-10-25-16-42-20" src="https://github.com/HBNU-SWUNIV/come-capstone23-edubot/assets/124351914/eb7e4784-8b12-4389-bff1-894d8fcf6869">
<img width="1109" alt="KakaoTalk_Photo_2023-10-25-16-42-13" src="https://github.com/HBNU-SWUNIV/come-capstone23-edubot/assets/124351914/0d2b8b07-4c57-404e-9f89-caa50bd59ddf">



## 패치노트

### 3/19
AI 백엔드 자동화 학습

1. 학생들이 질문한 내용이 google spread sheet로 들어간다.
2. 학생들의 질문 내용을 사람이 가공하여 googlespreadsheet [AI 학습용 가공 데이터] 에 작성해서 놓는다.
3. 1번 ROW = 문제유형, 2번 QUERY = 질문 내용, 3번 ANSWER = 가공한 사람이 작성한 정답
4. 구글 스프레드 시트에 입력된 내용(주차별 질문 누적, 입력된 answer) + 기존 AI HUB에서 합친 "통합본 데이터"로 매주 새로운 AI 모델을 만들어낸다.
--> 이방법 실패 cnn 학습이 잘 되지않음

작동방법
1. 텔레그램에서 내부 코드(" AI 자동화 학습 ")을 입력하면 FLASK API 서버를 통하여 백엔드 서버로 전달한다.
2. 백엔드 서버는 응답이 들어오면 새로운 모델을 생성만 해준다.

3. *기존의 질의응답데이터 업로드시에 같이 업로드된다.*

query에 answer을 달아주는행위 -> ai 질의응답 학습에는 그냥 추가 데이터임, chattest 문제 제출을 위한 답을 하는것

ai 학습에는 어짜피 excel로 만들어진 답변 데이터가 있고, ai 자체로 생각해서 답을 주는 형태가 아니기 때문에 answer은 학습시키는 용도로 사용된다.


그럼 학생질문 350개 우리 대답 350개 매주 700개 데이터 학습


### 4/3 - 학생 질문 리스트를 엑셀파일로 출력해주는 기능 추가
*main파일이 있는 pythonProject파일안에 n주차 데이터.xlsx 파일을 넣어주면됨.

작동 원리는 사용자가 학생 질문 리스트를 보려고 입력하면(/sqd)
for문이 1부터 14까지 작동하며 사용자가 입력한 숫자가 있으면 엑셀을 출력해준다.
파일이 없을 경우 except문이 실행되어 예외처리된다.

*추가된 내용 및 수정 내용

def studentquerydata(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id,
                             text="학생분들의 질문 리스트 목록보기 기능입니다.\n 질문 리스트를 참고해서 ai에 궁금한 내용을 물어봐주세요. \n\n다른기능을 사용하고 싶으시면 /help를 입력해주세요")
    global NUM
    NUM = 5
    context.bot.send_message(chat_id=chat_id, text="몇 주차 과제 리스트를 보여드릴까요? \n*숫자만 입력해주세요*")


    context.bot.send_message(chat_id=chat_id, text="안녕하세요, 한밭대학교 교육용 챗봇입니다.\n" \
                  "현재 다음 기능을 제공하고 있습니다.\n" \
                  "1.과제 제출(질문) - /soa \n2.수업 질의응답 - /aqa\n3.챗봇 문제풀기 - /chattest\n4.질문 리스트 보기 - /sqd\n" \
                  "\n 커맨드를 입력해주시거나 클릭해주세요.")


    elif NUM == 5:
        for i in range(1,15):
            if user_text == str(i):
                try:
                    context.bot.send_message(chat_id=chat_id, text=user_text+"주차 과제 데이터 입니다.")
                    excel_file = open(str(i)+'주차 데이터.xlsx', 'rb')
                    context.bot.send_document(chat_id=chat_id, document=excel_file)
                    excel_file.close()
                except FileNotFoundError:
                    context.bot.send_message(chat_id=chat_id, text="과제 리스트가 없거나, 아직 추가되지 않았습니다.")
                break


student_querydata = CommandHandler('sqd', studentquerydata)
dispatcher.add_handler(student_querydata)


### 4/4 실제 코드에 넣음
- 깃허브 등록할때 저장하고 등록해야 됨

### 4/6 학생들에게 시험문제를 제공할 때 그냥 답을 알려주는게 아닌 서로 상호작용 하는 형식의 알고리즘을 생각해봐야함. 

1. 학생들이 퀴즈 데이터를 물어본다.
2. 문제가 별로 안되기때문에 문제당 유형을 물어본다.
3. 예를들어 퀴즈 4번에 대해 알려줘 물어본다면, 어떤게 막히시나요? 이런 문구를 출력
4. 그 퀴즈에 대한 힌트( 버튼을 추가해서 하는 형식?)으로 원하는 내용을 물어본다.
5. 바로 답을 해주는 형식이 아닌, 상호작용하면서 하는 형식으로 힌트를 제공한다.
6. 답은 그래도 모르겠어요 라고 5번 이상 들어온다면 알려주는게 좋을듯

학생들에게 피드백을 받는 기능을 만들었다.
데이터베이스는 chatid랑 type으로 만들어서 데이터가 들어간다.

def reportdata(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id,
                             text="챗봇을 이용하시면서 불편하신 내용을 적어주세요\n 적어주신 피드백을 기반으로 챗봇을 유지보수 하려고 합니다. \n\n다른기능을 사용하고 싶으시면 /help를 입력해주세요")
    global NUM
    NUM = 6
    context.bot.send_message(chat_id=chat_id, text="피드백을 [] 안에 적어주세요")


    elif NUM == 6:
        idx = user_text.find(']')
        type = user_text[1:idx]
        sql = "INSERT INTO dataset(chatid ,type) VALUES (%s, %s)"
        cursor.execute(sql, (chat_id, type))
        context.bot.send_message(chat_id=chat_id, text="피드백 제출이 완료되었습니다. 감사합니다.")
        db.commit()
        db.close() 


report_data = CommandHandler('report', reportdata)
dispatcher.add_handler(report_data)

context.bot.send_message(chat_id=chat_id, text="안녕하세요, 한밭대학교 교육용 챗봇입니다.\n" \
                "현재 다음 기능을 제공하고 있습니다.\n" \
                "1.과제 제출(질문) - /soa \n2.수업 질의응답 - /aqa\n3.챗봇 문제풀기 - /chattest\n4.질문 리스트 보기 - /sqd\n5.챗봇 사용에 불편한점을 기록해주세요- /report\n" \
                "\n 커맨드를 입력해주시거나 클릭해주세요.")

### 4/17 중간고사 문제제출 챗봇 개발중(examserver)
    현재 구현된 기능으로는 /다음, /이전, /제출하기이다.
    /start를 눌러 시작하면 infomessage를 출력해주고, /다음을 입력하여 문제를 풀게 시작한다.

    /다음 키워드를 입력시 전역변수 testnumber가 +1 되면서 1번 문제가 출력되고 /다음을 누를때마다 testnumber = testnumber + 1 로 다음문제를 게속 출제한다. 답을 입력시 문제 숫자에 맞게 데이터베이스에 저장된다.
    /이전 키워드를 입력시 전역변수 testnumber가 -1 이전 문제가 출제된다. 그리고 입력한 값은 이전 문제의 데이터로 수정되어 들어간다.
    /제출하기를 입력하면 시험을 다시 수정할수없는 상태가 된다.

    현재 asyncio 기능을 제외한 나머지는 테스트까지 끝마친 상태이다.
    

### 4/24 변경점
    create_traindata : 기존 ai학습 데이터지움
    intentmodel : 123이 번호 과제 등으로 고정되어있었기 떄문에 바꿈
    FindAnswer : 이제 의도분류모델과 키워드 추출을 둘다 사용하게 바꿈
    Create_imbeding_data : 에서 pos = self.p.pos(str(sentence)) 로 str을 붙임 * 원인을 모르겠음 *

    현재 home 모델은 기존 aihub 데이터를 지우고 처리함
    
    기존 챗봇 사용자 질문데이터를 라벨링을 새로했음
        1. 문자열-
        2. 반복문-
        3. 변수-
        4. 연산자-
        5. 입력문-
        6. 조건문-
        7. 주석-
        8. 출력문-
        9. 파이썬-
        10. 파일-
        11. 내장모듈-
        12. 내장클래스-
        13. 내장함수-
        14. 가상환경-
        15. 시퀀스자료형-
        16. 기타-

    결론적으론 실패했지만, 원인을 찾고 고쳐나가야함

    *현재는 cnn과 키워드 추출모델을 사용한 미완성 모델입니다.*
    
    인터넷에서 cnn학습시킨 방향과 비교해서 고쳐나가야함

### 4/25 main에 user_num rand_cluser 추가
    각자 개인의 전역변수를 사용해서 문제를 풀고, 명령어가 각자 개인 전역변수로 들어가서 오류가 발생하지않게 수정함


### 5/2 중간고사 이후 챗봇

    1. create_dic으로 단어사전 새로 생성( 새로운 단어가 추가되었을 경우 사용 googlespreadsheet 데이터와 기존 aihub데이터로 사전생성) * 자주 안해도됨 *
    2. capstone_question_data 엑셀에 추가한 내용 다운받고 csv파일로 저장한후 googledrive에 넣기
    3. 의도분류모델학습데이터생성하기(자동화).ipynb 실행해서 새로 추가된 내용있으면 넣고 돌려서 train_data 뽑아오기
    4. train_data를 다운받고 create_cnn으로 의도분류모델 생성하기
    5. 만약 추가된 내용이 있다면(intent) IntentModel에 추가해야함( 추가안하면 랜덤으로 뽑아와서 섞이게 되는 문제가 있음 )
    => 이부분 좀더 자동화할 생각해보기
    6. create_traindata를 안쓰는 방식 수정해야함
    7. 현재 문재점은 create_cnn을 사용하면 train_data값이 바뀜 

### 5/3 추가한 내용 
    1. create_cnn을 실행시킨다.
        1. create_traindata가 먼져 실행되어 새로 추가된 학습데이터로 train_data.csv를 새로 생성한다. (통합본데이터.csv도 생성)
    2. create_cnn에서 생성된 train_data.csv와 user_dic, chatbat2_dic (사전들) 과 cnn(intent_model.h5)을 새로 생성한다.
    기존 문제점 1 학습시키고 create_data가 들어옴
    create_data를 먼져해서 train_data를 만들어야 됨

### 5/5 수정사항
	IntentModel - traindata생성용.xlsx에서 인텐트를 뽑아서 자동으로 생성해줌
	creat_traindata - 엑셀데이터에서 자동으로 라벨과 인텐트 텍스트를 출력해서 뽑음 
	= 코드 수정할 필요 없음


자동화 v2 사용법


화요일 12시 /googlesheetupload 커멘드 출력 -> 구글 스프레드시트에 데이터 등록됨

화요일 오후에 질문데이터를 기반으로 인텐트수정후 답변달기
	1. 답변단 데이터를 추가한 엑셀데이터 ( 질문 답변 데이터 n 주차.xlsx )
	2. 문제출제( 구글스프레드시트 -> database )
	3. 학생들에게 제공할 엑셀파일( n주차 데이터.xlsx )
	4. 챗봇 학습시키기위한 엑셀파일( traindata생성용.xlsx ) 1번과 같이 데이터만 추가	    하면됨

코드에서 수정해야할일 -> 없음
	

챗봇에서 
	/mariadbupload -> 문제를 database로 옮김
		
	/intentlearning 입력시 traindata를 생성하고 cnn을 새로 생성한다.

	/aqa -> 질문 답변 데이터 업로드 -> 질문 답변 데이터 n 주차 업로드
	*얘를 맨마지막에 해야 기존에 업데이트한 내용들이 등록됨*


### 5/21 변경점
        pyevsim을 사용하여 자동화 한 목록(기존 예약 키워드 사용X)
        1. 화요일 00:00에 데이터베이스에 저장된 학생들의 질문리스트가 Googlespreadsheet에 전송
        2. 수요일 00:00에 학생들의 질문데이터로 만든 문제들을 데이터베이스에 저장
        3. 수요일 00:10에 학생들이 질문한 내용을 가공해서 AI를 학습

        *추가예정
        4. 기존 /aqa에서 질의응답업로드 키워드를 입력해서 챗봇을 업데이트 시켰던 방법을 pyevsim을 활용하여 완전 자동화를 할 예정


### 5/22 변경점
    추가내용 : pyevsim을 활용한 완전 자동화

    기존의 챗봇 업데이트는 예약 메세지 기능 및 챗봇에서 메세지(키워드)를 보내서 직접 학습을 시켜야하는 단점이 있었음
    이 내용을 pyevsim을 사용해서 일정 시간이 되면 자동으로 파일이 업데이트가 되고, 업데이트 된 파일을 자동으로 업로드 하는 독자적인 서버를 만듬

    기존내용
    1. 화요일 00:00에 데이터베이스에 저장된 학생들의 질문리스트가 Googlespreadsheet에 전송 -> 과제 마감일인 화요일 새벽 12:00에 저번주 화요일 00:00부터 이번주 월요일 23:59:59까지 입력된 모든 데이터를 구글 스프레드 시트에 전송함
    2. 수요일 00:00에 학생들의 질문데이터로 만든 문제들을 데이터베이스에 저장 -> 일정 시간이되면 구글스프레드시트에 정리해놓은 문제들을 데이터베이스에 전송함
    3. 수요일 00:10에 학생들이 질문한 내용을 가공해서 AI를 학습 -> create_cnn.py를 일정시간에 실행시켜 cnn을 학습시킴
    추가내용
    4. 수요일 00:20에 챗봇 전체 자동 업데이트( 임베딩 및 엑셀파일, ai 모델 업로드 ) -> json을 사용해서 기존 챗봇에 보내던 메세지를 자동으로 보내게 생성함

-> chatbot.py 파일의 맨마지막 시간을 수정해야함

    필요한 것, 서버에 학습을 위한 파일 넣기 ( 1.학습용 질의응답 가공 데이터 2.학생들이 질문한 주차별 데이터 3.챗봇이 사용할 대답 파일)
    --> 이부분도 구글드라이브 폴더를 만들어서 원격으로 자동화 할 예정


### 5/29 변경점
    기존의 pyevsim을 사용하여 완전자동화를 하는 과정에서 데이터를 뽑는 과정에서 날짜 오류가 발생해서 이부분을 수정했습니다.

    추가예정 : pyevsim을 현재 1분당 한번실행하는데 이 방법은 너무 낭비를 심하게 하는 부분임 -> 4개로 나눠서 일주일에 시간에 맞게 한번씩 실행하는 방향으로 수정하기
            BKT를 적용하기 위해 학생데이터 수집후 넣어보려고함
	    
	    
### 6/2 변경점
    기존의 chattest에서 아무리 틀려도 답을 모르면 풀수없는 문제가 있었음
    원래 계획은 학생들의 질문리스트를 보여주고 챗봇에 물어보면서 개념을 익히고 그 개념으로 문제를 풀면서 개념을 다지는 방향성으로 생각헀지만 매주 약 300개씩의 데이터를 일일히 찾아보기엔 부담이 꽤 큰것 같다는 생각이 들었다.
    학생들의 피드백 의견에서 chattest시 정답을 알려줬으면 좋겠다는 의견이 있었음, 그래서 3번이상 틀리면 정답을 알려주게 개선했습니다.

    아직 서버에는 넣지않았습니다. main서버에 넣기전에 다른 보완점을 다 해결하고 한번에 넣을 생각입니다.


### 6/6 변경점
    기존의 1분마다 실행되던 pyevsim 자동업데이트 서버에서 4가지 자동업데이트를 4개의 서버로 분할하여 일주일에 한번만 실행하여
    자원을 낭비하지 않는 방식으로 변경하였다.

    추가예정 : BKT를 사용하여 학생들의 데이터를 기반으로 학습추적 및 학습예측을 통한 개인별 학습방법을 관리해주려고한다. 
            로그를 추적해서 학생들의 챗봇 사용 빈도를 나누고 챗봇 사용률에 따른 성적을 구분해볼 생각이다. -> 챗봇이 도움이 되었다는 의미 찾기


### 6/8 변경점
    학생들의 챗봇 사용빈도를 파악하기위해 usage.txt파일에 학생들이 chattest기능을 사용할때마다 chatid, timestamp 로그를 남기는 코드를 추가함
    학생들이 chattest 에서 3번 오답을 기록할시 정답을 제공해주는 기능 서버에 넣음
    
     추가예정 : BKT를 활용하여 학습 추적을 할때 1번의 1개의 스킬밖에 사용하지 못하여 BKT개선 버전인 DKVMN을 사용하여 적응형 학습추적을 하기로 결정하여 중간고사 문제로 학습데이터를 가공중

### 1학기 마무리
	1학기동안 모은 학생들의 질문데이터로 파이썬에 대한 챗봇을 완성했다.


### 2학기 
	1학기 동안 서버를 운영하면서 수집한 학습데이터로 챗봇모델을 완성하였지만, 교육부분중 이론부분밖에 담당하지 못하였고 텔레그램이라는 모바일 틀 안에서는 원하는 실습환경을 구축할 수 없을 것 같아
 	웹으로 온라인저지를 구축하기로 하였다.
  	구축 목표 웹에는 챗봇을 활용한 파이썬 이론교육 채팅방, 온라인저지 기능을 활용한 파이썬 실습환경 구축이다.
 

### 채팅방 
	1학기때 학생들 상대로 질문을 학습시켜 만든 파이썬 모델을 사용하여 질문과 답변을 하는 채팅방


### 온라인저지 기능
	1. 문제 추가
	   ADD 버튼을 눌러 문제이름 ( 띄어쓰기 X ), 문제 코드, 문제 설명 정보를 입력한다
	   저장받은 이름, 코드를 데이터베이스에 넣고( 서버가 껏다가 켜져도 문제가 유지되게 )
	   입력받은 코드, 설명 정보를 python파일, txt파일로 생성한다.
	
	2. 문제 풀기
	   Test버튼을 눌러 문제의 설명과 출력값을 보고, 문제에 맞는 코드를 작성해 submit 버튼을 클릭하여 출력값이 같으면 correct, 오답시 incorrect 출력
	   Test버튼을 누르면 문제이름, 정보, 출력값이 나타나는데, 정보와 출력값은 txt파일로 생성되어있기때문에 값을 불러들여서 넣음
	   코드를 넣고 제출 버튼을 누르면 사용자가 입력한 코드가 py로 변환되고 결과값을 저장된 결과값과 비교한다. 비교후 같으면 correct 출력


## 막힌점

	프론트에서 입력받은 데이터를 데이터베이스에 저장하는건 쉽게 했지만,
	예외처리의 문제인지, 데이터베이스에 들어가는 Description의 양이 길어지면 Test버튼이 활성화가 되지않는 문제가 발생함
	데이터베이스를 사용하지 않아도 output 출력에 영향을 줘서 문제가 발생했음
	
	해결 : 데이터베이스에 Transient를 사용하여 Description을 저장하지않고, 텍스트파일로 남겨서 저장시킴
	
	아마 문자열 길이 255를 넘었기 때문이다. 생각보다 길었음

 ## 추가 개선안

기존의 온라인 저지 서버는 flask api 서버를 사용했는데, 이 방식보단 fast api (비동기 처리) 방식의 서버로 변환하여 조금 더 개선했다.


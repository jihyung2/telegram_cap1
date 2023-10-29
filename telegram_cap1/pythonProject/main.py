import time
import telegram
import pymysql
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import requests
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import logging
from telegram import Update, error
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

BOT_token = "6178643347:AAG1aXMwymNwLinmW3xrzsfeBUeovbNxAj4"
BOT_NAME = '한밭대 과제제출 봇'
host = "127.0.0.1"
port = 5050

n=0

user_num = {}
rand_num = {}
rand_cluster = {}
ENTER_NAME = 0

#db = pymysql.connect()
#cursor = db.cursor(pymysql.cursors.DictCursor)
bot = telegram.Bot(BOT_token)

info_message = "안녕하세요, 한밭대학교 교육용 챗봇입니다.\n" \
               "현재 다음 기능을 제공하고 있습니다.\n" \
               "1.과제 제출(질문) - /soa \n2.수업 질의응답 - /aqa\n3.챗봇 문제풀기 - /chattest\n4.질문 리스트 보기 - /sqd\n" \
               "\n 커맨드를 입력해주시거나 클릭해주세요. \n"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

def studentquerydata(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    global user_num
    context.bot.send_message(chat_id=chat_id,
                             text="학생분들의 질문 리스트 목록보기 기능입니다.\n 가공된 질문 리스트를 참고해서 ai에 궁금한 내용을 물어봐주세요. \n\n다른기능을 사용하고 싶으시면 /help를 입력해주세요")
    context.bot.send_message(chat_id=chat_id, text="몇 주차 과제 리스트를 보여드릴까요? \n*숫자만 입력해주세요*")
    if chat_id not in user_num:
        user_num[chat_id] = 5
    else:
        user_num[chat_id] = 5



def error_handler(update: Update, context: CallbackContext) -> None:
    """Log the error and send a message to the user."""
    logger.warning(f'Update "{update}" caused error "{context.error}"')
    try:
        raise context.error
    except error.BadRequest:
        # handle BadRequest error
        pass
    except error.TimedOut:
        # handle network connection errors
        pass
    except error.Unauthorized:
        # handle unauthorized access errors
        pass
    except error.RetryAfter as e:
        # handle throttling errors
        logger.warning(f'Throttled by Telegram: {e.retry_after} seconds')
        time.sleep(e.retry_after)
    except error.TelegramError:
        # handle all other Telegram errors
        pass
    except Exception:
        # handle all other exceptions
        pass

def intentlearning(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id, text="ai 학습중 입니다.")

    datas = {
        "query": str(user_text)
    }
    url = "http://127.0.0.1:5000/learn/LEARNING"
    requests.post(url, json=datas)
    context.bot.send_message(chat_id=chat_id, text="success!")


def idnameupload(update, context)-> None:
    db = pymysql.connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'C:/capstone/pythonProject/capdi-378609-2fc18c110369.json',
        scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open('capstone_question_data')
    worksheet = spreadsheet.worksheet('학생데이터')
    data = worksheet.get_all_values()

    #query = "INSERT INTO testdata (clustering, question, answer) VALUES (%s, %s, %s)"
    query = "INSERT INTO userinfo (num, name) VALUES (%s, %s)"

    for row in data:
        cursor.execute(query, (row[0], row[1]))
    context.bot.send_message(chat_id=chat_id,
                             text="학생데이터 스프레드시트 --> db 성공적으로 입력되었습니다.")
    db.commit()
    db.close()

def mariadbupload(update, context)-> None:
    db = pymysql.connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'C:/capstone/pythonProject/capdi-378609-2fc18c110369.json',
        scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open('capstone_question_data')
    worksheet = spreadsheet.worksheet('학습용질문데이터')
    data = worksheet.get_all_values()

    query = "INSERT INTO testdata (clustering, question, testnum) VALUES (%s, %s, %s)"

    for row in data:
        cursor.execute(query, (row[0], row[1], row[2]))
    context.bot.send_message(chat_id=chat_id,
                             text="구글 스프레드시트 --> db 성공적으로 입력되었습니다.")
    db.commit()
    db.close()

def googlesheetupload(update, context)-> None:
    db = pymysql.connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    global n
    now = datetime.datetime.now()
    print(now)

    n=n+1
    if now.weekday() == 1:

        last_tuesday = now - datetime.timedelta(days=now.weekday(), weeks=1)
        last_tuesday_str = last_tuesday.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(f"SELECT dataset.*, userinfo.* FROM dataset INNER JOIN userinfo ON dataset.id = userinfo.chatid WHERE dataset.timestamp > '{last_tuesday_str}' AND dataset.timestamp < '{now.strftime('%Y-%m-%d %H:%M:%S')}'")
        data = cursor.fetchall()
        print(data)

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'C:/capstone/pythonProject/capdi-378609-2fc18c110369.json',
            scope)
        client = gspread.authorize(creds)

        week_num = last_tuesday.isocalendar()[1]

        try:
            worksheet = client.open('capstone_question_data').worksheet(str(n+7)+"주차") #여기 부분에 작성했음 3/21일 기준 +1
        except gspread.exceptions.WorksheetNotFound:
            worksheet = client.open('capstone_question_data').add_worksheet(title=str(n+7)+"주차", rows=1, cols=1)

        keys = ['num', 'name', 'id', 'type', 'question', 'timestamp']

        for row_index, row_data in enumerate(data):
            row_data_values = [row_data[key] for key in keys]

            row_data_str = [str(cell) for cell in row_data_values]

            range_ = f'A{row_index + 2}:{chr(ord("A") + len(row_data_str))}{row_index + 2}'

            while True:
                try:
                    worksheet.update(range_, [row_data_str])
                    break
                except gspread.exceptions.APIError as e:
                    if e.response.status_code == 429:  # rate limit exceeded
                        print("Quota exceeded, waiting...")
                        time.sleep(60)  # wait for 1 minute
                    else:
                        raise e

        context.bot.send_message(chat_id=chat_id,
                                 text="db --> 구글 스프레드시트로 성공적으로 입력되었습니다.")

    else:
        context.bot.send_message(chat_id=chat_id,
                                 text="시간과 날짜가 맞지않습니다.")
    db.commit()
    db.close()

def help(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id, text="안녕하세요, 한밭대학교 교육용 챗봇입니다.\n" \
                                                   "현재 다음 기능을 제공하고 있습니다.\n" \
                                                   "1.과제 제출(질문) - /soa \n2.수업 질의응답 - /aqa\n3.챗봇 문제풀기 - /chattest\n4.질문 리스트 보기 - /sqd\n" \
                                                   "\n 커맨드를 입력해주시거나 클릭해주세요.")


def Submission_of_assignments(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id, text="과제 제출 기능입니다.\n 사용예시 - [과제 유형]질문 \n*양식을 지켜주세요*\nex)[for문]for문은 반복문인가요?\n\n다른기능을 사용하고 싶으시면 /help를 입력해주세요")
    global user_num
    if chat_id not in user_num:
        user_num[chat_id] = 0
    else:
        user_num[chat_id] = 0


def ai_question_answer(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id,
                             text="AI기반 질의응답 기능입니다.\n 사용예시 - 이번주 과제 알려줘, 교수님 번호 알려줘, 질문과제에 넣은 내용도 됩니다. \n\n다른기능을 사용하고 싶으시면 /help를 입력해주세요")
    global user_num
    if chat_id not in user_num:
        user_num[chat_id] = 1
    else:
        user_num[chat_id] = 1


def chat_test(update, context)-> None:
    db = pymysql.connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    user = update.message.from_user #사용자의 정보
    chat_id = update.message.chat_id
    user_text = update.message.text #사용자의 텍스트
    context.bot.send_message(chat_id=chat_id,
                             text="랜덤 문제 출제 기능입니다.\n 데이터베이스에 저장된 비슷한 유형의 문제 두개를 출제합니다.\n문제를보고 어떤 유형의 문제인지 작성해보세요\n\nex) 출력문에 대한 문제1, 출력문에 대한 문제2 답변: 출력문\n\n다른기능을 사용하고 싶으시면 /help를 입력해주세요")
    global user_num
    if chat_id not in user_num:
        user_num[chat_id] = 2
    else:
        user_num[chat_id] = 2

    sql = "SELECT COUNT(*) FROM testdata"
    cursor.execute(sql)
    testcount = cursor.fetchone()
    print(testcount["COUNT(*)"])

    global rand_num
    if chat_id not in user_num:
        rand_num[chat_id] = random.randint(1, testcount["COUNT(*)"])
        print(rand_num)
    else:
        rand_num[chat_id] = random.randint(1, testcount["COUNT(*)"])

    global rand_cluster
    sql = "SELECT clustering FROM testdata WHERE testnum = %s"
    cursor.execute(sql, rand_num[chat_id])
    rand_cluster[chat_id] = cursor.fetchone()
    print(rand_cluster[chat_id]['clustering'])

    sql = "SELECT question FROM testdata WHERE clustering = %s ORDER BY RAND() LIMIT 2"
    cursor.execute(sql, rand_cluster[chat_id]['clustering'])
    result2 = cursor.fetchall()
    print(result2)


    for row in result2: #반복
        context.bot.send_message(chat_id=chat_id, text=row['question'])#메세지보냄

    db.commit()
    db.close()

def register_handler(update, context)-> None:
    db = pymysql.connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text

    idx = user_text.find('/')
    dbid = user_text[:idx]
    dbname = user_text[idx + 1:]

    select_data = [[dbid, dbname]]
    sql = "SELECT num, name FROM userinfo WHERE num = %s AND name = %s "
    cursor.executemany(sql, select_data)
    result = cursor.fetchone()
    print(dbid, dbname)

    if result is not None:

        sql2 = "SELECT chatid FROM userinfo WHERE num = %s AND name = %s "
        cursor.executemany(sql2, select_data)
        result2 = cursor.fetchone()

        if result2['chatid'] is None:
            select_data2 = [[chat_id, dbid, dbname]]
            print(result2['chatid'])
            sql3 = "UPDATE userinfo SET chatid = %s WHERE num = %s AND name = %s"
            cursor.executemany(sql3, select_data2)
            cursor.execute("CREATE TABLE HB" + str(
                chat_id) + " (id VARCHAR(50) ,type VARCHAR(50),question VARCHAR(500),timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP())")
            db.commit()
            db.close
            context.bot.send_message(chat_id=chat_id, text="로그인 성공!")
            context.bot.send_message(chat_id=chat_id, text=info_message)
            context.dispatcher.remove_handler(register_message_handler)
            return ConversationHandler.END
        else:

            print(chat_id)
            print(result2['chatid'])

            if str(chat_id) == str(result2['chatid']):
                context.bot.send_message(chat_id=chat_id, text="로그인 성공!")
                context.bot.send_message(chat_id=chat_id, text=info_message)
                context.dispatcher.remove_handler(register_message_handler)
                return ConversationHandler.END

            else:
                context.bot.send_message(chat_id=chat_id, text="본인 학번/이름을 입력해주세요 \n/start를 입력하여 다시 로그인 해주시기 바랍니다.")
                context.dispatcher.remove_handler(register_message_handler)
                return ConversationHandler.END


    else:
        context.bot.send_message(chat_id=chat_id, text="학번/이름이 올바르지 않습니다. \n/start를 입력하여 다시 로그인 해주시기 바랍니다.")
        context.dispatcher.remove_handler(register_message_handler)
        return ConversationHandler.END



def start_handler(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=f"안녕하세요 {BOT_NAME}입니다!\n로그인을 위해 학번/이름을 입력해주세요 \n ex) 20101312/홍길동")
    global user_num
    if chat_id not in user_num:
        user_num[chat_id] = 4
    else:
        user_num[chat_id] = 4

    return ENTER_NAME

def handler(update, context)-> None:
    db = pymysql.connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text

    if user_num[chat_id] == 0:
        idx = user_text.find(']')
        type = user_text[1:idx]
        contexts = user_text[idx + 1:]
        sql = "INSERT INTO dataset(id, type, question) VALUES (%s, %s, %s)"
        sql2 = "INSERT INTO HB" + str(chat_id) + " (id, type, question) VALUES (%s, %s, %s)"
        sql3 = "SELECT COUNT(id) FROM HB" + str(chat_id)
        n=1
        if (idx != -1):
            cursor.execute(sql, (chat_id, type, contexts))
            cursor.execute(sql2, (chat_id, type, contexts))
            cursor.execute(sql3)
            result = cursor.fetchone()
            context.bot.send_message(chat_id=chat_id, text="문제유형 :" + type)
            context.bot.send_message(chat_id=chat_id, text="내용 :" + contexts)
            context.bot.send_message(chat_id=chat_id, text="제출완료")
            context.bot.send_message(chat_id=chat_id, text="지금까지 " +str(result['COUNT(id)']) + "개 제출")


        else:
            context.bot.send_message(chat_id=chat_id, text="양식을 맞춰주세요.")
        db.commit()
        db.close()

    elif user_num[chat_id] == 1:
        datas = {
            "query": str(user_text)
        }
        url = "http://127.0.0.1:5000/query/NORMAL"
        response = requests.post(url, json=datas)
        context.bot.send_message(chat_id=chat_id, text=response.json()['Answer'])
        if response.json()['Answer'] == "부정확한 질문이거나 답변할 수 없습니다.":
            sql = "INSERT INTO failanswer (userquery ,aiquery, answer, intent) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql,
                           (str(user_text), response.json()['Query'], response.json()['Answer'],
                            response.json()['Intent']))
        db.commit()
        db.close()

    elif user_num[chat_id] == 2:
        if user_text == rand_cluster[chat_id]['clustering']:
            context.bot.send_message(chat_id=chat_id, text="정답입니다.\n다른문제를 원하시면 /chattest 커맨드를 다시 입력해주세요 ")
            sql = "INSERT INTO testresult (chatid ,useranswer, chatbotanswer) VALUES (%s, %s, %s)"
            cursor.execute(sql,
                           (str(chat_id), str(user_text), rand_cluster[chat_id]['clustering']))
            db.commit()
            db.close()
        else:
            context.bot.send_message(chat_id=chat_id, text="다시 생각해보세요")
            sql = "INSERT INTO testresult (chatid ,useranswer, chatbotanswer) VALUES (%s, %s, %s)"
            cursor.execute(sql,
                           (str(chat_id), str(user_text), rand_cluster[chat_id]['clustering']))
            db.commit()
            db.close()

    elif user_num[chat_id] == 5:
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

    elif user_num[chat_id] == 4:
        context.bot.send_message(chat_id=chat_id, text="커맨드를 다시 입력해주세요")
        db.close()




conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_handler)],
    states={
        ENTER_NAME: [MessageHandler(Filters.text & ~Filters.command, register_handler)],
    },
    fallbacks=[]
)

updater = Updater(token= BOT_token, use_context=True)
dispatcher = updater.dispatcher

register_message_handler = MessageHandler(Filters.text & ~Filters.command, register_handler)
echo_handler = MessageHandler(Filters.text & ~Filters.command, handler)
help_handler = CommandHandler('help', help)
Submission_of_assignments_handler = CommandHandler('soa', Submission_of_assignments)
ai_question_answer_handler = CommandHandler('aqa', ai_question_answer)
chat_test_handler = CommandHandler('chattest', chat_test)
google_sheet_upload = CommandHandler('googlesheetupload', googlesheetupload)
mariadb_upload = CommandHandler('mariadbupload', mariadbupload)
id_name_upload = CommandHandler('idnameupload', idnameupload)
intent_learning = CommandHandler('intentlearning', intentlearning)
student_querydata = CommandHandler('sqd', studentquerydata)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(register_message_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(Submission_of_assignments_handler)
dispatcher.add_handler(ai_question_answer_handler)
dispatcher.add_handler(chat_test_handler)
dispatcher.add_handler(google_sheet_upload)
dispatcher.add_handler(mariadb_upload)
dispatcher.add_handler(id_name_upload)
dispatcher.add_handler(intent_learning)
dispatcher.add_error_handler(error_handler)
dispatcher.add_handler(student_querydata)

updater.start_polling()

# -*- coding: utf-8 -*-
import time
import asyncio
import telegram
import pymysql
import threading
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import requests
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import logging
from telegram import Update, error
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

BOT_token = ""
BOT_NAME = ''

host = "127.0.0.1"
port = 5050

user_variables = {}
user_threads = {}
n=0

global NUM
NUM=4

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

db = pymysql.connect(host='', user='', password='', db='', charset='', port=)
cursor = db.cursor(pymysql.cursors.DictCursor)
bot = telegram.Bot(BOT_token)

info_message = "안녕하세요, 파이썬 프로그래밍 중간고사 챗봇입니다.\n" \
                  "유의사항을 공지하겠습니다. 미숙지시 불이익은 본인에게 있습니다.\n" \
                  "1. 총 20문제이며, 다음 문제를 원할시 [/next] 이라고 입력해주시고, 이전문제로 돌아갈시 [/previous] 이라고 입력해주세요 \n 2. 답의 수정을 원할경우 원하는 문제로 [/next], [/previous]을 하시고 답을 다시 입력해주시면 됩니다. \n 3. 문제를 다 푸신 분들은 [/finish]를 입력해주시고 퇴실해주시면 됩니다. 제출하기를 입력하시면 다시 답을 수정할 수 없으므로 확실하실 때 입력해주시길 바랍니다. \n 4. 답안 제출이 완료되면, n번 문제 입력된 답은 : 입니다. 라고 출력되오니 꼭 확인 해주시길 바랍니다.  출력이 되지않으면 다시 입력해주시길 바랍니다. \n 5. 부정행위 적발시 0점처리되오니 기본적인 매너를 지켜주시길 바랍니다. \n" \
                  "\n /next 을 입력하여 문제를 풀어주시길 바랍니다."

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

def googlesheetupload(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    cursor.execute(
        f"SELECT examdata.*, userinfo.* FROM examdata INNER JOIN userinfo ON examdata.id = userinfo.chatid ")
    data = cursor.fetchall()
    scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
            'C:/capstone/pythonProject/capdi-378609-2fc18c110369.json',
            scope)
    client = gspread.authorize(creds)

    worksheet = client.open('capstone_question_data').worksheet("중간고사 학생 데이터")

    keys = ['id', 'name', 'num', 'question', 'answer', 'timestamp']

    for row_index, row_data in enumerate(data):
        row_data_values = [row_data[key] for key in keys]

        row_data_str = [str(cell) for cell in row_data_values]

        range_ = f'A{row_index + 2}:{chr(ord("A") + len(row_data_str))}{row_index + 2}'

        worksheet.update(range_, [row_data_str])

        context.bot.send_message(chat_id=chat_id,
                                 text="db --> 구글 스프레드시트로 성공적으로 입력되었습니다.")



def end_handler(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    user_threads = {}
    if chat_id in user_threads and user_threads[chat_id].is_alive():
        user_threads[chat_id].do_run = False
        user_threads[chat_id].join()
        print("죽었따.")
    else:
        print("살아있다.")
    global NUM
    NUM = 0
    context.bot.send_message(chat_id=chat_id,
                             text="챗봇 중간고사를 종료합니다. \n수고하셨습니다. \n감독관의 지시에 따라 행동해주시면 됩니다.")


def start_handler(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=info_message)


def next(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    global user_variables
    if chat_id not in user_variables:
        user_variables[chat_id] = 1
    else:
        user_variables[chat_id] = user_variables[chat_id] + 1
    print(user_variables[chat_id])
    try:

        sql = "SELECT mtquestion FROM middleterm where mtnum = %s"
        cursor.execute(sql, user_variables[chat_id])
        testdata = cursor.fetchone()
        context.bot.send_message(chat_id=chat_id,
                                 text=testdata['mtquestion'])
        global NUM
        NUM = 1

        db.commit()
    except:
        context.bot.send_message(chat_id=chat_id,
                                 text="문제는 20번까지 입니다.")

def previous(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text
    global user_variables

    if chat_id not in user_variables:
        user_variables[chat_id] = 1
    else:
        user_variables[chat_id] = user_variables[chat_id] - 1
    print(user_variables[chat_id])
    try:
        sql = "SELECT mtquestion FROM middleterm where mtnum = %s"
        cursor.execute(sql, user_variables[chat_id])
        testdata = cursor.fetchone()
        context.bot.send_message(chat_id=chat_id,
                                 text=testdata['mtquestion'])
        global NUM
        NUM = 1

        db.commit()
    except:
        context.bot.send_message(chat_id=chat_id,
                                 text="문제는 1번부터 시작입니다.")

def handler(update, context)-> None:
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_text = update.message.text

    if NUM == 0:
        pass

    elif NUM == 1:

        try:
            sql1 = "SELECT mtquestion FROM middleterm where mtnum = %s"
            cursor.execute(sql1, user_variables[chat_id])
            question = cursor.fetchone()
            sql2 = "INSERT INTO examdata (id, question, answer) VALUE (%s, %s, %s)"
            cursor.execute(sql2, (chat_id, question['mtquestion'], user_text))
            sql3 = "UPDATE mid%s SET aw = %s, pb = %s WHERE testnum = %s"
            cursor.execute(sql3, (chat_id, user_text, question['mtquestion'], user_variables[chat_id]))
            testdata = cursor.fetchone()
            context.bot.send_message(chat_id=chat_id,
                                 text=str(user_variables[chat_id])+"번 문제에 입력된 답은 \n"+str(user_text)+" ")
            context.bot.send_message(chat_id=chat_id,
                                     text="/next\n\n/previous")
            db.commit()
        except:
            context.bot.send_message(chat_id=chat_id,
                                     text="에러가 발생했습니다.")

updater = Updater(token= BOT_token, use_context=True)
dispatcher = updater.dispatcher

start_handler=CommandHandler('start', start_handler)
echo_handler = MessageHandler(Filters.text & ~Filters.command, handler)
google_sheet_upload = CommandHandler('googlesheetupload', googlesheetupload)
end_handler = CommandHandler('finish', end_handler)
next = CommandHandler('next', next)
previous = CommandHandler('previous', previous)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(google_sheet_upload)
dispatcher.add_error_handler(error_handler)
dispatcher.add_handler(next)
dispatcher.add_handler(previous)
dispatcher.add_handler(end_handler)


updater.start_polling()
updater.job_queue.start()

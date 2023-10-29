import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from konlpy.tag import Komoran
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

tokenizer = Komoran()

exclusion_tags = [
    'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
    'JX', 'JC',
    'SF', 'SP', 'SS', 'SE', 'SO',
    'EP', 'EF', 'EC', 'ETN', 'ETM',
    'XSN', 'XSV', 'XSA'
]


class CreateTraindata:
    def __init__(self):
        self.traindata()
        self.label_count = None
        self.keyword_ai = None

    def traindata(self):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            '',
            scope)
        client = gspread.authorize(creds)

        worksheet = client.open('capstone_question_data').worksheet("AI학습용가공데이터")

        data = worksheet.get_all_values()

        text_column = [row[0] for row in data]
        query_column = [row[1] for row in data]
        answer_column = [row[2] for row in data]

        keyword_ai = list(set(text_column))
        query = list(query_column)
        answer = list(answer_column)

        querydata = {}
        answerdata = {}
        labeldata = {}
        aidata = {}

        train_dfs = []

        for keyword in keyword_ai:
            querydata[keyword] = []
            answerdata[keyword] = []
            aidata[keyword] = []
        a = 2
        for keyword in keyword_ai:
            a = a + 1
            for row in data:
                if keyword == row[0]:
                    aidata[keyword].append(row[1])
                    aidata[keyword].append(row[2])

            len(aidata[keyword])
            labeldata[keyword] = []

            for _ in range(len(aidata[keyword])):
                labeldata[keyword].append(a)
            len(labeldata[keyword])

            train2_df = pd.DataFrame({'text': aidata[keyword],
                                      'label': labeldata[keyword]})
            train_dfs.append(train2_df)

        qnatrain_df = pd.concat(train_dfs, ignore_index=True)

        total = pd.read_csv("C:/capstone/통합본데이터.csv")

        total.dropna(inplace=True)

        all_data = list(total['text']) + list(query_column) + list(answer_column)

        len(all_data)

        print(len(all_data))

        class1 = []
        hw = []
        number = []

        etc = []

        for i in all_data:
            if ('수업' or '강의') in i:
                class1.append(i)
            elif ('과제' or '숙제' or '레포트') in i:
                hw.append(i)
            elif ('번호' or '전화' or '연락처') in i:
                number.append(i)
            else:
                etc.append(i)

        len(number)

        number_label = []
        for _ in range(len(number)):
            number_label.append(0)
        len(number_label)

        len(class1)
        class1_label = []
        for _ in range(len(class1)):
            class1_label.append(1)
        len(class1_label)

        len(hw)
        hw_label = []
        for _ in range(len(hw)):
            hw_label.append(2)
        len(hw_label)

        train_df = pd.DataFrame({'text': number + class1 + hw,
                                 'label': number_label + class1_label + hw_label})

        train_df = pd.concat([train_df, qnatrain_df], ignore_index=True)

        label_count = a
        self.label_count = label_count
        self.keyword_ai = keyword_ai

        train_df.reset_index(drop=True, inplace=True)

        train_df.to_csv("C:/capstone/train_data.csv", index=False)
        data = pd.read_csv('C:/capstone/train_data.csv')

        data.shape

        data_tokenized = [[token + "/" + POS for token, POS in tokenizer.pos(text_)] for text_ in data['text']]

        f = lambda x: x in exclusion_tags

        data_list = []
        for i in range(len(data_tokenized)):
            temp = []
            for j in range(len(data_tokenized[i])):
                if f(data_tokenized[i][j].split('/')[1]) is False:
                    temp.append(data_tokenized[i][j].split('/')[0])
            data_list.append(temp)

        num_tokens = [len(tokens) for tokens in data_list]
        num_tokens = np.array(num_tokens)

        # 평균값, 최댓값, 표준편차
        print(f"토큰 길이 평균: {np.mean(num_tokens)}")
        print(f"토큰 길이 최대: {np.max(num_tokens)}")
        print(f"토큰 길이 표준편차: {np.std(num_tokens)}")

        select_length = 25

        def below_threshold_len(max_len, nested_list):
            cnt = 0
            for s in nested_list:
                if (len(s) <= max_len):
                    cnt = cnt + 1

            print('전체 샘플 중 길이가 %s 이하인 샘플의 비율: %s' % (max_len, (cnt / len(nested_list))))

        below_threshold_len(select_length, data_list)
        return



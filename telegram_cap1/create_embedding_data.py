import pandas as pd
from tqdm import  tqdm
tqdm.pandas()

import torch
from sentence_transformers import SentenceTransformer

"""
train_file = "C:/Users/82105/OneDrive/바탕 화면/캡스톤디자인/텍스트 전처리/질문 답변 데이터.xlsx"
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

df = pd.read_excel(train_file)
df['embedding_vector'] = df['질문(Query)'].progress_map(lambda x: model.encode(x))
df.to_excel("C:/Users/82105/OneDrive/바탕 화면/캡스톤디자인/텍스트 전처리/train_data_embedding.xlsx", index = False)

embedding_data = torch.tensor(df['embedding_vector'].tolist())
torch.save(embedding_data, 'C:/Users/82105/OneDrive/바탕 화면/캡스톤디자인/텍스트 전처리/embedding_data.pt')
"""

class CreateEmbeddingData:
    def __init__(self, preprocess, df):

        #텍스트 전처리기
        self.p = preprocess

        #질문 데이터 프레임
        self.df = df

        self.model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

    def create_pt_file(self):
        #질문 목록 리스트
        target_df = list(self.df['질문(Query)'])

        #형태소 분석
        for i in range(len(target_df)):
            sentence = target_df[i]
            pos = self.p.pos(sentence)
            keywords = self.p.get_keywords(pos, without_tag=True)
            temp = ""
            for k in keywords:
                temp += str(k)
            target_df[i] = temp
        
        self.df['질문 전처리'] = target_df
        self.df['embedding_vector'] = self.df['질문 전처리'].progress_map(lambda x: self.model.encode(x))
        embedding_data = torch.tensor(self.df['embedding_vector'].tolist())
        torch.save(embedding_data, 'C:/capstone/embedding_data.pt')
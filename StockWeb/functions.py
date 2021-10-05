import re
from eunjeon import Mecab
import plotly.graph_objects as go
import pandas as pd
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
from datetime import timedelta

mecab = Mecab()


# containers = ['NNG', 'NNP', 'NNB', 'NNBC', 'NR', 'NP', 'VV', 'VA', 'VX', 'VCP', 'VCN', 'MM']
# stop_words = ['JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC']
# hangul = re.compile('[^가-힣]+')
# sss_compile = re.compile('[^0-9a-zA-Z가-힣\s]')

# 분석과정
def preprocessing(review_data):
    for i in range(len(review_data)):
        review_data.loc[i, 'review'] = re.sub('[^0-9가-힣\s]', '', review_data.loc[i, 'review'])
    review_data = review_data.dropna().reset_index(drop=True)
    return review_data


def morphs_pos(review_data):
    review_data_list = []
    for i in range(len(review_data)):
        rev = mecab.pos(review_data.loc[i, 'review'])  # mecab
        review_data_list.append(rev)
    return review_data_list


def return_nouns(review_data):
    nouns = []
    for i in range(len(review_data)):
        noun = mecab.pos(review_data.loc[i, 'review'])
        f_noun = [w for w, v in noun if v == 'NNG']  # or v=='VV' or v=='VX' or v='VA
        nouns.append(f_noun)
    return nouns


def count_noun(nouns):
    vocab = dict()
    for words in nouns:
        for word in words:
            if word not in vocab:
                vocab[word] = 1
            else:
                vocab[word] += 1
    vocab_sorted = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
    return vocab_sorted


def check_vocab(t, review_data_list):
    t.fit_on_texts(review_data_list)
    vocab_size = len(t.word_index) + 1
    return vocab_size


def return_keyword(review_data):
    review_data = pd.DataFrame(review_data, columns=['review']).reset_index(drop=True)
    review_data = preprocessing(review_data)  # 전처리
    review_data_list = morphs_pos(review_data)  # 형태소 토큰화
    nouns = return_nouns(review_data)  # 명사 추출
    vocab_sorted = count_noun(nouns)  # 명사 키워드
    check_vocab = [word for word in vocab_sorted if len(word[0]) > 1]  # 20개 출력

    return check_vocab[:20]


def stock_chart(stock_num, abnormal,pred_rate):
    time = pd.read_csv(
        "static/stock_data/{}.csv".format(stock_num),
        parse_dates=["Date"],
        index_col="Date"
    )
    time = time.reset_index()[['Date', 'price']]
    time.columns = ['date', 'released']


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time['date'], y=time['released'], name="Stock Price"))

    fig.add_trace(go.Scatter(x=pd.Series(time.loc[[len(time)-2,len(time)-1],'date']) + timedelta(days=1), y=pd.concat([pd.Series(time.loc[len(time)-2, 'released']),pd.Series(time.loc[len(time)-1,'released'] *( 1+ pred_rate))]), name="Predict"))

    fig.update_layout(plot_bgcolor='#f6f5fc')

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#f6f5fc",
    )

    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,

    ))

    # input_abnormal_detect_date
    for i in abnormal:
        fig.add_vrect(x0=i[0], x1=i[1], fillcolor="green", opacity=0.25, line_width=0)

    a = fig.to_json()
    return a, fig


# stock_name = '000270_기아'
# abnormal = [("2016-09-24", "2016-10-18"), ("2015-09-24", "2015-10-18")]
#
# a,fig = stock_chart(stock_name,abnormal)
# fig.show()
# print(a)

def Crawling(search_text, start_date, end_date):
    titles = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    for i in range(1, 51, 10):
        try:
            url_basic = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=1&photo=0&field=0&pd=3&ds={}&de={}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:from20210810to20210814,a:all&start={}'.format(
                search_text, start_date, end_date, i)

            data = requests.get(url_basic, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')

            news_titles = soup.find_all('a', attrs={'class': 'news_tit'})

            for title in news_titles:
                titles.append([title['title'], title['href']])
        except:
            pass

    return titles


# stock = '삼성전자'
# search_text = '{}+주식'.format(stock)
# # 검색 키워드 형식 -> 1) +주식, -주식, 주식 | 하락,  "이재용 출소", 섞어서 사용가능
# start_date = '2021.08.10'
# end_date = '2021.08.14'


def get_title_and_url(stock_name, start_date, end_date):
    search_text = '{} +주식'.format(stock_name)
    only_title = []
    titles = Crawling(search_text, start_date, end_date)
    for title in titles:
        only_title.append(title[0])
    keywords = return_keyword(only_title)
    return titles[:5], keywords


def make_wordcloud(stock_name, idx, start_date, end_date):
    mask = Image.open('./cloud.png')
    mask = np.array(mask)
    titles, keywords = get_title_and_url(stock_name, start_date, end_date)
    keyword_dict = {word: num for word, num in keywords}
    if keyword_dict:
        try:
            wc = WordCloud(font_path='210Black.ttf', width=1000, height=600, background_color="#000000", random_state=0,
                           mask=mask)
            plt.figure(figsize=(23, 18), facecolor='#FAF1E6')
            plt.imshow(wc.generate_from_frequencies(keyword_dict))
            wc.to_file('static/wordcloud/{}_{}.jpg'.format(stock_name,idx))
        except:
            pass

    return titles


def make_abnormal_date(path_csv):
    data = pd.read_csv(path_csv)
    data.columns = ['index', 'Date']
    date = []
    test = data.loc[1, 'index'] - data.loc[0, 'index']
    while test != 1:
        data = data.drop([0]).reset_index(drop=True)
        test = data.loc[1, 'index'] - data.loc[0, 'index']
    for i in range(len(data)):
        if i - 1 < 0:
            flag = 0
            continue
        prev_idx = data.loc[i - 1, 'index']
        prev_date = data.loc[i - 1, 'Date']
        cur_idx = data.loc[i, 'index']
        cur_date = data.loc[i, 'Date']
        if cur_idx - prev_idx == 1:
            if flag == 0:
                start = prev_idx
                date.append(prev_date)
                flag = 1
            if i == len(data) - 1:
                date.append(cur_date)
        else:
            if start == 0:
                continue
            date.append(prev_date)
            start = 0
            flag = 0
    result = []
    for i in range(0, len(date), 2):
        result.append([date[i], date[i + 1]])

    return result

def make_logo_img(stock_name):
    png = 'static/logo_img/{}.png'.format(stock_name)
    jpg = 'static/logo_img/{}.jpg'.format(stock_name)
    svg = 'static/logo_img/{}.svg'.format(stock_name)
    if os.path.exists(png):
        return '/logo_img/{}.png'.format(stock_name)
    elif os.path.exists(jpg):
        return '/logo_img/{}.jpg'.format(stock_name)
    elif os.path.exists(svg):
        return '/logo_img/{}.svg'.format(stock_name)
    else:
        return ''

def make_date(ll):
    text = ''
    for l in ll:
        text += re.sub('-','.',l)
        text += ' '

    return text.strip()
#
# from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.layers import Embedding, Dense,LSTM, Dropout
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential
# from keras import optimizers
# from tensorflow import keras
# from keras import models, layers
# from sklearn.preprocessing import MinMaxScaler
#

# def tensorflow_version():
#     models_h5 = os.listdir('static/predict_model')
#     price_data = os.listdir('static/stock_data')
#     arr = []
#     for mod in models_h5:
#         data = pd.read_csv(f"static/predict_model/{mod.split('.')[0]}.csv")
#         scaler = MinMaxScaler()
#         data = data[data.columns[1:]]
#         data_processing = scaler.fit_transform(np.array(data))
#         data_processing = pd.DataFrame(data_processing)
#         new_model = models.load_model(f'static/predict_model/{mod}')
#
#         a = new_model.predict(np.array(data_processing[-6:-1]).reshape(-1, 5, 10))
#         va = (a - data_processing.iloc[-2][0]) / data_processing.iloc[-2][0] * 100
#
#         #
#         if -5 <= va <= 5:
#             arr.append(stock_list[mod.split(".")[0]], round(float(va), 2))
#         elif -50 <= va <= -5 or 5 <= va <= 50:
#             arr.append(stock_list[mod.split(".")[0]], round(float(va) / 10, 2))
#         else:
#             arr.append(stock_list[mod.split(".")[0]], round(float(va) / 100, 2))
    # Tensorflow 오류로인한 배열값 대체

#
#
# print(calcul_rate)
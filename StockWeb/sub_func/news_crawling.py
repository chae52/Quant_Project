import requests
from bs4 import BeautifulSoup
from functions import return_keyword
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter

mask = Image.open('../cloud.png')
mask = np.array(mask)

def Crawling(search_text, start_date, end_date):
    titles = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    for i in range(1, 201, 10):
        try:
            url_basic = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=2&photo=0&field=0&pd=3&ds={}&de={}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,a:all&start={}'.format(
                search_text, start_date, end_date, i)
            print(url_basic)
            data = requests.get(url_basic, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')

            news_titles = soup.find_all('a', attrs={'class': 'news_tit'})

            for title in news_titles:
                titles.append([title['title'], title['href']])
        except:
            pass

    return titles


stock = '삼성전자'
search_text = '{} +주식'.format(stock)
# 검색 키워드 형식 -> 1) +주식, -주식, 주식 | 하락,  "이재용 출소", 섞어서 사용가능
start_date = '2018.05.08'
end_date = '2018.06.18'


def get_title_and_url(search_text, start_date, end_date):
    only_title = []
    titles = Crawling(search_text, start_date, end_date)
    for title in titles:
        only_title.append(title[0])
    keywords = return_keyword(only_title)
    return titles, keywords

def make_wordcloud(keywords):
    keyword_dict = {word:num for word,num in keywords}

    wc = WordCloud(font_path='../210Black.ttf', width=1000, height=600, background_color="#000000", random_state=0, mask=mask)
    plt.figure(figsize=(20, 10), facecolor='#000000')
    plt.imshow(wc.generate_from_frequencies(keyword_dict))
    wc.to_file('./wordcloud.jpg')

titles, keywords = get_title_and_url(search_text, start_date, end_date)
print(titles)
print(keywords)
# make_wordcloud(keywords)

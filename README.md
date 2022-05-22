# 개요

<code>`본 프로젝트는 세종대학교 2021 SW/AI 해커톤를 통해 진행되었습니다. 🏆장려상 수상`</code> 
2021.10.1 ~ 2 (무박 2일)

퀀트란 Quantitative 와 Analyst의 합성어로, 수학 및 통계에 기반해 투자 모델을 만들거나 금융 시장 변화 예측을 말합니다. 

- Kospi 시가총액 상위 100개의 주가를 ML/DL 방식을 이용하여 다음날의 주가를 예측하고 종목을 추천합니다.

- Abnormal Detection을 이용하여 이상치를 감지하여 이를 시각화합니다.
- 이상치 감지를 통해 검출된 기간의 뉴스를 NLP를 통해 시각화합니다.
- 효율적인 접근성 고려하여 웹사이트 제작을 통해 서비스를 배포합니다.

<br>


### 차별성

- 다양한 변수 사용 - 다른 모델과 다르게, 주가 뿐만 아니라 주가에 큰 영향을 미치는 변수들을 사용
- 개별 모델 사용 - 변동성이 큰 종목장세에서 전략적 대응을 위한 기업별 개별 모델 학습


<br>

### 기술스택

- Python - Pandas / Numpy / Matplotliib / bs4 / WordCloud

- ML/DL - LSTM / AutoEncoder ( LSTM / KNN )
- Frontend - HTML / CSS / JavaScripts
- Backend - Django

<br>

### 사용 데이터셋 ( 10년치 )

해당 데이터셋 선정이유는 다음 사이트를 참고하세요 ( 이후 추가예정 )

- Kospi 시가총액 100개 기업 주가
- Kospi 외국인 / 기관 수급
- High yield spread
- WTI - Crude Oil Price
- US 500 지수
- 상해 지수
- 미국 10년 금리
- Dollar Index
- 원/달러 환율

### Web
![image](https://user-images.githubusercontent.com/41178045/169684112-c71aab9b-8ebb-4af8-8d1f-2d18d071adeb.png)
- 그래프에 하이라이트된 구간은 이상치 감지를 통해 평소와 다른 그래프를 나타낸 구간을 표현했습니다.
- 구간의 날짜에 해당하는 주식과 관련한 뉴스를 표시했습니다.
- 가져온 연관 뉴스들의 키워들 word cloud로 요약했습니다.

<br>

### 예측 mse va_loss

| 종목명           | validation_loss |
| ---------------- | --------------- |
| 셀트리온         | 0.02246         |
| SK               | 0.00047         |
| SK텔레콤         | 0.00042         |
| 삼성물산         | 0.00109         |
| 현대모비스       | 0.00024         |
| 삼성전자우       | 0.00094         |
| 삼성전자         | 0.00202         |
| 삼성SDI          | 0.00486         |
| POSCO            | 0.00008         |
| 현대차           | 0.00027         |
| SK하이닉스       | 0.00054         |
| 기아             | 0.00037         |
| Naver            | 0.00385         |
| LG화학           | 0.00287         |
| 카카오           | 0.00055         |
| LG생활건강       | 0.01420         |
| 신한지주         | 0.00027         |
| 삼성바이오로직스 | 0.03506         |
| KB금융           | 0.0055          |
| SK이노베이션     | 0.0010          |
| LG전자           | 0.0105          |


<br>
#### 잘되면 창업 
#### 팀원 : [김찬영](https://github.com/kochanha) / [박정빈](https://github.com/wjdqlsdlsp) / [박승일](https://github.com/bob8dod) / [이재훈](https://github.com/dlwogns1205) / [이채원](https://github.com/chae52)

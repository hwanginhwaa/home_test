# Overwatch Data Analysis
# OverView

<크롤링 사이트>

![image](https://user-images.githubusercontent.com/27941099/83348393-2838ee00-a367-11ea-97ec-5d11f89184f0.png)

![image](https://user-images.githubusercontent.com/27941099/83349291-afd62b00-a36e-11ea-94cf-d9392d823f99.png)

출처: https://overwatch.op.gg/



<크롤링 결과>

| Rank  | Nickname | Rating      | Win  | Lose  | Win_rate | Kill | Death | K/D  | Time_on_Fire | Level | Playtime | Most1 | Most2      | Most3    |            |
| :---- | :------- | :---------- | :--- | :---- | :------- | :--- | :---- | :--- | :----------- | :---- | :------- | :---- | :--------- | :------- | ---------- |
| 0     | 1        | Viol2t      | 4569 | 59.0  | 31.0     | 66   | 22.4  | 7.4  | 3.02         | 94    | 839      | 17.0  | Baptiste   | Sigma    | Widowmaker |
| 1     | 2        | Water       | 4541 | 231.0 | 174.0    | 57   | 22.5  | 8.6  | 2.61         | 75    | 2349     | 85.0  | Genji      | Baptiste | Hanzo      |
| 2     | 3        | Z9Hong      | 4518 | 106.0 | 55.0     | 66   | 21.2  | 7.3  | 2.92         | 58    | 68       | 29.0  | Hanzo      | Orisa    | Roadhog    |
| 3     | 4        | AnsanSniper | 4506 | 32.0  | 22.0     | 59   | 18.1  | 6.8  | 2.66         | 85    | 469      | 11.0  | Baptiste   | Zenyatta | Ana        |
| 4     | 5        | uaena       | 4498 | 170.0 | 110.0    | 61   | 23.6  | 7.0  | 3.36         | 84    | 931      | 54.0  | Widowmaker | McCree   | Zarya      |
| ...   | ...      | ...         | ...  | ...   | ...      | ...  | ...   | ...  | ...          | ...   | ...      | ...   | ...        | ...      | ...        |
| 22295 | 22296    | designer    | 1206 | 30.0  | 38.0     | 44   | 18.1  | 6.7  | 2.69         | 50    | 777      | 12.0  | Reinhardt  | Zarya    | Ana        |
| 22296 | 22297    | leesj       | 1204 | 22.0  | 26.0     | 46   | 18.9  | 7.5  | 2.53         | 71    | 285      | 8.0   | Ana        | McCree   | Reinhardt  |
| 22297 | 22298    | 세준띠      | 1204 | 26.0  | 28.0     | 48   | 19.1  | 8.2  | 2.33         | 57    | 324      | 10.0  | Reinhardt  | Reaper   | Ana        |
| 22298 | 22299    | 도현        | 1204 | 28.0  | 33.0     | 46   | 14.4  | 9.6  | 1.49         | 33    | 153      | 11.0  | Reinhardt  | Ana      | Zarya      |
| 22299 | 22300    | 숨겨진트롤  | 1203 | 41.0  | 26.0     | 61   | 29.0  | 7.1  | 4.05         | 176   | 156      | 12.0  | Hanzo      | McCree   | Roadhog    |

22300 rows × 15 columns



requests와 beautifulsoup(Python 라이브러리)를 이용하여 오버워치 전적 검색 사이트 op.gg를 크롤링.

numpy와 pandas를 이용하여 크롤링한 데이터를 데이터프레임 변환 및 전처리

~~pandas와  matplotlib 및 seaborn을 이용하여 데이터 분석~~  (코로나 사태로 인해 학교 서버 이용 불가)



# Requirements

- python 3.6
- Numpy (배열 처리 및 연산 라이브러리)
- Pandas (데이터 처리 및 분석 라이브러리)
- Requests (HTTP 요청 라이브러리)
- Beautifulsoup (크롤링 라이브러리)
- Matplotlib & Seaborn (데이터 시각화 라이브러리)



만약 저와 같은 환경에서 작업하고 싶으신 분들은 Anaconda Prompt에 들어가셔서 

```
pip install -r requirements.txt
```

입력하시면 됩니다.



사실 설치한 라이브러리가 많이 없기 때문에 없는 라이브러리만

```
pip install <라이브러리 이름>
```

입력하시면 됩니다.



저는 jupyter Notebook에서 작업을 했기 때문에 가급적 그에 맞춰서 작업해주시면 감사하겠습니다.



# File

- 고급시계.ipynb: 간단하게 오버워치 데이터를 크롤링한 심플 코드입니다.

- overwatch_rank.ipynb: 본격적으로 오버워치 데이터를 처음(천상계)부터 끝까지(심해) 유저 데이터를 크롤링한 코드입니다. 고급시계.ipynb보다 변수가 더 추가되었습니다.

- overwatch rank_add detail_crawling.ipynb: 유저 심층 데이터를 크롤링하여 기존 데이터(overwatch_rank.ipynb) 추가한 코드입니다. 변수 추가.

- ~~detail_data_cleaning.ipynb: 심층 데이터(overwatch rank_add detail_crawling.ipynb)들을 전처리하는 코드입니다.~~ 


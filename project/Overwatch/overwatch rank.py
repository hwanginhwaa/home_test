#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 크롤링
import requests
from bs4 import BeautifulSoup

# 데이터 분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # 크롤링

# In[4]:


data = []

def find_tag(tag, class1):
    result = tr.find(tag, class_=class1)
    if result != None:
        row.append(result.get_text())
    else: row.append(-1)
    
for page in range(1,224):

    url = 'https://overwatch.op.gg/leaderboards?platform=pc&role_id=0&page={}'.format(page)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text)

    # table tag
    table = soup.find('table', class_='LeaderBoardsTable')

    # tag
    for tr in table.find('tbody').find_all('tr'):
        row = []
        # #, 플랫폼 
        for span in tr.find_all('span'):
            row.append(span.get_text())
        # 플레이어, K/D, 승률
        for b in tr.find_all('b'):
            row.append(b.get_text())
        # 레벨, 상세 K/D
        for em in tr.find_all('em'):
            row.append(em.get_text().strip())
        # 점수
        find_tag('td', 'ContentCell ContentCell-SkillRating')
        #  폭주 시간
        find_tag('td', 'ContentCell ContentCell-AvgFire')
        # 승
        find_tag('div', 'Win')
        # 패
        find_tag('div', 'Lose')
        # 플레이 시간
        find_tag('td', 'ContentCell ContentCell-PlayTime')
        # 모스트 영웅
        for heros in tr.find_all('td', class_='ContentCell ContentCell-MostHeros'):
            for hero in heros.find_all('img', alt=True): # 모스트 영웅은 img로 되어 있다.
                row.append(hero['alt'])
        # 하나의 행을 data에 축적
        data.append(row)
    
    # 진행사항 출력
    if page % 10 == 0:
        print(page, " page complete")
print("Mission complete")
df = pd.DataFrame(data)


# In[5]:


df


# # 전처리

# In[6]:


# header 이름 설정
df.columns = ['Rank', 'Platform', 'Nickname', 'K/D', 'Win_rate', 'Level', 'Kill/Death', 'Rating', 'Time_on_Fire', 
     'Win', 'Lose', 'Playtime', 'Most1', 'Most2', 'Most3']
df.head()


# In[7]:


df.info()


# In[8]:


# Rank
df['Rank'] = df['Rank'].str.replace(',', '')
df['Rank']


# In[9]:


# K/D 컬럼
df['K/D'] = df['K/D'].str.replace(': 1', '')
df['K/D']


# In[10]:


# Level
df['Level'] = df['Level'].str.replace('Lv.', '')
df['Level']


# In[11]:


# Kill/Death
df['Kill/Death'] = df['Kill/Death'].str.replace('\n', '')

# separate
new = df['Kill/Death'].str.split('/', expand=True)
df['Kill'] = new[0]
df['Death'] = new[1]

df[['Kill/Death', 'Kill', 'Death']]


# In[12]:


# rating
df['Rating'] = df['Rating'].str.replace('\n', '').str.strip()
df['Rating']


# In[13]:


# Time on Fire
df['Time_on_Fire'] = df['Time_on_Fire'].str.replace('\n', '').str.strip()
time = df['Time_on_Fire'].str.split(':')

def to_seconds(x):
    # error
    if len(x) != 2:
        return -1
    
    x = list(map(int, x))
    result = 0
    # 1 min = 60 sec
    if x[0] > 0:
        result = 60 * x[0]
    result += x[1]
    return(result)

df['Time_on_Fire'] = time.apply(to_seconds)


# In[14]:


df['Time_on_Fire']


# In[15]:


# Win
df['Win'] = df['Win'].str.replace('W', '').str.strip()
df['Win']


# In[16]:


# Lose
df['Lose'] = df['Lose'].str.replace('L', '')
df['Lose']


# In[17]:


# PlayTime
df['Playtime'] = df['Playtime'].str.replace('hour[s]*', '')
# 1시간도 하지 않은 관측치 수정
mins_player = df['Playtime'].str.contains('mins')
def mins_to_hours(x):
    print(x, '가 검출되었습니다')
    x = x.replace('mins','').strip()
    x = int(x)/60
    return str(round(x,2))


# 해당 관측치의 Playtime만 수정한다
if len(df.loc[mins_player]) > 0:
    df.loc[mins_player, 'Playtime'] = df.loc[mins_player, 'Playtime'].apply(mins_to_hours)
    
    
df[mins_player]


# In[18]:


df


# ## 데이터 형변환

# In[19]:


df.info()


# In[20]:


# float
df[['K/D', 'Kill', 'Death', 'Win', 'Lose', 'Playtime']] = df[['K/D', 'Kill', 'Death', 'Win', 'Lose', 'Playtime']].astype(float)
print(df[['K/D', 'Kill', 'Death', 'Win', 'Lose', 'Playtime']].dtypes)

# int
df[['Win_rate', 'Level', 'Rating', 'Rank']] = df[['Win_rate', 'Level', 'Rating', 'Rank']].astype(int)
print(df[['Win_rate', 'Level', 'Rating', 'Rank']].dtypes)


# In[21]:


df.info()


# In[22]:


# 불필요한 변수 삭제
del df['Kill/Death']
del df['Platform']


# In[23]:


# 컬럼 순서 바꾸기
df = pd.DataFrame(df, columns=['Rank', 'Nickname', 'Rating', 'Win', 'Lose', 'Win_rate', 'Kill', 'Death', 
                          'K/D', 'Time_on_Fire', 'Level', 'Playtime', 'Most1', 'Most2', 'Most3'])
df


# ## 변수 생성 

# In[54]:


# 티어 변수 생성
bins = [0, 1500, 2000, 2500, 3000, 3500, 4000, 5000]
labels = ['bronze', 'silver', 'gold', 'platinum', 'diamond', 'master', 'grand_master']
df['Tire'] = pd.cut(df['Rating'], bins, labels=labels)


# 상위 1위 ~ 500위는 순위 자체가 티어가 된다.
df['Tire'] = df['Tire'].astype(str)
df.loc[df['Rank'] <= 500, 'Tire'] = df.loc[df['Rank'] <= 500,'Rank'].astype(str)
df.iloc[490:510, :]


# In[6]:


df = pd.read_csv('rank.csv')
df[df['Nickname'] == 'APOCALYPSE']


# In[58]:


# csv save
df.to_csv('rank.csv')


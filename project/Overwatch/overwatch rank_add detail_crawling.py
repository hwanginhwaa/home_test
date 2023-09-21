#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 크롤링
import requests
from bs4 import BeautifulSoup

# 데이터 분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import clear_output


# # 크롤링

# ## 리더보드 테이블

# In[2]:


# hyper parameter
minimum = 1
maximum = 250



data = []

def find_tag(tag, class1):
    result = tr.find(tag, class_=class1)
    if result != None:
        row.append(result.get_text())
    else: row.append(-1)
    
for page in range(minimum, maximum):

    url = 'https://overwatch.op.gg/leaderboards?platform=pc&role_id=0&page={}'.format(page)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text)

    # table tag
    table = soup.find('table', class_='LeaderBoardsTable')

    # tag
    for tr in table.find('tbody').find_all('tr', {'data-uid':True}):
        row = []
        # data base id
        row.append(tr['data-uid'])
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
    print("{} / {} page complete".format(page, maximum))
    clear_output(wait=True)
print("Mission complete")
df = pd.DataFrame(data)


# In[3]:


# header 이름 설정
df.columns = ['DBid', 'Rank', 'Platform', 'Nickname', 'K/D', 'Win_rate', 'Level', 'Kill/Death', 'Rating', 'Time_on_Fire', 
     'Win', 'Lose', 'Playtime', 'Most1', 'Most2', 'Most3']
df.head()


# In[4]:


df.info()


# In[5]:


df


# # 전처리

# ## 리더보드 테이블

# ### 변수 불필요한 문자열 제거

# In[6]:


# Rank
df['Rank'] = df['Rank'].str.replace(',', '')
df['Rank']


# In[7]:


# K/D 컬럼
df['K/D'] = df['K/D'].str.replace(': 1', '')
df['K/D']


# In[8]:


# Level
df['Level'] = df['Level'].str.replace('Lv.', '')
df['Level']


# In[9]:


# Kill/Death
df['Kill/Death'] = df['Kill/Death'].str.replace('\n', '')

# separate
new = df['Kill/Death'].str.split('/', expand=True)
df['Kill'] = new[0]
df['Death'] = new[1]

df[['Kill/Death', 'Kill', 'Death']]


# In[10]:


# rating
df['Rating'] = df['Rating'].str.replace('\n', '').str.strip()
df['Rating']


# In[11]:


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


# In[12]:


df['Time_on_Fire']


# In[13]:


# Win
df['Win'] = df['Win'].str.replace('W', '').str.strip()
df['Win']


# In[14]:


# Lose
df['Lose'] = df['Lose'].str.replace('L', '')
df['Lose']


# In[15]:


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


# In[16]:


df


# ### 데이터 형변환

# In[17]:


df.info()


# In[18]:


# float
df[['K/D', 'Kill', 'Death', 'Win', 'Lose', 'Playtime']] = df[['K/D', 'Kill', 'Death', 'Win', 'Lose', 'Playtime']].astype(float)
print(df[['K/D', 'Kill', 'Death', 'Win', 'Lose', 'Playtime']].dtypes)

# int
df[['Win_rate', 'Level', 'Rating', 'Rank']] = df[['Win_rate', 'Level', 'Rating', 'Rank']].astype(int)
print(df[['Win_rate', 'Level', 'Rating', 'Rank']].dtypes)


# In[19]:


df.info()


# In[20]:


# 불필요한 변수 삭제
del df['Kill/Death']
del df['Platform']


# In[21]:


# 컬럼 순서 바꾸기
df = pd.DataFrame(df, columns=['DBid', 'Rank', 'Nickname', 'Rating', 'Win', 'Lose', 'Win_rate', 'Kill', 'Death', 
                          'K/D', 'Time_on_Fire', 'Level', 'Playtime', 'Most1', 'Most2', 'Most3'])
df


# ### 변수 생성 

# In[22]:


# 티어 변수 생성
bins = [0, 1500, 2000, 2500, 3000, 3500, 4000, 5000]
labels = ['bronze', 'silver', 'gold', 'platinum', 'diamond', 'master', 'grand_master']
df['Tire'] = pd.cut(df['Rating'], bins, labels=labels)


# 상위 1위 ~ 500위는 순위 자체가 티어가 된다.
df['Tire'] = df['Tire'].astype(str)
df.loc[df['Rank'] <= 500, 'Tire'] = df.loc[df['Rank'] <= 500,'Rank'].astype(str)
df.iloc[490:510, :]


# In[24]:


# df.to_csv('rank.csv')
df


# ## 상세 테이블

# In[ ]:


# 종합 통계에서 필요한 라벨
stats = ['Damage dealt/Game', 'Healed/Game', 'Time Played', 
         'Time Played/Day', 'Time on fire', 'Avg Time on Fire', 'Avg Obj Time', 'Avg Obj Kills', 
         'Cards', 'Avg Medals/Game', 'Gold', 'Silver', 'Bronze']
data = {}
i = 0
for DBid in df['DBid']:
    url = 'https://overwatch.op.gg/detail/overview/{}'.format(DBid)
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text)
    
    
    # 종합 통계
    summary_stats = soup.find('div', class_='PlayerSideSummaryStats')
    # 가끔씩 프로필 비공개로 바꾸는 사람이 있기에 해당 DBid는 넘어가자
    if summary_stats == None:
        continue
    # DBid 추가
    if 'DBid' in data:
        data['DBid'].append(DBid)
    else:
        data['DBid'] = [DBid]
        
    # 종합 통계
    stat_list = summary_stats.find_all('li')[4:17] # 내가 확인해보고 싶은 리스트의 자리가 5번째 ~ 17번째에 있다.
    for stat in stat_list:
        b = stat.find('b').get_text() # lavel
        span = stat.find('span').get_text() # content
        
        if b in data:
            data[b].append(span)
        else:
            data[b] = [span]

    # 진행사항
    i += 1
    print(round(i/df['DBid'].count(),2))
    clear_output(wait=True)
print('Complete')


# In[ ]:


detail_df = pd.DataFrame(data)
detail_df
# data
# detail_df.to_csv('detail.csv')


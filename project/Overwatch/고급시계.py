#!/usr/bin/env python
# coding: utf-8

# In[124]:


# 크롤링
import requests
from bs4 import BeautifulSoup

# 데이터 분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # 크롤링

# In[125]:


url = 'https://overwatch.op.gg/heroes/global'
resp = requests.get(url)

resp.text


# In[126]:


soup = BeautifulSoup(resp.text)
soup


# In[127]:


# table tag
table = soup.find('table', class_='HeroesRank')


# In[128]:


# header tag
headers = []
for i in table.find('thead').find_all('th'):
    headers.append(i.get_text().strip())
headers


# In[129]:


data = []
for tr in table.find('tbody').find_all('tr'):
    row = []
    for span in tr.find_all('span'):
        row.append(span.get_text())
    data.append(row)
    
data


# # 크롤링 데이터를 데이터 프레임을 변환

# In[130]:


df = pd.DataFrame(data)
df.columns = pd.Series(headers[1:])
df


# # 전처리

# In[131]:


# 역할군 설정
role = {
    'Tanker': ['Reinhardt', 'Zarya', 'Sigma', 'Orisa', 'Roadhog', 'Wrecking Ball', 'D.Va', 'Winston'],
    'DPS': ['Genji', 'McCree', 'Hanzo', 'Reaper', 'Doomfist', 'Widowmaker', 'Tracer', 'Junkrat', 'Mei', 'Ashe', 'Soldier: 76',
           'Pharah', 'Torbjörn', 'Sombra', 'Bastion', 'Symmetra'],
    'Healer': ['Ana', 'Baptiste', 'Moira', 'Lúcio', 'Mercy', 'Zenyatta', 'Brigitte']
}


# In[132]:


# 각 역할군 영웅 개수
print("각 역할군 영웅 개수")
print('-'*50)
for key in role:
    print(key,"=", len(role[key]))


# In[133]:


np.where(df['Heroes'].isin(role['Tanker']), "Tanker", df['Heroes'])


# In[139]:


# 각 역할군을 변수로 만들자
df['role'] = pd.Series("") # 초기화
for key in role:
    df['role'] = np.where(df['Heroes'].isin(role[key]), key, df['role'])


# In[158]:


df.head()


# # 산술 통계를 위해 변수값 단위 제거

# In[150]:


df['Pick Rate'] = df['Pick Rate'].str.replace('%', '')
df['Pick Rate']


# In[163]:


df['Win Rate'] = df['Win Rate'].str.replace('%', '').str.strip()
df['Win Rate']


# In[159]:


# 1 min = 60 secs
df['Time on Fire'] = df['Time on Fire'].str.replace('1 min', '60 secs')
df['Time on Fire'] = df['Time on Fire'].str.replace('secs', '').str.strip()
df['Time on Fire']


# In[162]:


df['K/D'] = df['K/D'].str.replace(':1', '').str.strip()
df['K/D']


# ## 데이터 형변환

# In[191]:


df.info()


# In[194]:


cols = ['Pick Rate', 'Win Rate', 'Time on Fire', 'K/D']
for col in cols:
    df[col] = df[col].astype(float)


# In[196]:


df.info()


# In[195]:


df.head()


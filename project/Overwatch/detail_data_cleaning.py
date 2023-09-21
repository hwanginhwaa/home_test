#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 데이터 분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import clear_output


# # detail data 전처리

# In[4]:


# 데이터 불러오기
df = pd.read_csv('./data/detail.csv')
df


# In[6]:


# 불필요한 변수 삭제
del df['Unnamed: 0']


# In[7]:


df.info()


# In[8]:


df.head()


# In[16]:


df.loc[1:4, 'DBid']
df.iloc[1:4, 3:4]


# In[9]:


# Damaage dealt/Game & Healed/Game 변수  


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


s = pd.Series([1,2,3], [3,4,5])


# In[3]:


np.array([1,2,3])


# In[5]:


s.index


# In[7]:


s.values


# In[8]:


s = pd.Series([1, 2, 3, 1, 2, 2, 1, 2, 3, 3, 4, 4, 4, 5, 6, np.NaN])
s


# In[9]:


s.sum()


# In[10]:


s.size


# In[11]:


len(s)


# In[13]:


s.count()


# In[15]:


s.value_counts()


# In[19]:


# multi- index
s[[1,3,4]]


# In[20]:


s = pd.Series(np.arange(10), np.arange(10)+1)
s


# In[21]:


s >= 7


# In[24]:


s[11] = 1100


# In[28]:


s.drop(11, inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





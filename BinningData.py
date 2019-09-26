#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


# create a bin
bins = [0, 80, 100]
# create a status 
status_name = ['Fail', 'Pass']


# In[7]:


df['status'] = pd.cut(df['grade'], bins, labels=status_name)
df


# In[8]:


pd.value_counts(df['status'])


# In[ ]:





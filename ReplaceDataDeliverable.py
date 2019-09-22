#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [70,-2,77,78,101]


# In[5]:


GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df


# In[6]:


df.loc[(df['Grades'] < 0,'Grades')] = 0


# In[7]:


df


# In[ ]:





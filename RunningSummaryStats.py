#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0]


# In[2]:


# create a dataframe that we can run summary stats on 


# In[4]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
 #dataframe name 
df = pd.DataFrame(data = GradeList, columns=('Names', 'Grades', 'BS', 'MS', 'PhD'))
df


# In[5]:


df.count()


# In[6]:


df.mean()


# In[7]:


df.std


# In[8]:


df.min()


# In[9]:


df.max()


# In[11]:


df.quantile(.25) #highest value in the lowest 25% of data


# In[12]:


df.quantile(.5) #highest value in the lowest 50% of data


# In[14]:


df.quantile(.75) #highest value in the lowest 75% of data


# In[ ]:





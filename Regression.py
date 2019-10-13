#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[4]:


def genderToNumber(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0


# In[5]:


df['gender_val'] = df['gender'].apply(genderToNumber)
df.tail()


# In[9]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()


# In[11]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender_val', data=df).fit()
result.summary()


# In[12]:


# r squared is 66% which is not good and I elminated age because of the high pvalue. 


# In[13]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours', data=df).fit()
result.summary()


# In[14]:


# adding gender did not affect the rsquared


# In[ ]:





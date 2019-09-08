#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "datasets/CRM01.xls"
df = pd.read_excel(Location, headers=None)

df.head()


# In[6]:


# df.columns = ['State & Cities', 'Crime data'];
# this is changing the column names, however there are 42 elements that would need to changed so code would not run unless I completed all 42


# In[ ]:





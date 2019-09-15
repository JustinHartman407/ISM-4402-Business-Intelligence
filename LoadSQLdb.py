#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine


# In[2]:


# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))


# In[3]:


sql = "select name from sqlite_master where type = 'table';"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df
# this is a query that we ran to see what is the name of the table in the database


# In[4]:


sql = "select * from scores;"
scores_df = pd.read_sql(sql, engine)
scores_df.head()
# this is a query that was ran to show the results from scores and the table that is a associated. 


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import requests


# In[12]:


simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")


# In[14]:


len(simpsons)


# In[23]:


simpsons[3]


# # Web Scraping

# using  https://www.football-data.co.uk/data.php
#  extracting csv file from websites
# 

# In[32]:


# reading 1 csv file from website
df_championship26 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2627/E1.csv")


# In[35]:


# showing dataframe
df_championship26.head()


# In[39]:


# columns renaming
df_championship26.rename(columns = {'FTHG' : 'home_goals',
                                    'FTAG' : 'away_goals'},inplace = True)


# In[41]:


# view updated dataframe
df_championship26.head()


# ## Extracting tables from pdfs

# In[52]:


get_ipython().run_line_magic('pip', 'install camelot-py')


# In[53]:


import camelot


# In[ ]:


camelot.read_pdf('foo.pdf')


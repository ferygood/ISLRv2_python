#!/usr/bin/env python
# coding: utf-8

# # Applied  
# **Q8.** This exercise relates to the "College" data set. 
# a. Load College.csv data

# In[1]:


import os
import pandas as pd

os.chdir("/home/yaochung41/github/ISLRv2_python/notebook/")


# In[2]:


college = pd.read_csv("data/College.csv")
college.head()


#!/usr/bin/env python
# coding: utf-8

# # Applied  
# This section we will go through the applied exercise part. Contents are related to *p.66* in the [ISLRv2 book](https://hastie.su.domains/ISLR2/ISLRv2_website.pdf)  
# <br/>
# **Q8.** This exercise relates to the "College" data set, which can be found in the file `College.csv` on the book [website](https://www.statlearning.com/resources-second-edition). It contains a number of variables for 777 different universities and colleges in the US. 
# a. Load College.csv data

# In[1]:


import os
import pandas as pd

os.chdir("/home/yaochung41/github/ISLRv2_python/notebook/")


# (a) Called the load data `College.csv`

# In[2]:


college = pd.read_csv("data/College.csv")
college.head()


# (b) Make the row names of the data to college names and then remove the first column. Using pandas, we can first rename the column including college name to `college` and use it as index value.

# In[3]:


college.rename(columns={'Unnamed: 0': 'college'}, inplace=True)
college.set_index('college', inplace=True)
college.head()


# (c) i. Produce a numerical summary of all the variables in the data

# In[4]:


college.describe()


# (c) ii. Produce a scatterplot matrix of the first ten columns or variable of the data. To create a scatterplot matrix, we import `seaborn` library.

# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='ticks')


# In[6]:


sns.pairplot(college.iloc[:, 0:10])


# (c) iii. Produce side-by-side boxplot of `Outstate` versus `Private`

# In[7]:


ax = sns.boxplot(x='Private', y='Outstate', hue="Private", data=college).set(title="Private vs. Outstate")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()


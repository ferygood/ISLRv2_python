#!/usr/bin/env python
# coding: utf-8

# # Applied  
# This section we will go through the applied exercise part. Contents are related to *p.66* in the [ISLRv2 book](https://hastie.su.domains/ISLR2/ISLRv2_website.pdf)  
# <br/>
# ## Q8. 
# This exercise relates to the "College" data set, which can be found in the file `College.csv` on the book [website](https://www.statlearning.com/resources-second-edition). It contains a number of variables for 777 different universities and colleges in the US. 
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
plt.clf()


# (c) iv. Create a new qualitative variable, called `Elite`, by binning the `Top10perc` variable. We are going to divide universities into two groups based on whether or not the proportion of students coming from the top 10% of their high school classes exceeds 50%.

# In[8]:


# 1 create a Elite list and set it as no first
college['Elite'] = 'no'

# 2 if Top10perc is larger than 50, change Elite to yes
college.loc[college['Top10perc'] > 50, 'Elite'] = 'yes'
college.describe(include='all')


# Find out how many elite universities there are. Also produce a side-by-side boxplots of `Outstate` versus `Elite`.

# In[9]:


# elite univerisities
elite_count = college[college['Elite']=='yes'].shape[0]
print("There are %s elite universities." % (elite_count))

# side-by-side boxplot
ax1 = sns.boxplot(x='Elite', y='Outstate', hue="Elite", data=college).set(title="Elite vs. Outstate")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()


# (c) v. Produce histograms with differing numbers of bins for a few of the quantitative variables. Try to divide the print window to certain regions so that plots can be made simultaneously. 
# vi. Continue exploring the data, and provide a brief summary of what you discover (to-do)

# Below we first explore `PhD` feature. This feature is the percent of faculty with Ph.D.'s. As you can see in the histogram, this feature appears a left-skewed distribution and the largest number of faculty to have Ph.D. degree is over a hundred. 

# In[10]:


fig, axs = plt.subplots(2, 2, figsize=(7, 7))

sns.histplot(college, x="PhD", kde=True, color="skyblue", binwidth=5, ax=axs[0, 0])
sns.histplot(college, x="PhD", kde=True, color="olive", binwidth=10, ax=axs[0, 1])
sns.histplot(college, x="PhD", kde=True, color="purple", binwidth=15, ax=axs[1, 0])
sns.histplot(college, x="PhD", kde=True, color="red", binwidth=20, ax=axs[1, 1])

plt.show()


# Next, we give another example on feature `Personal`. This feature shows the information of estimated personal spending in our data. As you can see in these figure, the estimated spending has a right-skewed (positive skew) distribution.

# In[11]:


fig, axs = plt.subplots(1, 4, figsize=(28, 7))

sns.histplot(college, x="Personal", kde=True, color="skyblue", binwidth=100, ax=axs[0])
sns.histplot(college, x="Personal", kde=True, color="olive", binwidth=500, ax=axs[1])
sns.histplot(college, x="Personal", kde=True, color="purple", binwidth=1000, ax=axs[2])
sns.histplot(college, x="Personal", kde=True, color="red", binwidth=2000, ax=axs[3])

plt.show()


# ## Q9 
# 
# This exercise involves the Auto data set. Make sure that the missing values have been removed from the data.  
#   
# ### (a) Which of the predictors are quantitative, and which are qualitative?

# In[12]:


auto = pd.read_csv("data/Auto.csv")
auto.dropna(inplace=True)
print(auto.dtypes)
print(auto.shape)


# So, basically we have 397 rows and 9 columns in our Auto data. Among 9 features, mpg, cylinders, displacement, weight, acceleration, year, and origin are quantitative. Horsepower and name are qualitative.
# <br/>
# ### (b) What is the range of each quantitative predictor?

# In[13]:


auto.describe(include='all')


# You can now see the range of each quantitative predictors from the dataframe above. For example, the range of `mpg` is from 9 to 46, and the range of `cylinders` is from 3 to 8 respectively.

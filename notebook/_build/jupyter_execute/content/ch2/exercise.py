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
print(auto.dtypes)
print(auto.shape)


# In[13]:


import numpy as np

# we found that there are question mark in the dataframe
auto = auto.replace("?", np.nan)
auto['horsepower'] = pd.to_numeric(auto['horsepower'])
auto.dropna(inplace=True)
print(auto.shape)
print(auto.dtypes)


# So, basically we have 392 rows and 9 columns in our Auto data. Among 9 features, mpg, cylinders, displacement, weight, acceleration, year, and origin are quantitative. Horsepower and name are qualitative.
# <br/>
# ### (b) What is the range of each quantitative predictor?

# In[14]:


auto.describe(include='all')


# You can now see the range of each quantitative predictors from the dataframe above. For example, the range of `mpg` is from 9 to 46, and the range of `cylinders` is from 3 to 8 respectively.  
#   
# ## (c) What is the *mean* and *standard deviation* of each quantitative predictor?  
# We can look up the previous output dataframe again. For example, `mpg` has a mean value 23.515869 and standard deviation as 7.825804.  
#   
# ## (d) Now remove the 10th through 85th observations. What is the range, mean, and standard deviation of each predictor in the subset of the data that remains?

# In[15]:


auto_subset = auto.drop(auto.index[9:85])
print(auto_subset.index)
auto_subset.describe(include='all')


# We can use `.drop` attributes in pandas to drop rows by index number. Remember python index starts from 0, and not include the the suffix. Therefore, we need to set the rows we want to remove as `[9:85]`. Then we can look up the answer, for example, `mpg` now has 24.438629 as mean and 7.908184 as standard deviation.  
#   
# ## (e) Using the full data set, investigate the predictors graphically, using scatterplots or other tools of your choice. Create some plots highligting the relationships among the predictors. Comment on your findings.

# In[16]:


sns.pairplot(auto, corner=True)


# We first use a pair-scatterplot to visualize the relationship of one-to-one predictors. These observation can show that quantitative variables has a trend of positive correlation such as `displacement` and `weight`, `mpg` and `acceleration`, `displacement` and `horsepower`. Other varibales has negative correlation such as `mpg` and `weight`, `weight` and `accelearation`, `mpg` and `horsepower`.  
#   
# ## (f) Suppose that we wish to predict gas mileage (mpg) on the basis of the other variables. Do your plots suggest that any of the other variables might be useful in predicting mpg? Justify your answer.  
#   
# From the pairplot above, we can have a first insight that quantitative predictors will be useful to predict mpg since we have seen some trends. To justify we can calculate their correlations.

# In[17]:


import numpy as np

# compute correlation matrix
corr = auto.corr()

# generate a mask for hte upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# set up matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom divergin colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, square=True, linewidths=.5, cbar_kws={"shrink": .8}, annot=True)


# We can see from above that `weight`, `displacement`, `horsepower` and `cyclinders` have strong negative correlation coefficients (approx. lower than -0.8). Therefore, we can consider to use these three predictors to predict mpg from the Auto dataset.

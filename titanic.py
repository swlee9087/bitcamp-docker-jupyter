#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


this = pd.read_csv("data/train.csv")


# In[6]:


f, ax = plt.subplots(1, 2, figsize=(18, 8))  # f=line, ax=col
series = this['Survived'].value_counts()  # ret data will print in col type = df->series
"""print(type(series))
print(series)"""
series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('0.dead VS 1.alive')
ax[0].set_ylabel('')
ax[1].set_title('0.dead VS 1.alive')
sns.countplot('Survived', data=this, ax=ax[1])
plt.show()


# In[7]:


this['pop Survived'] = this['Survived'].replace(0, 'dead').replace(1, 'alive')
this['Seat Class'] = this['Pclass'].replace(1, 'First').replace(2, 'Second').replace(3, 'Third')
sns.countplot(data=this, x='Seat Class', hue='pop Survived')


# In[8]:


this['pop Survived'] = this['Survived'].replace(0, 'dead').replace(1, 'alive')
this['Port'] = this['Embarked'].replace('C', 'Chellbourg').replace('S', 'Sth Hampton').replace('Q', 'Queenstown')
sns.countplot(data=this, x='Port', hue='pop Survived')


# In[9]:


f, ax = plt.subplots(1, 2, figsize=(18, 8))
male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Male Survival Rate 0.dead VS 1.alive')
ax[0].set_ylabel('')
ax[1].set_title('Female Survival Rate 0.dead VS 1.alive')


# In[ ]:





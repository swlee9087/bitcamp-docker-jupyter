#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import matplotlib.pyplot as plt
import numpy as np


# In[9]:


data: [] = list()
data = csv.reader(open('data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))


# In[10]:


arr = []
[arr.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print([i for i in arr])


# In[11]:


plt.style.use('ggplot')
plt.plot(arr)


# In[ ]:





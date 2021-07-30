#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[26]:


data: [] = list()
home: [] = list()
away: object = None
result_name: str = ''


# In[27]:


#df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands=',', index_col=0)
#df.to_csv('./data/202106_202106_연령별인구현황_월간_wo_comma.csv', sep=',', na_rep='NaN')
data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_wo_comma.csv', 'rt', encoding='UTF-8'))
next(data)
data = list(data)


# In[28]:


arr = []
[arr.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print([i for i in arr])


# In[29]:


plt.style.use('ggplot')
plt.plot(arr)


# In[30]:


home = []
[home.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print(home)


# In[31]:


plt.title('Pildong pop')
plt.plot(arr)


# In[54]:


home = []  # 정의되었던 self.home 을 local variable home 으로 변경해야
for i in data:
    if '필동' in i[0]:
        home = np.array(i[3:], dtype=int)/int(i[2])
        
away = []        
result = 0
mn = 1  # 최소값
for i in data:
    away = np.array(i[3:], dtype=int)/int(i[2])
    s = np.sum((home-away)**2)
    if s < mn and '필동' not in i[0]:  # s < 1
        mn = s
        result_name = i[0]
        result = away


# In[55]:


plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.title('Area with similar pop size as Pildong')
plt.plot(home, label='Pildong')
plt.plot(away, label='Similar Area')
plt.legend()


# In[ ]:





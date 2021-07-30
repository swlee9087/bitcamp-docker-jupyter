#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv

from matplotlib import pyplot as plt


# In[36]:


data = csv.reader(open('./data/unit05_seoul.csv', 'rt', encoding='UTF-8'))
next(data)


# In[37]:


ls = list(data)


# In[38]:


print([i for i in ls])


# In[64]:


[i[-1] for i in ls]  # show max temp


# In[65]:


[i[-2] for i in ls] 


# In[67]:


max_temps = []
min_temps = []
[max_temps.append(float(i[-1])) for i in ls if i[-1] != '']
[min_temps.append(float(i[-2])) for i in ls if i[-2] != '']
print(f'max temps: total {len(max_temps)} records. \nmin temps: total {len(min_temps)} records. ')


# In[69]:


plt.title('Temp changes on my birthday')
plt.plot(max_temps, 'r', label='max temp')
plt.plot(min_temps, 'b', label='min temp')
plt.legend()
plt.show()


# In[70]:


high = []
low = []
for i in ls:
    if i[-1] != '' and i[-2] != '':
        if 1990 <= int(i[0].split('-')[0]):
            if i[0].split('-')[1] == '08' and i[0].split('-')[2] == '07':
                high.append(float(i[-1]))
                low.append(float(i[-2]))


# In[71]:


plt.rcParams['axes.unicode_minus'] = False
plt.title('Temp changes on my birthdays')
plt.plot(high, 'pink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show() 


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[133]:


import csv
import random
from matplotlib import pyplot as plt


# In[134]:


data = csv.reader(open('./data/unit05_seoul.csv', 'rt', encoding='UTF-8'))
next(data)


# In[135]:


ls = list(data)


# In[136]:


print([i for i in ls])


# In[137]:


[i[-1] for i in ls]  # show max temp


# In[138]:


[i[-2] for i in ls]   # show min temp


# In[139]:


max_temps = []
min_temps = []
[max_temps.append(float(i[-1])) for i in ls if i[-1] != '']
[min_temps.append(float(i[-2])) for i in ls if i[-2] != '']
print(f'max temps: total {len(max_temps)} records. \nmin temps: total {len(min_temps)} records. ')


# In[140]:


plt.title('Temp changes on my birthdays')
plt.plot(max_temps, 'r', label='max temp')
plt.plot(min_temps, 'b', label='min temp')
plt.legend()
plt.show()


# In[141]:


high = []
low = []
for i in ls:
    if i[-1] != '' and i[-2] != '':
        if 1990 <= int(i[0].split('-')[0]):
            if i[0].split('-')[1] == '08' and i[0].split('-')[2] == '07':
                high.append(float(i[-1]))
                low.append(float(i[-2]))


# In[142]:


plt.rcParams['axes.unicode_minus'] = False
plt.title('Temp changes on my birthdays')
plt.plot(high, 'orange', label='high')
plt.plot(low, 'g', label='low')
plt.legend()
plt.show() 


# In[143]:


arr = []
[arr.append(random.randint(1, 1000))for i in range(13)]
plt.boxplot(arr)
plt.show()


# In[145]:


month = [[], [], [], [], [], [], [], [], [], [], [], []]
# for i in arr:
#     if i[-1] != '':
#         month[int(i[0].split('-')[1])-1].append(float(i[-1]))
[month[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in ls if i[-1] != '']
plt.boxplot(month)
plt.show()


# In[144]:


day = []
[day.append([]) for i in range(31)]
[day[int(i[0].split('-')[2]) - 1].append(float(i[-1]))
 for i in ls
     if i[-1] != ''
         and i[0].split('-')[1] == month]

#    [day.append(float(j[-1]) for i in arr if j[-1] != '' and j[0].split('-')[1] == '08' and int(j[0].split('-')[2]) - 1]
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()


# In[130]:


aug=[]
dec=[]

for i in ls:
    month=i[0].split('-')[1]
    if i[-1] !='':
        if month =='08':
            aug.append(float(i[-1]))
        if month =='12':
            dec.append(float(i[-1]))
plt.title('Temp records in Aug and Dec')
plt.hist(aug, bins=100, color='orange', label='Aug')
plt.hist(dec, bins=100, color='green', label='Dec')
plt.legend()
plt.show()


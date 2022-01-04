#!/usr/bin/env python
# coding: utf-8

# In[79]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[81]:


df = pd.read_csv("2021 in data sleptenough.csv")


# In[102]:


#prepping grades column for bar graph
#grades = list(abs(df.loc[:,"Grade"]))

#Selecting grades where I slept enough
sleepgrades = list(abs(df.loc[(df["SleptEnough"]==1), "Grade"]))

#Selecting grades where I did not sleep enough
nosleepgrades = list(abs(df.loc[(df["SleptEnough"]==0), "Grade"]))


# In[151]:


#Creating bar graph

labels = ['Horrible', 'Bad', 'Not good', 'OK', 'Good', 'Very good', 'Amazing']

#Getting counts of grades where I slept enough
sleepgrades_count = []
for i in range(7):
    sleepgrades_count.append(sleepgrades.count(i +1)) 

#Counts of grades where I didn't sleep enough
nosleepgrades_count = []
for i in range(7):
    nosleepgrades_count.append(nosleepgrades.count(i+1))
    
x = np.arange(len(labels)) +1
width = 0.35

fig, ax = plt.subplots(figsize=(15,8))
rects1 = ax.bar(x - width/2, sleepgrades_count, width, label='Rested', color='Blue')
rects2 = ax.bar(x + width/2, nosleepgrades_count, width, label='Tired', color='Red')

ax.set_ylabel('Day Count')
ax.set_title('Day grade based on sleep')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.xticks(rotation=45)
ax.legend(fontsize = 14)

plt.show()


# In[153]:


#Saving plot
fig.savefig("sleepgrade_bar.jpeg", bbox_inches='tight',pad_inches=.5)


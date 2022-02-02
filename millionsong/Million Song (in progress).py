#!/usr/bin/env python
# coding: utf-8

# In[122]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import math
from numpy import nan
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
from collections import Counter


# In[98]:


df = pd.read_csv("E:\\Data Projects\\Million Song\\music.csv")


# In[99]:


df.head()


# In[160]:


df.info()


# In[103]:


df = df.rename(columns={'artist.hotttnesss' : 'artist_hotness', 'artist.id' : 'artist_id', 'artist.name':'artist_name', 'song.hotttnesss' : 'song_hotness'})
#df.head()


# In[104]:


#seeing how many unique artists there are
artists = df['artist_id']
df_set = set(df['artist_id'])
unique_artists = len(df_set)
print(unique_artists)


# In[105]:


#finding top artists
top_artists_list = Counter(df.loc[:,'artist_id']).most_common(20)

colnames = df.columns.values.tolist()
    
top_artists_df = pd.DataFrame(columns = colnames)

for i in top_artists_list:
    #print(i[0])
    #print(df.loc[df['artist_id'] == i[0]])
    top_artists_df = top_artists_df.append(df.loc[df['artist_id'] == i[0]])
    
top_artists_df.head()


# In[106]:


top_artists_count = list(top_artists_df['artist_id'].value_counts())
print(top_artists_count)

top_artists_ids = list(top_artists_df.artist_id.unique())
print(top_artists_ids)


# In[107]:


#top_hist = pd.DataFrame(columns = ("artist_name", "count"))
#top_hist["count"] = top_artists_count
#top_hist


# In[108]:


#top_hist["artist_name"] = list(top_artists_df.artist_id.unique())

#top_hist


# In[109]:


#top_artists_names = []
#top_artists_names = list(top_artists_names)

#for x in top_hist['artist_name']:
#    val = df['artist_name'].loc[df['artist_id']==x]
    
#top_artists_names.append(val)


# In[110]:


#top_artists_names = pd.DataFrame()
#for x in top_hist['artist_name']:
#    val = df['artist_name'].loc[df['artist_id']==x]
    
#top_artists_names.head()


# In[111]:


#top_artists_df['artist_id'].value_counts().plot.bar(x='Artist Id', y='Song Count')


# In[112]:


ax = df['artist_id'].value_counts().plot(kind='hist', figsize=(10,10), title=("Artists' Song Counts"))
ax.set_xlim(0,15)
ax.set_xlabel("Number of Songs", fontsize=12, color='red')
ax.title.set_size(24)
ax.set_ylabel("Number of Artists", fontsize=12, color='red')
ax.grid(axis='y', alpha=(0.75))


# In[116]:


#Creating dataframe that contains only values that have song hotness
df_sh = pd.DataFrame()


# In[150]:


#for x,y in df.iterrows(): 
    #if df['hotness'][x] == float and df['hotness'][x]==0.0:
    #if df['song_hotness'][x]!=0.0 and math.isnan(df['song_hotness'][x]) != True :
        #print(df['song_hotness'][x], ' ',df['artist_name'][x])


# In[185]:


#Dropping everything where song hotness = 0 or the value is NaN
df_sh = df.drop(df[(df.song_hotness == 0.0)].index)
df_sh = df_sh[df_sh['song_hotness'].notna()]
#df_sh.info()


# Song Hotness Analysis

# In[186]:


for x,y in df_sh.iterrows(): 
    #if df['hotness'][x] == float and df['hotness'][x]==0.0:
    #if df_sh['song_hotness'][x]!= 0.0 and math.isnan(df_sh['song_hotness'][x]) == False :
        print(df_sh['song_hotness'][x], ' ',df_sh['artist_name'][x])


# In[210]:


#Viewing correlation matrix
df_sh.corr()


# In[178]:


#Training vs. Testing
training = df_sh.sample(frac=0.8, random_state=25)
testing = df_sh.drop(training.index)


# In[208]:


fig=plt.figure()
ax=fig.add_axes([0,0,2,2])
ax.set_xlabel("Loudness")
ax.scatter(df_sh['loudness'], df_sh['song_hotness'], label="Loudness")

plt.show()


# In[ ]:





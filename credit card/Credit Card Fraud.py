#!/usr/bin/env python
# coding: utf-8

# In[78]:


#Initializing

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os, psutil

process = psutil.Process(os.getpid())


# In[79]:


#Application data - read  csv
appdata = pd.read_csv("application_data.csv")
appdata.head()


# In[80]:


#prevappdata = pd.read_csv("previous_application.csv")
#prevappdata.head()


# In[81]:


appdata.info()


# In[82]:


print(process.memory_info().rss)


# In[83]:


#appdata.dtypes

# -- SAVED CODE FOR MAPPING BOOLEAN VALUES

#s = {'Y': True, 'N': False}

#appdata['FLAG_OWN_CAR']=appdata['FLAG_OWN_CAR'].map(s)


# In[84]:


def redmem(df): 
    
    for col in df.columns:
        coltype = df[col].dtype
        
        if coltype != object: 
            cmin = df[col].min()
            cmax = df[col].max()
            
            if str(coltype)[:3] == 'int':
                if cmin > np.iinfo(np.int8).min and cmax < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif cmin > np.iinfo(np.int16).min and cmax < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif cmin > np.iinfo(np.int32).min and cmax < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif cmin > np.iinfo(np.int64).min and cmax < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            
            else: 
                if cmin > np.finfo(np.float16).min and cmax < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif cmin > np.finfo(np.float32).min and cmax < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                elif cmin > np.finfo(np.float64).min and cmax < np.finfo(np.float64).max:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('object')


# In[89]:


#run reducing memory
redmem(appdata)
#appdata.info()


# In[90]:


s = {'Y': 1, 'N': 0, 'NaN': -1}

appdata['FLAG_OWN_CAR']=appdata['FLAG_OWN_CAR'].map(s)
appdata['FLAG_OWN_REALTY']=appdata['FLAG_OWN_REALTY'].map(s)


# In[91]:


appdata.head()


# In[ ]:





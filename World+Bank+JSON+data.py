
# coding: utf-8

# In[200]:


import os
from pandas.io.json import json_normalize
import pandas as pd
import json


# In[51]:


with open('/Users/alizadmehr/Documents/data_wrangling_json/data/world_bank_projects.json', 'r') as json_file:
      data = pd.read_json(json_file) 


# In[58]:


data.columns


# In[100]:


dataQ1 = data[['countryname','project_name']].groupby('countryname').agg('count')


# In[107]:


dataQ1Sorted = dataQ1.sort_values('project_name', ascending=False, inplace=False)


# In[109]:


dataQ1Sorted.head(10)


# In[204]:


#dataQ2  = data[['_id','mjtheme_namecode']]
json_normalize(data, 'mjtheme_namecode')


# In[197]:





# In[187]:


dataQ2['mjtheme_namecode'].array


# In[181]:


flatten(dataQ2)


# In[154]:


print(dataQ2['mjtheme_namecode'].head())


# In[159]:


json_normalize(data['mjtheme_namecode'])


# In[157]:


for key , value in dataQ2['mjtheme_namecode']:
    print (key,value)


# In[205]:


data['mjtheme_namecode'].value_counts
#data[['_id','mjtheme_namecode']]

#json_normalize(dataQ2)

mjTheme = json_normalize(data=dataQ2, record_path='mjtheme_namecode', 
                            meta=['_id'])


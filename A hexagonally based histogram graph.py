#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt 
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import seaborn as sns 
plt.style.use('classic') 
plt.style.use('seaborn-whitegrid') 
# Create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
# Plot the data with seaborn

for col in 'xy': 
    sns.kdeplot(data[col], shade=True)
    sns.kdeplot(data);
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde');
with sns.axes_style('white'): 
    sns.jointplot("x", "y", data, kind='hex')


# In[ ]:





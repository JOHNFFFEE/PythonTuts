
# coding: utf-8

# # Newsvendor model with normal distribution

# In[14]:


#import libraries
import pandas as pd
import numpy as np
import scipy.stats as st


# Cu – variable cost. This cost type expresses the production cost of one product 
# Co -fixed cost. This cost always exists when the production of a series is started.

# D – a random variable with cumulative distribution function F representing uncertain customer demand.
# Q - the product quantity in the inventory.

# In[28]:


Cu = np.random.randint(10,15)


# In[29]:


Co = np.random.randint(1,10)


# FQ - unpropability of unsatisfied orders  NFQ - propability of unsatisfied orders 

# In[39]:


FQ= Cu/(Cu+Co)


# In[55]:


NFQ= 1-FQ


# In[56]:


#for instance let's take a normal distribution
z=st.norm.ppf(FQ)


# In[57]:


z1=st.norm.ppf(NFQ)


# S - standard deviation (here 30), M-mean demand  (here 500)

# In[43]:


#for example  
S=30
M=500


# In[59]:


Q=z*S+M


# In[60]:


Q1=z1*S+M


# In[54]:


print('Optimal Qty {}'.format(Q))


# In[62]:


print('Non Optimal Qty {}'.format(Q1))


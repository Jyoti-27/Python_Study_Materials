#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


l1 = [1,2,3,4,5,6,7]
l1


# In[3]:


s = pd.Series(l1)
s


# In[4]:


series = pd.Series([0.2, 0.5, 0.75, 1.6])
print("Pandas Series:\n", series)


# In[5]:


s.values


# In[6]:


print("Series.values: ",series.values)
print("Data type of Series: ", type(series.values))
print("Type of series: ", type(series))
print("Index of Series: ", series.index)


# In[7]:


s = pd.Series([10,20,30])

type(s)


# In[8]:


type(s.values)


# In[9]:


type(s.index)


# In[10]:


s = pd.Series([5,4,3],  index=[100, 200, 300])


# In[11]:


print("Series.values: ",s.values)
print("Data type of Series: ", type(s.values))
print("Type of series: ", type(s))
print("Index of Series: ", s.index)


# In[12]:


l = [4,5,6]
l


# In[13]:


print("List values: ",l.values)


# In[14]:


print("Data type of List: ", type(l.values))


# In[15]:


print("Type of List: ", type(l))


# In[16]:


print("Index of List: ", l.index)


# In[17]:


List=[20, 15, 42, 33, 94, 8, 5]
print("List is: " , List)
ser_list=pd.Series(List)
print("Series from List: \n",ser_list)


# In[18]:


print("Explicit Indexing: \n",pd.Series(List, index = ['i','ii','iii','iv','v','vi','vii']))


# In[19]:


order=[1,2,3,4,5,6,7]
ser_ord=pd.Series(List,index=order)
print("Ordered series: \n",ser_ord)


# In[20]:


ser_ord[1] = 21


# In[21]:


ser_ord


# In[ ]:





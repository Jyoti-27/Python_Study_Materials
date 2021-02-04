#!/usr/bin/env python
# coding: utf-8

# # Tuple
# Tuple is a collection which is ordered and unchangeable.
# They are written within round brackets.
# Tuple can store hetrogeneous data types.

# In[14]:


#how to make a tuple

tuple1=('I','am','a','tuple')  #by using round brackets
print('Tuple1: ',tuple1)

tuple2=tuple(('I','am','a','tuple'))  #by using tuple() method
print('Tuple2: ',tuple2)


# In[7]:


#joining two tuples
tup =(1,2,3)
print(tup)
tup1 = (1,2,3) + (3,4,22,9,0,56)
print(tup1)


# In[10]:


#accessing elements of tuple
print(tup[1])
print(tup1[6])


# In[12]:


#accessing elements of tuple using negative indexing
print(tup1[-3])
print(tup1[-8])


# In[15]:


#accessing range of indexes
print(tup1[3:])   #this will give elements from third index till the end
print(tup1[:4])   #this will give elements from the beginning till 3rd index
print(tup1[2:7:2]) #this will give elements from 2 to 6 index with sep size of 2


# In[24]:


#accessing range of indexes using negative indexing
print('Tuple :',tup1)
print(tup1[-8:-2])
print(tup1[-9:-5:2])


# In[36]:


# accessing the elemets from nested tuple
tuple_1 = ("Data", [100, 'Science', 200], (150, 90, 'Study'))
print('Tuple :',tuple_1)

print(tuple_1[1][1])  #retrieving 'Science'
print(tuple_1[1][0])  #retrieving 100
print(tuple_1[2][1])  #retrieving 90


# In[6]:


#this will give us an error as we cannot change any element in th tuple
tup[1]=10


# In[3]:


#type method
tup=(1,2,34)
print(type(tup))


# 
# 
# #### Can we create an empty tuple? Yes

# In[4]:


#creating an empty tuple
tuple1=()
print(tuple1)
#adding elements in the empty tuple
a=10,20,30,40
tuple1=a
print(tuple1)


# In[ ]:


#deleting tuple
del tuple1
tuple1


# #### What will happen if we create a tuple only with one element ?

# In[25]:


#Python will consider it as a string
course=('Data science')
print(course)
print(type(course))


# In[26]:


#this is how we can create a tuple with one element
course=('Data science',)    #by adding comma 
print(course)
print(type(course))


# #### How can we change a tuple if they are immutable ?

# In[38]:


#we can change anything in tuple by converting it into list
names=('Shreya','Jay','Diya','Priya')
print('Names tuple :',names)
names1=list(names)
print('Names list :',names1)

#changing an element
names1[2]='Reema'

print('Modified Names :',names1)


# In[29]:


#to check whether an item exists in tuple
tuple2=('Delhi','Mumbai','Chennai')
print(tuple2)
'Chennai' in tuple2


# In[31]:


#count method - this will check the count of the given element
print(tuple2.count('Mumbai'))
print(tup1.count(3))


# In[33]:


#index method
print(tuple2.index('Chennai'))
print(tup1.count(3))   #this will give the index of the first occurance of element


# In[ ]:





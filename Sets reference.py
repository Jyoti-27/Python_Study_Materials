#!/usr/bin/env python
# coding: utf-8

# # Sets
# - are unordered collection of unique elements
# - by default sorted
# - iterable
# - mutable
# - Normal set operations, i.e., union, intersection, etc.
# - Checking presence of particular element - optimized
# - Syntax : variable_name = set([a list of elements])

# ## Creation of Sets

# ##### using curly braces { }

# In[1]:


set_ = {11,22,33}
print('Set is : ', set_)
print('Type: ',type(set_))


# ##### using list

# In[2]:


_set = set([1,2,3,4])
print('Set is : ', _set)
print('Type: ',type(_set))


# ### Lists vs Sets

# In[3]:


l1 = [1,2,2,4,6,5,6,1,3,8,0,0,9, 'apple', 'Axe', 'ball','apple']
print('List is : ', l1, '\nType : ',type(l1))
print('Accessing list element, l1[5]: ', l1[5])

#duplicates are not considered in the set unlike lists
s1 = set(l1)
print('\nSet is : ', s1, '\nType : ',type(s1))
#print("Accessing set element, s1[5]: ,'s1[5])


# ###  Mutability of sets

# In[6]:


#sets are mutable

s={22,78,0,22,7,34}
print('Set : ', s )

s.add('a')
print('After adding an element : ', s )

s.update([4,5,6])
print('After updating elements : ', s )


# In[17]:


#removing elements from set
s.remove('a')
print("Set after removing:",s)


# ### Immutable sets - frozenset( )

# In[7]:


fs = frozenset([1,2,3,4])
fs


# In[8]:


#this will give error as frozen sets are immutable - they are used rarely
fs1 = fs.add('a')


# ### Set Operations

# In[9]:


set_A = set([11, 3, 'doll', 52, 36, 'apple'])
set_B = set([23, 44, 36, 'doll', 11, 'brain'])
print("Set A : ", set_A)
print("Set A : ", set_B)


# In[10]:


print('Union of sets: ', set_A.union(set_B))
print('Intersection of sets: ', set_A.intersection(set_B))
print('Symmetric difference of sets: ', set_A.symmetric_difference(set_B))
print('Difference of SetA and Set B : ', set_A.difference(set_B))


# ### Operators with Sets

# ##### Set Operations using Bit-wise opeartors

# In[11]:


print('Symmetric difference of sets: ', set_A ^ set_B) 
print('Intersection of sets: ', set_A & set_B)
print('Union of sets: ', set_A | set_B)
print('Difference of SetA and Set B : ', set_A - set_B)


# ##### Testing presence of elements using Membership Operators

# In[12]:


0 in s1


# In[13]:


3 not in s1


# #### isuperset()

# In[16]:


print('Set 1 is : ',s1)
s2 = {'b',1,'a',37}
s3 = {'b', 1, '37'}
print('Set 2 is : ',s2)
print('Set 3 is : ',s3)
print('s2 is subset of s1? : ', s1.issuperset(s2))
print('s3 is subset of s1? : ', s1.issuperset(s3))


# In[22]:


#it clears all the elemets of set and gives empty set
s2.clear()
s2


# In[23]:


#this method will update the elements in the set
s2.update('Data')
s2


# In[ ]:





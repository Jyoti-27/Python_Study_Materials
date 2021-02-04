#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# ### Series Concatenation

# In[48]:


ser1=pd.Series(['A', 'B', 'C'], index=[1,2,3])
ser1


# In[47]:


ser2=pd.Series(['D', 'E', 'F'], index=[4,5,6])
ser2


# In[50]:


#concat () function  for concatenating the  series
#stack the  series one below the other
print("Concatenated series is \n", pd.concat([ser1, ser2]))


# In[11]:


ser3=pd.Series(['F', 'G', 'H'], index=[9,10,11])
ser3


# In[12]:


list=[ser1,ser2,ser3]
print(pd.concat(list))


# ###  DatafRame Concatenation

# In[15]:


df1=pd.DataFrame({'A':['axe', 'art', 'ant'], 'B':['bat', 'bar', 'bin'],  'C': ['cap', 'cat', 'car']})
df1


# In[25]:


df2=pd.DataFrame({'D':['dog', 'den', 'dot'], 'E':['ear', 'eat', 'egg'],  'F': ['fan', 'fat', 'fog']})
df2


# ###  Concatention can be rowwise one DF below another axis =0
# ###  columns stacked alongside axis=1

# In[23]:


print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=0))
#for overlapping columns  the values are also stacked one  below 
#concatentaion with axis=0 considers the overlap of columns


# In[27]:


print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=0,  ignore_index=True))


# In[26]:


print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=1))


# In[32]:


#case for common columns
df1=pd.DataFrame({'A':['axe', 'art', 'ant'], 'B':['bat', 'bar', 'bin'],  'C': ['cap', 'cat', 'car']})
df2=pd.DataFrame({'D':['dog', 'den', 'dot'], 'B':['ear', 'eat', 'egg'],  'C': ['fan', 'fat', 'fog']})
print(df1)
print(df2)
#print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=0, ignore_index=True))
print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=1))
#with repeated columns   it will just append the columns
#it will consider common rows


# ### Axis=0
# * Concatenation just appends on dataframe below another
# * considers the intersection of columns stcaks values for them one below another
# * rowise indices if there is repition it reains the repitions

# ### Axis=1
# * Concatenation just appends one dataframe alonside the other columns are put together
# * considers the intersection of rows stcaks values for them one on the side of other
# * column  indices(column names) if there is repition it retains the repetitions

# In[37]:


#case for no common  rows
df1=pd.DataFrame({'A':['axe', 'art', 'ant'], 'B':['bat', 'bar', 'bin'], 
                  'C': ['cap', 'cat', 'car']}, index=[1,2,3])
df2=pd.DataFrame({'D':['dog', 'den', 'dot'], 'E':['ear', 'eat', 'egg'], 
                  'F': ['fan', 'fat', 'fog']}, index =[1,2,3])
print(df1)
print(df2)
print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=1))


# * eg: of two file having common empids and different columns 
# *  one file has name and address
# * another file has dept salary

# In[38]:


#case for common row indices columns
df1=pd.DataFrame({'A':['axe', 'art', 'ant'], 'B':['bat', 'bar', 'bin'], 
                  'C': ['cap', 'cat', 'car']}, index=[1,2,3])
df2=pd.DataFrame({'D':['dog', 'den', 'dot'], 'E':['ear', 'eat', 'egg'], 
                  'F': ['fan', 'fat', 'fog']}, index =[2,3,4])
print(df1)
print(df2)
print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=1))


# In[40]:



print(df2)
print("Concatenated dataframes axis=0\n#case forno  common row indices columns
df1=pd.DataFrame({'A':['axe', 'art', 'ant'], 'B':['bat', 'bar', 'bin'], 
                  'C': ['cap', 'cat', 'car']}, index=[1,2,3])
df2=pd.DataFrame({'D':['dog', 'den', 'dot'], 'E':['ear', 'eat', 'egg'], 
                  'F': ['fan', 'fat', 'fog']}, index =[4,5,6])
print(df1)", pd.concat([df1,df2], axis=0))


# In[41]:


#case forno  common row indices columns
df1=pd.DataFrame({'A':['axe', 'art', 'ant'], 'B':['bat', 'bar', 'bin'], 
                  'C': ['cap', 'cat', 'car']}, index=[1,2,3])
df2=pd.DataFrame({'D':['dog', 'den', 'dot'], 'E':['ear', 'eat', 'egg'], 
                  'F': ['fan', 'fat', 'fog']}, index =[4,5,6])
#conacatenation on axis =0 stacks the rows repition of row is retained, 
#stack the overllaping column values
#concatenation axis=1 stacks the columns repition of column is reatined,
#stack the overlapping row value
print(df1)
print(df2)
print("Concatenated dataframes axis=0\n", pd.concat([df1,df2], axis=1))


# ### Merge  is based on a common column
# 

# In[44]:


df_stud = pd.DataFrame({'St_id': [101,102,103,104,105],'Branch': ['IT','CS','ECE','CS','Mech']})
df_stud


# In[51]:


df_fac = pd.DataFrame({'F_id' : [110,120,130,140,150 ],'F_name' : ['A', 'B', 'C', 'D', 'E'],'Branch': ['ECE','Mech', 'EEE', "IT", 'CS'] })
#print("Student dataframe: \n", df_stud,'\nFaculty Dataframe :\n', df_fac)
df_fac
#print(pd.concat([df_stud, df_fac], axis=1))
print(pd.merge(df_stud, df_fac,on='Branch', sort=True))


# In[52]:


df1 = pd. DataFrame({'key' :['b', 'a', 'd','e'], 'data1': [0,4,6,8]}) #has unique
df2 =pd. DataFrame({'key' :['a', 'b', 'd', 'f'], 'data2': [3,6,9,11]})   # has unique row labels
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)


# In[53]:


print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   # union of keys


# In[57]:


print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))
# intersectionof keys


# In[55]:


df1 = pd. DataFrame({'key' :['b', 'a', 'd','e'], 'data1': [0,4,6,8]}) #has unique
df2 =pd. DataFrame({'key' :['a', 'b', 'd', 'f'], 'data2': [3,6,9,11]})   # has unique row labels
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)


# In[19]:


print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))
# keys from left dataframe


# In[58]:


print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))
# keys from Right dataframe


# ### Summary of the above 
# #### One One join with four cases outer, inner, left and right

# In[60]:


#many one merge
df1=pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a','a'], 'data1':[10,20,30,40,50,60]})
df2=pd.DataFrame({'key':['a', 'b', 'd'], 'data2':[100, 200, 300]})
print("\n", df1)
print("\n", df2)
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# union of keys 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))    
# intersection of keys 
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))  
#  keys from left dataframe
print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))   
#  keys from right  dataframe


# In[44]:


# Many many merge
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a'], 'data1': [10,20,30,40,50,60]})  
#has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'b', 'a', 'd'], 'data2': [100,200,300,400,500]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to many  merge situation
#No of rows in the dataframe = 6x5 for outer

#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# Union of keys 

#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))   
# Intersection of keys

#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))    
#  keys from left dataframe

print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True, indicator=True))  
# Here left and outer is same and Right and Inner is same


# ## Session 24_01_2021

# ###  Merge over indices
# * left_index and right_index flags can be used to perform merge over the similar index of the dataframes.
# * Also, join( ) method in the DataFrame class performs the merge by default on indices

# In[54]:


df1 = pd. DataFrame({'key' :['b', 'a', 'd','e'], 'data1': [0,4,6,8]}) #has unique
df2 =pd. DataFrame({'key' :['a', 'b', 'd', 'f'], 'data2': [3,6,9,11]})   # has unique row labels
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


# In[55]:


print('\nUsing merge on indices: \n',pd.merge(df1, df2, how='outer', left_index=True, right_index=True))
#by default it adds suffixes _x  and _y on the common column
#by default how=inner. here  we can have all options


# In[68]:


#DataFrame has a convenient join method for merging by index
#print('\nUsing join( ): \n', df1.join(df2))
print('\nUsing join( ): \n', df1.join(df2, how='inner', lsuffix='_df1', rsuffix='_df2'))
#lsuffix='_x', rsuffix='_y')
#default  is left  join


# In[6]:


print("Concatenated dataframes axis=1\n", pd.concat([df1,df2], axis=1))


# In[58]:


# for merge by index if we have a different index
df1 = pd. DataFrame({'key' :['b', 'a', 'd','e'], 'data1': [0,4,6,8]}, index= [10,20,30,40]) #has unique
df2 =pd. DataFrame({'key' :['a', 'b', 'd', 'f'], 'data2': [3,6,9,11]}, index  = [40,50,60,70])   # has unique row labels
print('\nUsing merge on indices: \n',pd.merge(df1, df2, how='inner' , left_index=True, right_index=True))


# In[60]:


# If we want to join using the key columns, we need to set key to be the index in both `df1` and `df2`.
# The joined DataFrame will then have the  key as its index
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a'], 'data1': [10,20,30,40,50]})  
#has multiple rows labelled a and b

df2 = pd.DataFrame({'key' : ['a', 'b', 'a', 'd'], 'data2': [100,200,300,400]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)


# In[70]:


dfn1 = df1.set_index('key')
dfn2 = df2.set_index('key')
print(dfn1)
print('\n Using merge on indices: \n',pd.merge(dfn1, dfn2, left_index=True, right_index=True))
#For merge how="inner"
#print('\nUsing join( ): \n', dfn1.join(dfn2, lsuffix='_x', rsuffix='_y'))
#for join how='left' by default


# ## An Example

# In[62]:


df_stud = pd.DataFrame({'St_id': [101,102,103,104,105],'Branch': ['IT','CS','ECE','CS','Mech']})
df_fac = pd.DataFrame({'F_id' : [110,120,130,140,150 ],'F_name' : ['A', 'B', 'C', 'D', 'E'],
                       'Branch': ['ECE','Mech', 'EEE', "IT", 'CS'] })
print("Student dataframe: \n", df_stud,'\nFaculty Dataframe :\n', df_fac)


# In[63]:


# Merge on commom column i.e Branch
#next try all values of how= inner, outer, left, right
df_merge = pd.merge(df_stud, df_fac, on = 'Branch', how='inner', sort = True)
print("Merged dataframe : \n ", df_merge)   #Merge on a common column


# * When similar columns have different names in different dataframes

# In[64]:


df_stud = pd.DataFrame({'St_id': [101,102,103,104,105],'Branch': ['IT','CS','ECE','CS','Mech']})
df_fac1 = pd.DataFrame({'F_name' : ['A', 'B', 'C', 'D', 'E'],
                        'Stream': ['ECE','Mech', 'EEE', "IT", 'CS'] })
#print("Student Details : \n", df_stud, 'Faculty Details: \n', df_fac)
print("Merged Dataframes : \n", pd.merge(df_stud, df_fac1, left_on = 'Branch', right_on = 'Stream'))


# In[75]:


# the redundant column can also be dropped
new_df=pd.merge(df_stud, df_fac1, left_on = 'Branch', right_on = 'Stream')
new_df

print(new_df.drop('Stream', axis = 1))


# ## Merge over indices same example

# In[31]:


print('\n Using merge on indices: \n',pd.merge(df_stud, df_fac, left_index=True, right_index=True))
print('\n Using join( ): \n', df_stud.join(df_fac, lsuffix='_stud', rsuffix='_fac'))


# In[34]:


#will merge with the default common index else set_index as Branch
df1 = df_stud.set_index('Branch')
df2 = df_fac1.set_index('Stream')
print("Student Details : \n", df1, '\n Faculty Details: \n', df2)
#print('\nUsing merge on indices: \n',pd.merge(df1, df2, left_index=True, right_index=True))
print('\nUsing join( ): \n', df1.join(df2))


# In[ ]:





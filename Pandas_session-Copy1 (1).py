#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd


# In[6]:


print(pd.__version__)
get_ipython().run_line_magic('pinfo', 'pd')


# # Creation of Pandas Series

# In[7]:


series = pd.Series([0.2, 0.5, 0.75, 1.6])    #call the constructor and send the values as a list
print("Pandas Series:\n" , series)


# Attributes of Pandas Series

# In[8]:


series.unique()


# In[9]:


print("Series.values: ",series.values)   #to find the values in a series
print("Index of Series: ", series.index)
print("Data type of Series.values: ",series.values.dtype)
print("Data type of   Series", type(series.values))
print("Type of Series", type(series))


# In[10]:


s = pd.Series([5,4,3],  index=[100, 200, 300])  #creating a series with a given index, index has to be given as 2nd parameter
print("Series is : \n", s, '\n Indices are : ', s.index)
print("Data type of   Series", type(series.values)) 


# ## Creating Series from a List

# In[26]:


List=[20, 15, 42, 33, 94, 8, 5]    #Default indexing or Implicit Indexing
print("List is: " , List)
ser_list= pd.Series([20, 15, 42, 33, 94, 8, 5])
print("Series from List\n", ser_list)
print("Data type of   Series", type(ser_list.values))
print("Type of Series", type(ser_list))


# In[27]:


print("Explicit Indexing: \n",
      pd.Series(List, index = ['i','ii','iii','iv','v','vi','vii']))


# In[28]:


#Update the whole index of  a series
s1= pd.Series([0,1,2,3,4])
print(s1)
s1.index=['A','B','C','E','E']
print(s1['E'])


# ##  Creating Series from numpy array
# ###  Numpy 1D array vs Series
# Array contains implicit indexing, series has explicit indexing along with some additional capabilities

# In[31]:


arr = np.array([10, 20, 30, 40, 50])   #creating a numpy array
ser_arr = pd.Series(arr)               #creating Series from a numpy array
print("Pandas Series:\n" , ser_arr)
print("Data type of   Series", type(ser_arr.values))
print("Type of Series",type(ser_arr))    #Observe difference between dtype between List and array
#dtype tells memory allocated to one item or element of an array. it is an array method
#type() is like type(str)   dtype tells memory allocated like int32 float64


# In[32]:


np_arr= np.random.random(5)
index= ['a','b', 'c','d', 'e']   #index 
ser_arr=pd.Series(np_arr, index)
print("Series \n", ser_arr)      #show that repition is allowed in index


# ## Creating series from a dictionary
# 

# In[36]:


dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}      #creating a Dictionary
print("dictinary is: ", dict)
ser_dict = pd.Series(dict)         # creating a Series from a Dictionary
print("Series is \n", ser_dict)
print("b" in ser_dict)
print('Indices are : ', ser_dict.index,'\n Elements of the series are : ', ser_dict.values)


# In[37]:


d={'monkey':153 ,'rat':212 ,'cotton':334 ,'fan':98}
print("Dictionary is: ", d)
ser_d=pd.Series(d)
print("Series from Dictionary:\n", ser_d)
print('Indices are : ', ser_d.index,'\n Elements of the series are : ', ser_d.values)


# ## Indexing and Slicing

# In[38]:


#Acessing, Indexing and Slicing of Values in a series
#Since a series is a Numpy array we can access elements using the default numeric index like array
#array or list type of slicing
ser_arr = pd.Series([10, 20, 30, 40, 50,60])
print(ser_arr[3])
print(ser_arr[1:4])      #array or list type of slicing
print(ser_arr[:4])
print(ser_arr[3:])
print(ser_arr[1:6:2])
print(ser_arr[: : 2])
ser_arr[3]=100          #update of a series this means series values are mutable
#print(ser_arr)


# In[40]:


#Acessing, Indexing and Slicing of Values in a series
#Since a series is a Numpy array we can access elements using the default numeric index like array
#array or list type of slicing
ser_arr = pd.Series([10, 20, 30, 40, 50,60])
print(ser_arr[3])
print(ser_arr[1:4])      #array or list type of slicing
print(ser_arr[:4])
print(ser_arr[3:])
print(ser_arr[1:6:2])
print(ser_arr[: : 2])
ser_arr[3]=100          #update of a series this means series values are mutable
print(ser_arr)


# In[41]:


# familiar attributes from NumPy arrays
print("\n ser_arr.size: ",ser_arr.size , 
      '\n ser_arr.shape: ',ser_arr.shape,
      '\n ser_arr.ndim: ',ser_arr.ndim,
      '\n ser_arr.dtype: ',ser_arr.dtype)


# In[42]:


#Another way to slice a series is to select elements by specifying the index
#Fancy Indexing
ser_slice=pd.Series(ser_arr, index=[3,2])     #select rows with the index
print(ser_slice)   
print(ser_slice)


# In[43]:


#Accessing series elements in a dictionary way. this is with explicit index or key
dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}      #creating a Dictionary
print("dictinary is ", dict)
ser_dict = pd.Series(dict)         # creating a Series from a Dictionary
print("ser_dict['b']:\n", ser_dict['b'])   #Accessing oone element
print("ser_dict['b':'e']:\n ", ser_dict['b': 'e'])
print("ser_dict[: 'd']:\n", ser_dict[:'d'])
print("ser_dict[['b', 'e']]:\n",  ser_dict[['b', 'e']])    #Fancy Indexing 


# In[44]:


s1= pd.Series([0,1,2,3,4], index=['A','B','C','D','E'])
print(s1)
#Series operations similar to sets and dictinary
print('A' in s1)
print(s1.keys())         #similarity to dictionary
print(list(s1.items()))   #similarity to dictionary
print(s1.values)      #access to dictionary values

# extending the series like dictinaries
s1['F'] = 5
print("\n After updation : \n",s1)


# In[45]:


# masking  on the values to extract subsets of data
s1= pd.Series([10,20,30,40,50], index=['A','B','C','D','E'])
print(s1)
print('Masking')
print("s1[(s1>10) & (s1<40)] \n", s1[(s1>10) & (s1<40)])
#print('Fancy indexing')
#print("s1[['A', 'C']] \n" , s1[['A', 'C']])


# Slicing may be the source of the most confusion. Notice that when slicing with an explicit index (i.e. data['a':'c']), the final index is included in the slice, while when slicing with an implicit index (i.e. data[0:4]), the final index is excluded from the slice.

# In[46]:


#Problem that may arise with implicit and explicit indexing
#Consider an Example where the explicit index is also a number
s = pd.Series([5,4,3,2],  index=[100, 200, 300,400])  # index has to be given as 2nd parameter
print("Series is : \n", s, '\n Indices are : ', s.index) 
#print(s['100':'300'])
print(s[1:3])


# Because of this potential confusion in the case of integer indexes, Pandas provides some special indexer attributes
# loc() - explicit indexing  and iloc() always refers to  the implicit Python-style index:

# In[47]:


#the loc() - indexing and slicing with explicit index
#the iloc() - indexing and slicing with implicit index
s = pd.Series([5,4,3,2],  index=[100, 200, 300,400])  # index has to be given as 2nd parameter
print("Series is : \n", s, '\n Indices are : ', s.index)
print("Series with explicit index :s.loc[100:300]\n", s.loc[100:300])  #it will take the end value too
print("Series with implicit index:  s.iloc[1:3] \n" , s.iloc[1:3])
print('Implicit access  : s.iloc[2] \n' , s.iloc[2])
print('Explicit access  : s.loc[200] \n' , s.loc[200])


# # Series Operations

# In[48]:


s1=pd.Series([6,7,8,9,5])
s3 = pd.Series([1,2,3,4], index = ['a','b','c','d'])
print('s1: \n',s1,'s3: \n',s3)
s4 = s1.append(s3)
print('Appended  series: \n',s4 )
# Delete a row with a particular element
s4.drop(['c'])
print("Series s4  after dropping 'c':\n",  s4)


# ## Aritmetic Functions 
# ### Elementwise Addition, Subtraction, Multiplication and Division

# In[49]:


import pandas as pd
#Create two series 
s1=pd.Series([6,7,8,9,5])
s2=pd.Series([0,1,2,3,4,5,7])
print('Series are : \n',s1, '\n', s2)


# In[50]:


print('Addition of series: \n', s1.add(s2))    #Elementwise addition
print('\n Subtraction of series: \n', s1.sub(s2))    #Elementwise Subtraction
print('\n Multiplication of series: \n', s1.mul(s2))
print('\n Division of series: \n', s1.div(s2))
print('Series are : \n',s1, '\n', s2)    #Series remains unchanged


# ##  Aggregate Functions  - Which reduce the series to a single number

# In[51]:


print("\nMedian of series s2 is", s2.median())
print("\n Mean of series s2 is " , s2.mean())
print("\n Maximum of series s2 is", s2.max())
print("\n Minimum of series s2 is", s2.min())


# In[52]:


#Series with char/ string elements
string=pd.Series(['a','b','c','S','e','J','g','B','P','o'])
print('A Series wih String values: \n ', string)
print('string.str.upper(): \n',string.str.upper())
print('string.str.lower(): \n',string.str.lower())


# In[53]:


#Avoid this
# Just as we can do slicing like an array on a series index we can also do set operations on an index but here 
#index should not have repitition
# Index as ordered set
indA = pd.Index([1, 3, 5, 7, 9])    #we can just create a Index object
indB = pd.Index([2, 3, 5, 7, 11])

print(indA & indB) # intersection
print(indA | indB) # union
print(indA ^ indB) # symmetric difference


# In[55]:


#Dont do this  #Index as an immutable array 
#Acessing, Indexing and Slicing of Indices in a series
#Index is like an ordered set
ser=pd.Series([6,7,8,9,5,3])
print(ser.index)
print(ser.index[3])
print(ser.index[1:4])      #array or list type of slicing
print(ser.index[:4])
ser.index[3]=10    #index array cannot be updated
print(ser.index)   #error


# # Pandas DataFrames

# * Table with indexed rows and columns
# * can be seen as a sequence of aligned Series object, i.e., share same index
# * generalization of NumPy 2D Arrays
# * with heterogenous and/or missing data

# ## Creation of DataFrames

# In[56]:


#Dataframe as a stack of Series.  we create two columns using series and then make a DataFrame
population_d= {'California': 3833, 'Texas': 8193,
                'New York': 6511, 'Florida': 5560, 'Ohio': 1135}    #Statewise population 
print(population_d, type(population_d))
population = pd.Series(population_d)
print(population)


# In[57]:


area_d = {'California': 423967, 'Texas': 695662, 'New York': 141297,   
             'Florida': 170312, 'Ohio': 149995}
area = pd.Series(area_d) 
print(area)


# In[58]:


states = pd.DataFrame({'Population': population,  'Area': area})
print("Data Frame of States: \n", states)


# ## DataFrame Attributes

# In[59]:


print('\n', states.index)     #row indices
print('\n', states.columns)    #column names
print('\n', states['Area'])     #access a column on a DataFrame like a key value pair
print('\n',states.Area)        #Columns can also be accessed as an Attribute
print('\n',states.Area is states['Area'])


# using Numpy Arrays

# In[60]:


import numpy as np
num_arr=np.random.randn(6,4)     #random delection of numbers following a standard normal distribution
print("Array is : \n", num_arr)  
cols=['A','B','C','D']            #arrays will not have index and columns
df1=pd.DataFrame(num_arr, columns=cols, index = ['i', 'ii', 'iii', 'iv', 'v', 'vi'])
#array of values, index, column
print('\n Data Frame from numpy array is : \n')
df1


# ### DataFrame as a Specialized Dictionary
#  DataFrame maps a column name to a Series of column data.

# In[61]:


# create a dataframe using a dictionary of Lists, values are lists and column names are keys
data= {'city' : ['Bombay', 'Chennai', 'Chennai', 'Delhi', 'Mysore' ], 'year' : [2001, 2005, 2003, 2001, 2000],  
        'pop' : [25, 35, 20, 40, 15]}
df2= pd.DataFrame(data)
print(df2)
#observe index is assigned automatically


# In[62]:


# create a dataframe using a dictionary of Lists, values are lists and column names are keys
data= {'city' : ['Bombay', 'Chennai', 'Chennai', 'Delhi', 'Mysore' ], 'year' : [2001, 2005, 2003, 2001, 2000],  
        'pop' : [25, 35, 20, 40, 15]}
labels=['a', 'b', 'c', 'd', 'e']
df2= pd.DataFrame(data, index=labels)
print(df2)
#observe index is assigned automatically


# In[63]:


#create a dataframe from a list of dictionaries
df3=pd.DataFrame([{'a': 1, 'b': 2, 'c':3, 'd':4}, {'a': 10, 'b': 20, 'c': 30}, {'a': 11, 'b': 21, 'c': 41, 'd': 51}])
print(df3)  # creating a dataframe from a list of dictionaries


# ## Visualizing DataFrames 

# In[64]:


#First Create a DataFrame
data={'Animals': ['cat','cat','turtle','dog','dog','cat','turtle','cat','dog','dog'],
          'Age': [2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3], 
      'Visits' : [1,3,2,3,2,3,1,1,2,1], 
    'Priority' : ['y','y','n','y','n','n','n','y','n','n']}
labels=['a','b','c','d','e','f','g','h','i','j']
animals_data=pd.DataFrame(data,index=labels)
animals_data
#observe the data type of each column


# ### DataFrame Attributes  - index,  cols,  values, datatype of values

# In[65]:


print("\n animals_data.index:\n ", animals_data.index)
print("\n animals_data.columns:\n", animals_data.columns)
print("\n animals_data.values:\n", animals_data.values)      #will show only values without index and column names
print("\n animals_data.dtypes:\n", animals_data.dtypes)    #will show the datatype of each column


# In[ ]:


###  Visualizing DataFrames


# In[66]:


print(animals_data)   #Visualizing complete may not be feasible in real data


# In[67]:


print(animals_data.head())   # will display top 5 lines of the dataFrame
print(animals_data.tail())     # will display bottom 5 lines of the dataframe


# ### Details about the DataFrame

# In[68]:


# Information about the whole dataframe
print('\n Info : \n', animals_data.info())   #nrows, ncols, index, datatype of each column, number of nonnull values

#statistical data of dataframe
print('\n Statistical Description : \n',animals_data.describe())
#mean std max min quartiles for columns with numeric type
print('\n Description for object values: \n',animals_data.describe(include = ['object'])) 
#count, unique values, mode , freq


# ## DataFrame Operations

# * Accessing/Slcing Data in a DataFrame
# * Indexing into a DataFrame is for retrieving one or more columns either with a single value or sequence

# In[69]:


print("\n animals_data.index:\n ", animals_data.index)    #accessing index
print("\n animals_data.columns:\n", animals_data.columns)    #accessing column names
#Accessing columns of a DataFrame  2 ways
print("\n animals_data['Animals']:\n",animals_data['Animals'] )
print("\n animals_data['Age'] :\n", animals_data['Age'])
print("\n animals_data.Animal:\n",animals_data.Animals)
animals_data[['Age','Visits']]   #Displaying particular Columns

print("\n animals_data.loc['b', 'Age']:\n",animals_data.loc['b', 'Age'])   #accessing by row and column
animals_data.loc['b', 'Age'] =50
print("\n animals_data.loc['b', 'Age']:\n",animals_data.loc['b', 'Age'])   #updatinng a value in a Dataframe


# In[70]:


#Accessing rows of a DataFrame by implict and explicit index
print("\n animals_data.loc['a', :] :\n", animals_data.loc['a', :])   #values of a row are given as columns
print("\n rows by index animals_data.loc['b']:\n", animals_data.loc['b'])
print("\ Rows 1 to 3 using slicing:\n",animals_data.iloc[1:3, 2:3] )      #iloc for implicit indexing


# In[75]:


#Acessing individual elements in the table by row and column
print("\n animals_data.loc['b', 'Age']:\n",animals_data.loc['b', 'Age'])   #accessing by row and column
animals_data.loc['b', 'Age'] =50
print("\n animals_data.loc['b', 'Age']:\n",animals_data.loc['b', 'Age'])   #updatinng a value in a Dataframe
print("\n animals_data.iloc['b', 'Age']:\n",animals_data.iloc[2,2])   #accessing by row and column
df2.ix[:5, 'animals':'visits']


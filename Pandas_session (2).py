#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[3]:


print(pd.__version__)
get_ipython().run_line_magic('pinfo', 'pd')


# # Creation of Pandas Series

# In[4]:


series = pd.Series([0.2, 0.5, 0.75, 1.6])    #call the constructor and send the values as a list
print("Pandas Series:\n" , series)


# Attributes of Pandas Series

# In[5]:


series.unique()


# In[6]:


print("Series.values: ",series.values)   #to find the values in a series
print("Index of Series: ", series.index)
print("Data type of Series.values: ",series.values.dtype)
print("Data type of   Series", type(series.values))
print("Type of Series", type(series))


# In[7]:


s = pd.Series([5,4,3],  index=[100, 200, 300])  #creating a series with a given index, index has to be given as 2nd parameter
print("Series is : \n", s, '\n Indices are : ', s.index)
print("Data type of   Series", type(series.values)) 


# ## Creating Series from a List

# In[8]:


List=[20, 15, 42, 33, 94, 8, 5]    #Default indexing or Implicit Indexing
print("List is: " , List)
print("Series from List\n", ser_list)
print("Data type of   Series", type(ser_list.values))
print("Type of Series", type(ser_list))


# In[9]:


print("Explicit Indexing: \n",
      pd.Series(List, index = ['i','ii','iii','iv','v','vi','vii']))


# In[10]:


#Update the whole index of  a series
s1= pd.Series([0,1,2,3,4])
print(s1)
s1.index=['A','B','C','E','E']
print(s1['E'])


# ##  Creating Series from numpy array
# ###  Numpy 1D array vs Series
# Array contains implicit indexing, series has explicit indexing along with some additional capabilities

# In[11]:


arr = np.array([10, 20, 30, 40, 50])   #creating a numpy array
ser_arr = pd.Series(arr)               #creating Series from a numpy array
print("Pandas Series:\n" , ser_arr)
print("Data type of   Series", type(ser_arr.values))
print("Type of Series",type (ser_arr))    #Observe difference between dtype between List and array
#dtype tells memory allocated to one item or element of an array. it is an array method
#type() is like type(str)   dtype tells memory allocated like int32 float64


# In[12]:


np_arr= np.random.random(5)
index= ['a','b', 'c','d', 'e']   #index 
ser_arr=pd.Series(np_arr, index)
print("Series \n", ser_arr)      #show that repition is allowed in index


# ## Creating series from a dictionary
# 

# In[21]:


dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}      #creating a Dictionary
print(dict)
ser_dict = pd.Series(dict)         # creating a Series from a Dictionary
print("Series is \n", ser_dict)
print("b" in ser_dict)
print('Indices are : ', ser_dict.index,'\n Elements of the series are : ', ser_dict.values)


# In[22]:


d={'monkey':153 ,'rat':212 ,'cotton':334 ,'fan':98}
print("Dictionary is: ", d)
ser_d=pd.Series(d)
print("Series from Dictionary:\n", ser_d)
print('Indices are : ', ser_d.index,'\n Elements of the series are : ', ser_d.values)


# ## Indexing and Slicing

# In[23]:


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


# In[24]:


# familiar attributes from NumPy arrays
print("\n ser_arr.size: ",ser_arr.size , 
      '\n ser_arr.shape: ',ser_arr.shape,
      '\n ser_arr.ndim: ',ser_arr.ndim,
      '\n ser_arr.dtype: ',ser_arr.dtype)


# In[25]:


#Another way to slice a series is to select elements by specifying the index
#Fancy Indexing
ser_slice=pd.Series(ser_arr, index=[3,2])     #select rows with the index
print(ser_slice)   
print(ser_slice)


# In[26]:


#Accessing series elements in a dictionary way. this is with explicit index or key
dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}      #creating a Dictionary
print("dictinary is ", dict)
ser_dict = pd.Series(dict)         # creating a Series from a Dictionary
print("ser_dict['b']:\n", ser_dict['b'])   #Accessing oone element
print("ser_dict['b':'e']:\n ", ser_dict['b': 'e'])
print("ser_dict[: 'd']:\n", ser_dict[:'d'])
print("ser_dict[['b', 'e']]:\n",  ser_dict[['b', 'e']])    #Fancy Indexing 


# In[27]:


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


# In[28]:


# masking  on the values to extract subsets of data
s1= pd.Series([10,20,30,40,50], index=['A','B','C','D','E'])
print(s1)
print('Masking')
print("s1[(s1>10) & (s1<40)] \n", s1[(s1>10) & (s1<40)])
#print('Fancy indexing')
#print("s1[['A', 'C']] \n" , s1[['A', 'C']])


# Slicing may be the source of the most confusion. Notice that when slicing with an explicit index (i.e. data['a':'c']), the final index is included in the slice, while when slicing with an implicit index (i.e. data[0:4]), the final index is excluded from the slice.

# In[29]:


#Problem that may arise with implicit and explicit indexing
#Consider an Example where the explicit index is also a number
s = pd.Series([5,4,3,2],  index=[100, 200, 300,400])  # index has to be given as 2nd parameter
print("Series is : \n", s, '\n Indices are : ', s.index) 
#print(s['100':'300'])
print(s[1:3])


# Because of this potential confusion in the case of integer indexes, Pandas provides some special indexer attributes
# loc() - explicit indexing  and iloc() always refers to  the implicit Python-style index:

# In[30]:


#the loc() - indexing and slicing with explicit index
#the iloc() - indexing and slicing with implicit index
s = pd.Series([5,4,3,2],  index=[100, 200, 300,400])  # index has to be given as 2nd parameter
print("Series is : \n", s, '\n Indices are : ', s.index)
print("Series with explicit index :s.loc[100:300]\n", s.loc[100:300])  #it will take the end value too
print("Series with implicit index:  s.iloc[1:3] \n" , s.iloc[1:3])
print('Implicit access  : s.iloc[2] \n' , s.iloc[2])
print('Explicit access  : s.loc[200] \n' , s.loc[200])


# # Series Operations

# In[31]:


s1=pd.Series([6,7,8,9,5])
s3 = pd.Series([1,2,3,4], index = ['a','b','c','d'])
print('s1: \n',s1,'s3: \n',s3)
s4 = s1.append(s3)    #Observe no copy is created 
print('Appended  series: \n',s4 )
# Delete a row with a particular element
s4.drop(['c'])
print("Series s4  after dropping 'c':\n",  s4)


# ## Aritmetic Functions 
# ### Elementwise Addition, Subtraction, Multiplication and Division

# In[32]:


import pandas as pd
#Create two series 
s1=pd.Series([6,7,8,9,5])
s2=pd.Series([0,1,2,3,4,5,7])
print('Series are : \n',s1, '\n', s2)


# In[33]:


# Series methods print('Addition of series: \n', s1.add(s2))    #Elementwise addition
print('\n Subtraction of series: \n', s1.sub(s2))    #Elementwise Subtraction
print('\n Multiplication of series: \n', s1.mul(s2))
print('\n Division of series: \n', s1.div(s2))
print('Series are : \n',s1, '\n', s2)    #Series remains unchanged


# ##  Aggregate Functions  - Which reduce the series to a single number

# In[34]:


print("\nMedian of series s2 is", s2.median())
print("\n Mean of series s2 is " , s2.mean())
print("\n Maximum of series s2 is", s2.max())
print("\n Minimum of series s2 is", s2.min())


# In[35]:


#Series with char/ string elements
string=pd.Series(['a','b','c','S','e','J','g','B','P','o'])
print('A Series wih String values: \n ', string)
print('string.str.upper(): \n',string.str.upper())
print('string.str.lower(): \n',string.str.lower())


# In[36]:


#Avoid this
# Just as we can do slicing like an array on a series index we can also do set operations on an index but here 
#index should not have repitition
# Index as ordered set
indA = pd.Index([1, 3, 5, 7, 9])    #we can just create a Index object
indB = pd.Index([2, 3, 5, 7, 11])

print(indA & indB) # intersection
print(indA | indB) # union
print(indA ^ indB) # symmetric difference


# In[37]:


#Dont do this  #Index as an immutable array 
#Acessing, Indexing and Slicing of Indices in a series
ser = pd.Series([10, 20, 30, 40, 50,60])
#Index is like an ordered set
print(ser.index)
print(ser.index[3])
print(ser.index[1:4])      #array or list type of slicing
print(ser.index[:4])
ser.index[3]=10    #index array cannot be updated


# # Pandas DataFrames

# * Table with indexed rows and columns
# * can be seen as a sequence of aligned Series object, i.e., share same index
# * generalization of NumPy 2D Arrays
# * with heterogenous and/or missing data

# ## Creation of DataFrames

# In[2]:


#Dataframe as a stack of Series.  we create two columns using series and then make a DataFrame
population_d= {'California': 3833, 'Texas': 8193,
                'New York': 6511, 'Florida': 5560, 'Ohio': 1135}    #Statewise population 
print(population_d, type(population_d))
population = pd.Series(population_d)
print(population)


# In[3]:


area_d = {'California': 423967, 'Texas': 695662, 'New York': 141297,   
             'Florida': 170312, 'Ohio': 149995}
area = pd.Series(area_d) 
print(area)


# In[4]:


states = pd.DataFrame({'Population': population,  'Area': area})  #two series with same index
print("Data Frame of States: \n", states)


# ## DataFrame Attributes

# In[51]:


states = pd.DataFrame({ 'Area': area_d})
#print("Data Frame of States: \n", states)
states
print('\n', states.index)     #row indices
print('\n', states.columns)    #column names
print('\n', states.values)
print('\n', states['Area'])     #access a column on a DataFrame like a key value pair
print('\n',states.Area)        #Columns can also be accessed as an Attribute
#print('\n',states.Area is states['Area'])
print('\n',states.loc['California'])   #accessing row of a dataframe with explicit index
print('\n', states.iloc[3])
print('\n', states.loc['California','Area'])
print('\n', states.iloc[3,1])


# using Numpy Arrays

# In[52]:


import numpy as np
num_arr=np.random.randn(6,4) #random delection of numbers following a standard normal distribution
print("Array is : \n", num_arr)  
cols=['A','B','C','D']    #arrays will not have index and columns
df1=pd.DataFrame(num_arr, columns=cols, index = ['i', 'ii', 'iii', 'iv', 'v', 'vi'])
#array of values, index, column
print('\n Data Frame from numpy array is : \n')
df1


# ### DataFrame as a Specialized Dictionary
#  * DataFrame maps a column name to a Series of column data.
#  * key is a column name and value is a series

# In[53]:


# create a dataframe using a dictionary of Lists, values are lists and column names are keys
data= {'city' : ['Bombay', 'Chennai', 'Chennai', 'Delhi', 'Mysore' ], 'year' : [2001, 2005, 2003, 2001, 2000],  
        'pop' : [25, 35, 20, 40, 15]}
df2= pd.DataFrame(data)
print(df2)
#observe index is assigned automatically


# In[54]:


# create a dataframe using a dictionary of Lists, values are lists and column names are keys
data= {'city' : ['Bombay', 'Chennai', 'Chennai', 'Delhi', 'Mysore' ], 'year' : [2001, 2005, 2003, 2001, 2000],  
        'pop' : [25, 35, 20, 40, 15]}   #this will have only columns no index
labels=['a', 'b', 'c', 'd', 'e']
df2= pd.DataFrame(data, index=labels)
print(df2)
#observe index is assigned automatically


# In[55]:


#Exercise
#create a dataframe from a list of dictionaries
df3=pd.DataFrame([{'a': 1, 'b': 2, 'c':3, 'd':4}, {'a': 10, 'b': 20, 'c': 30}, {'a': 11, 'b': 21, 'c': 41, 'd': 51}])
print(df3)  # creating a dataframe from a list of dictionaries


# ## Visualizing DataFrames 

# In[56]:


#First Create a DataFrame
data={'Animals': ['cat','cat','turtle','dog','dog','cat','turtle','cat','dog','dog'],
          'Age': [2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3], 
      'Visits' : [1,3,2,3,2,3,1,1,2,1], 
    'Priority' : ['y','y','n','y','n','n','n','y','n','n']}
labels=['a','b','c','d','e','f','g','h','i','j']
animals_data=pd.DataFrame(data,index=labels)
print(animals_data)
print(type(animals_data))      #type of the dataframe


# ### DataFrame Attributes  - index,  cols,  values, datatype of values

# In[57]:


print("\n animals_data.index:\n ", animals_data.index)
print("\n animals_data.columns:\n", animals_data.columns)
print("\n animals_data.values:\n", animals_data.values)      #will show only values without index and column names
print("\n animals_data.dtypes:\n", animals_data.dtypes)    #will show the datatype of each column


# In[ ]:


###  Visualizing DataFrames


# In[58]:


print(animals_data)   #Visualizing complete may not be feasible in real data


# In[59]:


print(animals_data.head())   # will display top 5 lines of the dataFrame
print(animals_data.tail())     # will display bottom 5 lines of the dataframe


# ### Details about the DataFrame

# In[60]:


# Information about the whole dataframe
print( animals_data.info()) #nrows, ncols, index, datatype of each column, number of nonnull values

#statistical data of dataframe
print('\n Statistical Description : \n',animals_data.describe())
#mean std max min quartiles for columns with numeric type

print('\n Description for object values: \n',animals_data.describe(include = ['object'])) 
#count, unique values, mode , freq


# ## DataFrame Operations

# * Accessing/Slcing Data in a DataFrame
# * Indexing into a DataFrame is for retrieving one or more columns either with a single value or sequence

# In[61]:


#Exercise
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


# In[62]:


#Accessing rows of a DataFrame by implict and explicit index
print("\n animals_data.loc['a', :] :\n", animals_data.loc['a', :])   #values of a row are given as columns                                             
print("\ Rows 1 to 3 using slicing:\n",animals_data.iloc[1:3, 2:3] )      #iloc for implicit indexing


# In[63]:


# Exercise
#Acessing individual elements in the table by row and column
print(animals_data)
print("\n animals_data.loc['b', 'Age']:\n",animals_data.loc['b', 'Age'])   #accessing by row and column
animals_data.loc['b', 'Age'] =50
print("\n animals_data.loc['b', 'Age']:\n",animals_data.loc['b', 'Age'])   #updatinng a value in a Dataframe
print("\n animals_data.loc['b', 'Age']:\n",animals_data.iloc[2,2])   #accessing by row and column

print(animals_data.iloc[:5, 2:4] )
print(animals_data.loc['b':'e', 'Animals':'Visits'] )


# In[64]:


print("Transpose of the Data Frame :")
animals_data.T


# ### Sorting DataFrames
# * By default is ascending order
# * Mandatory to provide (by = ' '), Sort by one column
# * Can also combine sorting with slicing

# In[65]:


#Methods in DataFrame object Sort By Values  
print(animals_data)
print("\n Sorting the Data Agewise:\n", animals_data.sort_values(by = 'Age', ascending = False))   #sort by which column
#Any missing value is sorted at end by default
animals_data.sort_values(by='Age')[1:4]

#Sort by index
print("\n Sorting the Data by Index:\n", animals_data.sort_index(axis=1)) #Since it is already sorted you dont see the change


# ## ReIndexing DataFrames
# * Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.

# In[66]:


#. Create a new index  Reindexing
print(animals_data)
animals_data_reindex = animals_data.reindex(['d', 'e', 'g', 'f', 'a', 'b', 'c', 'i', 'j'])
print("\n ReIndexed Data: \n",animals_data.reindex)     #will not modify original data
print("\n Sorted by row index:\n", animals_data_reindex.sort_index(axis=0))
print("\n Sorted by Column Index:\n", animals_data_reindex.sort_index(axis=1))


# ### Creating a copy of the DataFrame

# In[67]:


animals_data_c=animals_data.copy()
print("\n Copy of animals_data:\n", animals_data_c)


# ### Deleting a row or Column of  a DataFrame
# * The drop() function modifies  the size or shape of a Series or DataFrame,
# * can manipulate an object in-place without returning a new object
# * Be careful with inplace as it destroys any data that is dropped
# 

# In[68]:


print(animals_data)
print("Drop rows with names 'a; and 'b':\n", animals_data.drop(['a', 'b']))   #dropping rows
#print(animals_data)
#to drop the columns permanently use inplace - True
print("Drop rows with names 'a; and 'b':\n", animals_data_c.drop(['a', 'b'], inplace=True))  
print(" Animals_data _c with inplace = true: \n", animals_data_c)

print(animals_data.drop('Visits', axis=1)) 
#dropping column  columns are axis=1 for drop() default is row
#So if we dont mention axis = 1 it will search for a row with name 'Visits'
print(animals_data.drop('Visits', axis='columns'))


# ### Aggregate Functions
# * All aggregation functions discussed in Series can be performed on columns of a DataFrame as each column is like a Series

# In[69]:


#Why doing an Aggregation on a Row doesnt make sense
print("Mean of the Dataframe is: \n",animals_data.mean())    #mean of values in columns containing numeric data
print("\nMean of 'Age' is: ",animals_data[['Age']].mean())
print("\nTotal visits :",animals_data[['Visits']].sum())
print("\nMax visits: ",animals_data[['Visits']].max())
print("\nMin visits: ",animals_data[['Visits']].min())
print("\n Index of Max visits: ",animals_data[['Visits']].idxmax())
print("\n Index of Min visits: ",animals_data[['Visits']].idxmin())
print("\nSum: \n",animals_data.sum())     #for strings sum is string concatenation


# ### Handling Missing Values
# * Difference between None and np.nan
# *For Series and DataFrame both None and np.nan are handled as np.nan
# * To detect missing values the isnull() and notnull() functions in Pandas are used
# *Filling of Missing Values

# In[70]:


#Trouble with missing data  
#Why we need to drop missing values
import numpy as np
arr1 = np.array([1, None, 3, 4])    #observe None is a NoneType
print(arr1,  arr1.dtype)
print(arr1.sum())    #unsupported operand type(s) for +: 'int' and 'NoneType
print(arr1.mean())
arr2 = np.array([1, np.nan, 3,4])   #np.nan is a float type
print(arr2,  arr2.dtype)  
print(arr2.sum())                 #so np.nan is handled by  numpy  but not None
print(arr2.mean())


# In[71]:


print(pd.Series([1, np.nan, 2, None]))
ser_null = pd.Series(range(5,8), dtype=int)
print('\n',ser_null)
ser_null[0] = None 
print('\n',ser_null)
print('\n',ser_null.sum())
#casting the integer array to floating point, Pandas automatically converts the None to a NaN value.
#Series datatype converts a None also to a nan and it can do the aggregation even with the nan values .
#it ignores the nan values


# In[72]:


#Dataframe aggregation methods ignore nan values and find the sum
data = pd.DataFrame([[1,      np.nan, 2],    
                   [2,      3,      5],     
                   [np.nan, 4,      6]])  
print(data)
print(data.sum())    #sum by default is column sum axis =0
print(data.sum(axis=1))   #sum across columns


# In[ ]:





# ### Detecting Null Values
# * To detect missing values the isnull() and notnull() functions in Pandas are used

# In[73]:


print(pd.isnull(animals_data))    #isnull() function in pandas library
#print(animals_data.isnull())      #isnull() in DataFrame object
#Observe that Age has two missing values
print(pd.notnull(animals_data)) 


# In[74]:


# we do this with a simpler example
data = pd.DataFrame([[1,      np.nan, 2],    
                   [2,      3,      5],     
                   [np.nan, 4,      6]])  
print('\n data.isnull(): \n',data.isnull())
print('\n data.notnull(): \n',data.notnull())
data[data.notnull()]


# ##  Dropping Null values 
# * dropna() drops all Null values - might drop good data
# * We specify how or thresh parameters
# * DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# * how(any,all)
# * ‘any’ : If any NA values are present, drop that row or column.
# * ‘all’ : If all values are NA, drop that row or column. thresh - 3 means requires that many nonNA values
# * inplace is True or False
# * For finer-grained control, the thresh parameter specifies a min no. of non-null values for the row/column to be kept

# In[75]:


#Dropping null values
print(data.dropna())
data.dropna(axis='rows', thresh=2)   #axis =0 means drop rows which have missing values, 1 cols which have missing values
data.dropna(axis='columns', thresh = 3)


# ### Filling Missing values
# * We may choose to fill in different data according to the data type of the column
# * Both numpy.nan and None can be filled in using pandas.fillna(). 
# * For categorical columns (string columns), we want to fill in the missing values with mode. 
# * For numerical columns, we want to fill in the missing values with mean
# * DataFrame.fillna(value=None, method=None, axis=None, inplace=False

# In[76]:


data = pd.DataFrame([[1,      np.nan, 2],    
                   [2,      3,      5],     
                   [np.nan, 4,      6]]) 
print(data)
#print(data.fillna(0))     we can fill with column mean or mode for categorical data
#print(data.fillna(method='ffill'))
print(data.fillna(method='bfill'))
print(data)          # original data will not change, to change we need to set inplace = True
#find mean of each column and fill each individually


# ###  Reading a csv and excel file into a DataFrame

# In[81]:


#First Create a DataFrame
data={'Animals': ['cat','cat','turtle','dog','dog','cat','turtle','cat','dog','dog'],
          'Age': [2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3], 
      'Visits' : [1,3,2,3,2,3,1,1,2,1], 
    'Priority' : ['y','y','n','y','n','n','n','y','n','n']}
labels=['a','b','c','d','e','f','g','h','i','j']
animals_data=pd.DataFrame(data,index=labels)
print(animals_data)
#print(animals_data.fillna(0))
print("\n\n",animals_data.fillna(animals_data['Age'].mean()))  
#observe the data type of each column


# In[6]:


#First write dataframe to csv then read it back
data={'Animals': ['cat','cat','turtle','dog','dog','cat','turtle','cat','dog','dog'],
          'Age': [2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3], 
      'Visits' : [1,3,2,3,2,3,1,1,2,1], 
    'Priority' : ['y','y','n','y','n','n','n','y','n','n']}
labels=['a','b','c','d','e','f','g','h','i','j']
animals_data=pd.DataFrame(data,index=labels)
animals_data
#data.to_csv('animal.csv')


# In[8]:


animals_data.to_csv('animal.csv')


# In[84]:


df_animal=pd.read_csv('animal.csv')
df_animal.head(3)


# In[90]:


animals_data.to_excel('animals.xlsx',sheet_name='sheet1')
#animals_data.to_excel('animals.xlsx',sheet_name='sheet1')
df_animal2=pd.read_excel('animals.xlsx','sheet1', index_col=None)
df_animal2


# In[92]:


animals_data.to_excel('animal.xlsx',sheet_name='sheet1')
df_animal2=pd.read_excel('animal.xlsx', 'sheet1',
                         index_col=None, na_values=['NA'])
df_animal2


# ### Combining DataSets
# * Pandas concatenation preserves indices, even if it results in duplicate indices.
# * Series Concatenation
# * DataFrame Concatenation :  Concatenation one below another (axis=0) , Concatenation side by side (axis=1)
# * Ignore Index while concatenation

# In[15]:


ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3]) 
ser2 = pd.Series( ['D', 'E', 'F'], index=[4, 5, 6] )     #test with the same index
print("Series 1 : \n",ser1, "\nSeries 2 : \n",ser2)
print("Concatenating series: \n", pd.concat([ser1, ser2]))   


# In[ ]:


* DataFrame Concatenation


# In[17]:


df1 = pd.DataFrame({'A' : ['axe', 'art', 'ant'], 'B' : ['bat', 'bar', 'bin'], 'C' : ['cap', 'cat', 'car']},
                   index = [1,2,3])
df2 = pd.DataFrame({'D' : ['dam', 'den', 'dot'], 'E': [ 'ear', 'eat', 'egg'], 'F': ['fan', 'fog', 'fat']}, 
                   index =[ 2, 3, 6])
print("Data frame 1 : \n", df1,'\n Data Frame 2: \n', df2)
print("Concatenating Data Frames: \n",pd.concat([df1,df2], axis=0))  # axis =0 is stacking one below the other
print("Concatenating Data Frames along axis 1: \n",pd.concat([df1,df2], axis = 1))
#will consider common indices


# ##### Ignoring the index

# In[93]:


df_concat = pd.concat([df1, df2], ignore_index = True)
print("Concatenation of dataframes while ignoring the index: \n", df_concat)


# ### Joining DataFrames
# * Inner Join  - Concatenation of common columns ie intersection of two dataframes
# * concat is like outer join
# * Using append() Function

# In[20]:


print(" Inner Join on dataframes : \n", pd.concat([df1, df2], join = 'inner')) #no overlapping columns


# In[ ]:


#exercise
df3 = pd.DataFrame({'B' : ['ball', 'box' , 'band'], 'C': ['cat', 'calendar', 'cone'],'G' : ['grain', 'grape', 'goat']} ,
                   index =[ 1, 4, 2])
print("Data Frame 1 : \n", df1, "Data Frame 3 : \n", df3)
print(" Joining Data frmes:  \n" , pd.concat([df1, df3]))   #stacking one below another
print(" Joining Data frmes along axis = 1:  \n" , pd.concat([df1, df3], axis = 1))


# In[22]:


print(" Inner Join on dataframes : \n", pd.concat([df1, df3], join = 'inner'))


# #### The append() 
# * the append() method in Pandas does not modify the original object—instead, it creates a new object with the combined data
# * not very efficient method as a new index and data buffer is created

# In[95]:


print(df1)
print(df2)
print(df1.append(df2))    # append is same as concat stocks dataframes one below another
print(df1)       # Original DataFrames are not update
print(df2)         # a new ccatenated dataframe is created


# ### Merge Operations
# * Pandas has join operations identical to SQL
# * pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True)
# * left, right- dataframes, One of 'left', 'right', 'outer', 'inner
# * on - Column to join, default is common column, left_on- column in left dataframe to use as keys
# * left_index- True means use left dataframe index as join key, sort - True Sort result by joining Keys

# In[96]:


df_stud = pd.DataFrame({'St_id': [101,102,103,104,105],'Branch': ['IT','CS','ECE','CS','Mech']})
df_fac = pd.DataFrame({'F_id' : [110,120,130,140,150 ],'F_name' : ['A', 'B', 'C', 'D', 'E'],'Branch': ['ECE','Mech', 'EEE', "IT", 'CS'] })
print("Student dataframe: \n", df_stud,'\nFaculty Dataframe :\n', df_fac)
df_merge = pd.merge(df_stud, df_fac)
print("Merged dataframe : \n ", df_merge)   #Merge on a common column
#works only if both dataframes have the specified column Default is inner
#print("Merged dataframe : \n ", pd.merge(df_stud, df_fac, on = 'Branch') )


# * When similar columns have different names in different dataframes

# In[5]:


df_fac1 = pd.DataFrame({'F_name' : ['A', 'B', 'C', 'D', 'E'],'Stream': ['ECE','Mech', 'EEE', "IT", 'CS'] })
print("Student Details : \n", df_stud, 'Faculty Details: \n', df_fac)
print("Merged Dataframes : \n", pd.merge(df_stud, df_fac1, left_on = 'Branch', right_on = 'Stream'))
print("Student Details : \n", df_stud, 'Faculty Details: \n', df_fac)


# In[105]:


# the redundant column can also be dropped
pd.merge(df_stud, df_fac, left_on = 'Branch', right_on = 'Stream').drop('Stream', axis = 1)


# # Merge over indices
#  * left_index and right_index flags can be used to perform merge over the similar index of the dataframes.
#  * Also, join( ) method performs the merge by default on indices

# In[6]:


#print('\n Using merge on indices: \n',pd.merge(df_stud, df_fac, left_index=True, right_index=True))
#print('\n Using join( ): \n', df_stud.join(df_fac))
#If we use default index branch is repeated. better way is to set the common column as index

df1 = df_stud.set_index('Branch')
df2 = df_fac1.set_index('Stream')
print("Student Details : \n", df1, 'Faculty Details: \n', df2)
print('\nUsing merge on indices: \n',pd.merge(df1, df2, left_index=True, right_index=True))
print('\nUsing join( ): \n', df1.join(df2))
#DataFrame has a convenient join method for merging by index


# In[ ]:


#### Different types of joins can also be specified like 'inner' , 'outer', 'left' and 'right' using how keyword


# In[98]:


# to see the effect of outer Join which is like Union we need to add different elements to Branch
df_stud = pd.DataFrame({'St_id': [101,102,103,104,105,106],'Branch': ['IT','CS','ECE','CS','Mech', ' EEE']})
df_fac = pd.DataFrame({'F_id' : [120,130,140,150 ],'F_name' : ['B', 'C', 'D', 'E'],'Branch': ['Mech', 'EEE', "IT", 'CS'] })
print("Student dataframe: \n", df_stud,'\nFaculty Dataframe :\n', df_fac)

df_merge = pd.merge(df_stud, df_fac, on = 'Branch', how='right')
print("Merged dataframe : \n ", df_merge)   #Merge on a common column


# #### One-to-one join
# * uses a common column as the key to join the dataframe.
# * the order of values in each column in not necessarily maintained

# In[99]:


df1 = pd. DataFrame({'key' :['b', 'a', 'd','e'], 'data1': range(4)}) #has unique  rows labels
df2 =pd. DataFrame({'key' :['a', 'b', 'd'], 'data2': range(3)})   # has unique row labels
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of one  to one merge situation
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))     # intersection of keys 
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))     # union of keys
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))     #  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# ##### Many-to-one joins
# - one of the two key columns contains duplicate entries.
# - the merged DataFrame preserves the duplicate entries.

# In[100]:


df1 =pd. DataFrame({'key' :['b', 'b', 'a', 'c', 'a', 'a'], 'data1': range(6)}) #has multiple rows labelled a and b
df2 = pd. DataFrame({'key' :['a', 'b', 'd'], 'data2': range(3)})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to one merge situation
#No of rows will be 5X2 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))     # intersection of keys 
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))     # union of keys
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))     #  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# ##### Many-to-many join
# * when the key column in both the left and right array contins duplicates

# In[101]:


df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a', 'b'], 'data1': range(7)})  #has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to one merge situation
#No of rows in the dataframe = 7x4 for inner
#No of rows will be 5X2 
print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))     # intersection of keys 
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))     # union of keys
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))     #  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[5]:


df1 =pd. DataFrame({'key' :['b', 'b', 'a', 'c', 'a', 'a'], 'data1': range(6)}) #has multiple rows labelled a and b
df2 = pd. DataFrame({'key' :['a', 'b', 'd'], 'data2': range(3)})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to one merge situation
#No of rows will be 5X2 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))     # intersection of keys 
print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))     # union of keys
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))     #  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[6]:


f1 =pd. DataFrame({'key' :['b', 'b', 'a', 'c', 'a', 'a'], 'data1': range(6)}) #has multiple rows labelled a and b
df2 = pd. DataFrame({'key' :['a', 'b', 'd'], 'data2': range(3)})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to one merge situation
#No of rows will be 5X2 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))     # intersection of keys 
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))     # union of keys
print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))     #  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[7]:


f1 =pd. DataFrame({'key' :['b', 'b', 'a', 'c', 'a', 'a'], 'data1': range(6)}) #has multiple rows labelled a and b
df2 = pd. DataFrame({'key' :['a', 'b', 'd'], 'data2': range(3)})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to one merge situation
#No of rows will be 5X2 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))     # intersection of keys 
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))     # union of keys
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))     #  keys from left dataframe
print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[102]:


series = pd.Series([2,3,4,5])
print(series[2])
series[2]=7.8
print(series[2])
print(series)


# ### pandas.merge connects rows in DataFrames based on one or more keys. This
# * will be familiar to users of SQL or other relational databases, as it implements database join operations
# * left LEFT OUTER JOIN	Use keys from left object
# * right	RIGHT OUTER JOIN	Use keys from right object
# * outer	FULL OUTER JOIN	Use union of keys
# * inner	INNER JOIN	Use intersection of keys
# 
# • pandas.concat concatenates or “stacks” together objects along an axis.### The merge method() is equivalent to the SQL join
dir( String)
# In[9]:


dir(Series)


# In[104]:


### Difference beytween axis =0 and axis =1
#Dataframe aggregation methods ignore nan values and find the sum
data = pd.DataFrame([[1,  4,  2],    
                   [2,   3, 5],     
                   [7,  4,  6]])  
print(data)
print(data.sum())    #sum by default is column sum axis =0  columnwise sum
print(data.sum(axis=1))   #roqwwise sum


# In[ ]:





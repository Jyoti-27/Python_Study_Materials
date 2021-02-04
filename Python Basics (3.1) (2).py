#!/usr/bin/env python
# coding: utf-8

# # Advanced Certification in AIML
# ## A Program by Datafolkz
# ### Introduction to Python
# 
# # Intro to Jupyter Notebook 
# 
# - SHIFT + ENTER for EXECuting the CELL using Jupyter noteboook
# 
# Shortcuts in both modes:
# - Shift + Enter run the current cell, select below
# - Ctrl + Enter run selected cells
# Alt + Enter run the current cell, insert below
# Ctrl + S save and checkpoint

# In[1]:


print('Hello World')


# In[2]:


a = 15
print(a)
b = 20
print(b)


# - esc + m for code to markdown
#  
# - esc + y for markdown to code 

# ## Julia , Python and R can be done using JupyterR

# About Python
# - Python is a scripting langugae
# - Its  case sensitive 
# - Its object oriented language
# 
# Python program is first compiled and then interpreted. The compilation part is hidden from the programmer thus, many programmers believe that it is an interpreted language. The compilation part is done first when we execute our code and this will generate byte code and internally this byte code gets converted by the python virtual machine(p.v.m) according to the underlying platform(machine+operating system).
# 
# An interpreter translates high-level instructions into an intermediate form, which it then executes. In contrast, a compiler translates high-level instructions directly into machine language. Compiled programs generally run faster than interpreted programs. The advantage of an interpreter, however, is that it does not need to go through the compilation stage during which machine instructions are generated. This process can be time-consuming if the program is long. The interpreter, on the other hand, can immediately execute high-level program

# ## Lexical Structure
# 
# The lexical structure of a programming language is the set of basic rules 
# that govern how you write programs in that language.
# 
# It is the lowest-level syntax of the language and specifies such things 
# as what variable names look like and which characters denote comments. 
# 
# Each Python source file, like any other text file, is a sequence of characters. 
# 
# You can also usefully consider it as a sequence of lines, tokens, or statements. 
# 
# These different lexical views complement and reinforce each other. 
# 
# Python is very particular about program layout,especially with regard to lines and indentation, 
# so you’ll want to pay attention to this information if you are coming to Python from another language.

# ## Lines and Indentation
# •	A Python program is composed of a sequence of logical lines, each made up of one or more physical lines. Each physical line may end with a comment. 
# A hash sign (#) that is not inside a string literal begins a comment. 
# 
# •	All characters after the # and up to the physical line end are part of the comment, and the Python interpreter ignores them. 
# 
# •	A line containing only whitespace, possibly with a comment, is known as a blank line, and Python totally ignores it. 
# 
# •	In an interactive interpreter session, you must enter an empty physical line (without any whitespace or comment) to terminate a multiline statement.

# •	However, Python automatically joins adjacent physical lines into one logical line if an open parenthesis ((), bracket ([), or brace ({) has not yet been closed, and taking advantage of this mechanism, generally produces more readable code instead of explicitly inserting backslashes at physical line ends.
#                                                                                                                                           
# •	Triple-quoted string literals can also span physical lines. Physical lines after the first one in a logical line are known as continuation lines. 
# 

# ## Indentation
# •	The indentation issues covered next do not apply to continuation lines but only to the first physical line of each logical line.
# 
# •	Python uses indentation to express the block structure of a program. Unlike other languages, Python does not use braces, or other begin/end delimiters, around blocks of statements; indentation is the only way to denote such blocks.
# 
# •	Each logical line in a Python program is indented by the whitespace on its left. A block is a contiguous sequence of logical lines, all indented by the same amount; a logical line with less indentation ends the block. 
# 
# •	All statements in a block must have the same indentation, as must all clauses in a compound statement.
# 
# •	The first statement in a source file must have no indentation (i.e., must not begin with any whitespace).
# 
# •	Statements that you type at the interactive interpreter primary prompt >>> (covered in Interactive Sessions) must also have no indentation.
# 

# ## Tokens
# 
# •	Python breaks each logical line into a sequence of elementary lexical components known as tokens. Each token corresponds to a substring of the logical line. 
# 
# •	The normal token types are identifiers, keywords, operators, delimiters, and literals, as covered in the following sections.
# 
# •	You may freely use whitespace between tokens to separate them. Some whitespace separation is necessary between logically adjacent identifiers or keywords; otherwise, Python would parse them as a single, longer identifier. 
#  For example, printx is a single identifier; to write the keyword print followed by the identifier x, you need to insert some whitespace (e.g., print x).
# 

# ## Identifiers
# 
# •	An identifier is a name used to identify a variable, function, class, module, or other object. An identifier starts with a letter (A to Z or a to z) or an underscore (_) followed by zero or more letters, underscores, and digits (0 to 9).
# 
# •	Case is significant in Python: lowercase and uppercase letters are distinct. Python does not allow punctuation characters such as @, $, and % within identifiers.
#     
# •	Normal Python style is to start class names with an uppercase letter and all other identifiers with a lowercase letter. 
# 
# •	Starting an identifier with a single leading underscore indicates by convention that the identifier is meant to be private. 
# 
# •	Starting an identifier with two leading underscores indicates a strongly private identifier; if the identifier also ends with two trailing underscores, the identifier is a language-defined special name. 
# 
# •	The identifier _ (a single underscore) is special in interactive interpreter sessions: the interpreter binds _ to the result of the last expression statement it has evaluated interactively, if any.
# 

# In[4]:


a = 15 
print(A)


# In[5]:


a1 = 25
print(a1)


# In[7]:


1a = 30


# In[11]:


a_1 = 50
print(a_1)


# In[13]:


_a = 40
print(_a)


# ## Keywords
# 
# Keywords are the reserved words in Python.
# 
# We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language.
# 
# In Python, keywords are case sensitive.
# 
# There are 33 keywords in Python 3.7. This number can vary slightly over the course of time.
# 
# All the keywords except True, False and None are in lowercase and they must be written as they are. 
# 
# The list of all the keywords is given below.
# 
# ![image.png](attachment:image.png)
# 

# ## Operators
# 
# Python uses non alphanumeric characters and character combinations as operators. 
# 
# Python divides the operators in the following groups:
#     
# 
# - Arithmetic operators
# - Assignment operators
# - Comparison operators
# - Logical operators
# - Identity operators
# - Membership operators
# - Bitwise operators
# 
# 

# ## Delimiter
# - **Used for grouping, punctuations and assignments**
# - (), [], {}
# - , : . ' = ;
# - += -= *= /= //= %=
# - &= |= ^= >>= <<= **=

# ## Literals
# 
# A literal is a number or string that appears directly in a program.
# 
# The following are all literals in Python:
#     
# - Integer literal 42
# - Floating-point literal 3.14                       
# - Imaginary literal 1.0j                       
# - String literal  'hello'                    
# - Another string literal "world"                   
# - Triple-quoted string literal """Good night"""           
# 

# ## Identifier/Variable
# 
# Which stores a value
# 
# - It is a sequence of characters that consists of letters, digits and  underscore
# - Can be of any length
# - Can starts with a letter which can be either lower or upper case
# - Can start with an underscore '_'
# - Can start with a digit
# - Cannot be a keyword.

# # Why Statistics is required for Analytics?
# 
# Without statistics, the interpretation of data can quickly become massively
# flawed. 
# Take, for example, the estimated number of German tanks produced during
# World War II, also known as the “German Tank Problem.” The estimate of the
# number of German tanks produced per month from standard intelligence data was
# 1,550; however, the statistical estimate based on the number of tanks observed
# was 327, which was very close to the actual production number of 342

# Similarly, using the wrong tests can also lead to erroneous results.
# 
# In general, statistics will help to
# 
# • Clarify the question.
# 
# • Identify the variable and the measure of that variable that will answer that
# question.
# 
# • Determine the required sample size.
# 
# • Describe variation.
# 
# • Make quantitative statements about estimated parameters.
# 
# • Make predictions based on your data.

# In[8]:


a1 = 10
print(a1)
a1


# ## Scalar Data Types and Operations
# 
# Python has four scalar data types:
# 
# - Integer
# - Float
# - Boolean
# - Complex
# 
# We will review these in this notebook

# ## Integers
# 
# The usual arithmetic operators are available: + for addition, - for subtraction and * for multiplication.

# In[14]:


print(2 + 4)
print(12878 + 1)
print(7 - 3)
print(127 - 128)
print(8 * 6)
print(17 * 12)


# There are two division operators:
#     / for everyday (float) division and // for truncating (integer) division

# In[15]:


print(19 / 4)
print(19 // 4)


# The modulo operator % and the exponentiation operator ** are also available.

# In[16]:


print(18 % 3)
print(72 % 5)


# In[18]:


2**10


# In[20]:


3**4


# In[21]:


2^4


# The usual operator precedence rules and use of parentheses to override that are available

# In[23]:


print(10 ** 2 * 7 - 3)
print(10 ** (2 * 7) - 3)
print(10 ** (2 * 7 - 3))


# In[13]:


a = 123456789 
b = a ** 2
c = b ** 3
d = c ** 4
e = d ** 5
print(e)


# ##### Assignment operators
# The standard assignment operators are available. That is,  $\alpha$  $\odot=\beta$ is a shorthand for $\alpha = \alpha \odot \beta$
# where $\odot$ is any binary arithmetic operator we saw above

# In[25]:


a = 12
b = 5
a += b
print(a, b)
a -= b
print(a, b)
a *= b
print(a, b)
a **=b
print(a,b)


# #### Boolean
# The two constants True and False are defined.
# 
# The usual boolean operators are also available: ==, !=, >, >=, <, <= 

# In[15]:


a = 12
b = 13
print(a == b - 1,a == b, a != b, a < b, a >= b)


# #### Float
# Python has a float datatype (and it is the same as C's double!) and the above operations are available

# In[17]:


a = 12.9
b = 3.6
c = a + b
d = a - b
e = a * b #Watch out for the round off error!
f = a / b
print(a, b, c, d, e, f, sep="\n")
print(a, b, c, d, e, f)


# ## Complex
# 
# Complex numbers are built-in

# In[29]:


z = 3 - 4j
print(z, z.real, z.imag, abs(z), sep="\n")


# In[28]:


x = 5 + 12j


# In[30]:


print(z + x, z - x, z * x, x / z, sep="\n")


# #### Variables
# We have been using variables already. Python variable naming rules are simple and similar to all major programming languages
#  * must start with a letter
#  * can have letters, numbers and underscore
#  * case sensitive
# 
# *Note that we need not declare variables but using an undefined variable is an error*

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Interview Python questions:**

## 1. Features of Python:

a) Easy, simple, fast  
b) Open source, interpreted language thus easy to debug  
c) Can be integrated with c, c++ or other programming languages  
d) Object oriented programming (can perform the tasks which resembles to the real world entity)  

## 2. Reserved keywords in python?

a) Cannot be used for purpose use  
b) They are known to the interpreter  
c) There are 33 keywords comes with new version of python  
d) examples: false, true, if, elseif, else, break

## 3. Literals in python?

a) The value or data which is given to the variables or the constant
b) There are of four types:
1. String literals: set of characters
2. Numeric literals: Integer, Floating numbers and complex numbers
3. Boolean: True or false
4. Special literals: NONE in python

## 4. How to concentenate two tuples?
tuple:
 1. Immutable variable which stores the data, cannot be edited
 2. They are fast
 3. Representation: t = ('a', 10, "khushi")
 
### example:

>t1=(10,20,56)  
t2=(23,45,12)

>print(t1+t2);  
output: (10,20,56,23,45,12)

## 5. Functions in python

1. Piece of code perform single and related events 
2. used for multiple times at any location to enhance the code resuability by calling it
3. Any No of arguments can be passed
4. Two types: Build in and User defined:
   1. Build in: Print()
   2. Def printing():  
>print("Hello Sofia")

## 6. How do you intilize a 5*5 numpy array with only zeroes?

### Numpy: 
Numerical python deals with arrays and matrices, helps in linear algebra, fourier transform and other mathematical calculations

>import numpy as np

>n1 = np.zeros((5,5))  

output: All elements intialized with zero

## 7. What is pandas?
Open source library, lots of functions, and data structures, used for analysis, cleaning, deriving, retrieving data
Two fantastic data structures: series and dataframes
Pandas : panel data or python data analysis

## 8. What is dataframes?
1. Used for storing data, different type of data can be stored thus hetrogeneous
2. Mutable thus can be edited
3. Present in pandas library
4. Can stored data from the csv file with the help of pd.csv_read("name of the file")

example: import pandas as pd
df= pd.read_csv("data1.csv);
df.head() gives five rows by default
df.head(12) gives 12 rows

## 9. What are Pandas series?

1. Data structure in pandas
2. Use for single dimension data

### example:
>import pandas as pd  
d = ['a', 23, 57.3, "khushi"]  
series= pd.Series(data)  
print(series)  
print(type(series))

## 10. Group by function in pandas

1. used for making the groups of same data according to the condition
2. Grouping of data together helps in getting the information related to the field

### example

>import pandas as pd

>df= pd.DataFrame({
'Vehicle': ['Lamborghini', 'Fortuner', 'Kia'], 'Type':['car', 'car', 'motorcycle']})  
print(df)  
df.groupby('Type').count()

## 11. How to create a dataframe from lists?
Yes, we can create dataframe from lists

### example: 
>import pandas as pd
ls1 = [23,34,12,11]  
ls2= ["khushi", "agarwal"]  
df["list1"]=ls1;  
df["list2]=ls2;

## 12. How to create dataframe from a dictionary?

>import pandas as pd
df= pd.DataFrame()  
a= [1,2,3,4]  
b=[23,34,45,56]  
d= {"cars":a, "bikes":b}  
df= pd.DataFrame(d)  
print(df)


## 13. How to combine DataFrames using join function?
1. used to join two or more dataframes together when one or columns are common
2. Stacking is always done in horizontal manner
3. Pandas supports left join, right join, inner join and outer join


## 14. Which method works best for vertical stacking of data frames?

vstack() is used in the case of numpy while concat() is use for vertical stacking in the case of dataframes

## 15. How to merge DataFrames in pandas?

1. Depends on the type and fields of different data frames
2. Data having similar fields merge along axis 0
3. Data having different type or fields merge along axis 1

## 16. Given a dataframe, how do you drop all rows having NaN?

By using inbuild function in pandas ie, dropna() function

## 17. How to access the first five and last five entries of a data frame?

>df.head()  
df.tail()

## 18. How to access data from a DataFrame using a value as index

### example: 
>import pandas as pd
df= pd.DataFrame()

ls1= ["a","b","c","d]  
ls2= ["12","13","34","80"]

df["cars"]=ls1;  
df["bikes"]=ls2;

a= [0,1,2,3]  
df.index=a  
df.loc[0]

## 19. How to do single line comment and multi line comment?

#single line comment  
"""

"""   
Multi line comment

## 20. What is the memory-efficient way to add elements to a tuple?

Tuples are immutable datatypes in python
You cannot add elements to an existing tuple
Tuples are immutable datatypes in python
A new one must be created if the values are to be changed!

## 21. What is dictionary?

1.Collection of items in no particular order
2.Keys and values
example: d={"a":1,"b":2}

## 22. 














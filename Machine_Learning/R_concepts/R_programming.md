# R- Programming Concepts

## 1. Basic Commmands:

* For Assignment:
> a <- 20  
  b <- 23

* For printing into the console:
> print(a)  
  print(b)

* For storing multiple values in a variable:
> a <-c(1,2,3,4,5)  
 *where c is the concentenation function*

* For storing continous values in a variable:
> a <- (1:10)
*stores value from 1 to 10*

* For adding the values of two arrays
> a <- b<- (1:20)   
Assign the value in both the variables from 1 to 20  
a+b-->> Add the values together like [2 4 6....] and gives the output

* For multiplication of the values together in the variable of other two variables:
> z <- a*b  
a*b-->> Multiply the values together like [1 4 9 ....] and stores in the Z

* For Commenting in R programming:  
Use # tag 

* For listing all the variables present in the workspace:
>ls()

* For removing the variable :
> rm (X)   
*where X is the name of the variable*

* For removing all the variables:
> rm (list= ls())

## 2. Packages

* browseURL('Url') --> Use to browse the URL and open the URL in new tab

* install.packages('package_name')

Example:
> install.packages('package_name')
* LiblineaR is a package which used to analysis the linear progression models

* Load packages in the program:
> require('package_name')

* Detach package from the program:
> detach(package:'package_name', unload=TRUE)

* Remove or uninstall package
> remove('package_name')

## 3. Data Stored for Analysis using R:

Three ways to store the data for analysis 
* With the help of data variables and create own data tables
* With the prebuilt datasets that comes with R libraries
* With the csv files

### 1. Prebuilt Datasets

> library(help ="datasets")
data()

Iris is one of the dataset which consist of properties of flowers such as petal length, petal width, sepal length and sepal width

* For displaying all the rows of the iris dataset
> iris

* For displaying the structure of the iris
> str(iris)

* For loading it into the workspace
> data("iris")

### 2. Manual
> x <- (1:30) *where including 30 as well*  
> x <- c(23,56,2,3)  
> x <- seq(0,20, by=5) *where by is the stepsize including 20 as well*  
> y <- scan()   *where it takes input from the console until we hit enter two times*

### 3. With the help of Csv files or text files

Text files are nothing but tab seperated files

> customer <- read.csv('path',header=TRUE)
> products <- read.table('path',header=TRUE, sep='\t') 

In order to view the customer table in tabular format

>   View(customer)

## 4. Barplots

* To find the frequency distribution of one column
> y <- table(customer$Region)

* To plot the graph

> barplot(y[order(y)])

1. To change the orientation:  
 Properties of bar plot
#### Arranging in increasing order
> barplot(y[order(y)])

#### Arranging in decreasing order
> barplot(y[order(-y)])

#### #To change the orientation of the graph  
>barplot(y[order(y)],horiz=TRUE)

#### To change the color of the graph  
>barplot(y[order(y)],horiz = TRUE, col="Red")


#### To change the color of each plot
>barplot(y[order(y)],horiz = TRUE, col= c("Red", "blue", "pink", "green"))

#### To remove the border
>barplot(y[order(y)], horiz = TRUE, col= c("red", "blue", "pink","green"), border='NA')

#### To give the title
>barplot(y[order(y)], horiz = TRUE, col= c("red", "blue", "pink","green"), border='NA', main="The Frequency of Region")

#### To give the x axis title  
>barplot(y[order(y)], horiz = TRUE, col= c("red", "blue", "pink","green"), border='NA', xlab ="No of Customers" )

#### Export the data into the image format  

>png(filename = "C:/Users/Khushi/OneDrive/Desktop/python/Machine_Learning/R_concepts/barplot.png")  
barplot(y[order(y)], col="pink", main="The Frequency distribution through region", xlab="No of Customers")  
dev.off() --> Needs to be off this!

## 5. Histograms

### Histograms
### Used for finding frequency within the range
>hist(customer$Age)

### For showing only 5 bars
>hist(customer$Age, breaks = 5)






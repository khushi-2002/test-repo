# Ways to import the data

# 1. By using the predefined datasets

# For getting all the datasets present in the package
data()

# Alternate way to do the same
library(help="datasets")

# Structure of iris dataset
str(iris)

# Load into the workspace for analysis
data("iris")

# For displaying the data present in the iris dataset
iris

# To know about the dataset iris
? iris

# 2. By manual adding the data

x <- (1:10)
y <- c(1,2,4,56,7)
z <- seq(0,20, by=5)

#For taking input from the console
a <- scan()

#3. With the help of CSV files and text files

product <- read.table('C:/Users/Khushi/OneDrive/Desktop/python/Machine_Learning/Data Files/1. ST Academy - Crash course and Regression files/Product.txt', header = TRUE, sep = '\t')


customer <- read.csv('C:/Users/Khushi/OneDrive/Desktop/python/Machine_Learning/Data Files/1. ST Academy - Crash course and Regression files/Customer.csv', header = TRUE)

#For finding the structure of the products
str(product)

# For printing the customer table
customer

# For printing the customer view table
View(customer)

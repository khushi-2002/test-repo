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

# Creation of frequency distribution 
#For fetching records and grouping together by column (frequency distribution in region)
y <- table(customer$Region)

# Printing into the console
y

# Showing result in tabular form
View(y)

# frequency distribution can be converted into the barplot

barplot(y)

# Properties of bar plot
# Arranging in increasing order
barplot(y[order(y)])

# Arranging in decreasing order
barplot(y[order(-y)])

#To change the orientation of the graph
barplot(y[order(y)],horiz=TRUE)

# To change the color of the graph
barplot(y[order(y)],horiz = TRUE, col="Red")


# To change the color of each plot
barplot(y[order(y)],horiz = TRUE, col= c("Red", "blue", "pink", "green"))

# To remove the border
barplot(y[order(y)], horiz = TRUE, col= c("red", "blue", "pink","green"), border='NA')

# To give the title
barplot(y[order(y)], horiz = TRUE, col= c("red", "blue", "pink","green"), border='NA', main="The Frequency of Region")

# To give the x axis title
barplot(y[order(y)], horiz = TRUE, col= c("red", "blue", "pink","green"), border='NA', xlab ="No of Customers" )

# Export the data into the image format

png(filename = "C:/Users/Khushi/OneDrive/Desktop/python/Machine_Learning/R_concepts/barplot.png")
barplot(y[order(y)], col="pink", main="The Frequency distribution through region", xlab="No of Customers")
dev.off()


# Histograms
# Used for finding frequency within the range
hist(customer$Age)

# For showing only 5 bars
hist(customer$Age, breaks = 5)

# For defining the range of the plot
hist(customer$Age, breaks = c(0,20,40,60,80), col="red", freq = TRUE, main="Histogram")






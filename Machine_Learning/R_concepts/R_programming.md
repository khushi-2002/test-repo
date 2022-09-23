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
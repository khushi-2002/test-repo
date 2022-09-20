# Day-4:


Random function:

---

The function which produces random numbers b/w the range
Example: import random-- > Python module : Piece of the code which can be used to use it in our programs
random_number = random.randint(100,200): Random numbers between 100 and 200 including both


For Floating point numbers:
random_float = random.random()--> Not including 1, thus [0,1)

For producing random numbers between 0 and 5:
random_float = random.random()*5 : But not including 5

Lists:
The list have an order and same group can be listed together.
Example: a= ["Khushi", "XYZ", "ABC"]

Accessing the elements from the list:
print(a[0])-->Khushi

Positive index: a[0]
Negative index: a[-1]

Lists are mutable, they can be edited or can add items 

1. a.append("Any_name"): Add items at the end
2. a.extend(["XYZ1", "XCYT"]): add lists to the end

Split method:

p= "Hello,Khushi,Your,name,is,good"
print(p.split(,))

Choose random name from the list:

print(random.choice(name_of_the_list)

Nested Lists:

fruits= ["Apple", "Banana", "Orange", "Pineapple"]
vegetables= ["Potato", "Brinjal", "Lady Finger"]

dirty_dorzon = [fruits, vegetables]

print(dirty_dorzon) : Nested list


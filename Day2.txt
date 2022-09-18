Day 2:

Data types: 
a) Primitive Data type in Python:

1. String : sequence of characters
Example: print ("Hello"[0]) pulling out the character from the string called subscripting

2. Integer
Example: print(123+234)

Note: Example: 23,00,000
In python we can write it in our program by adding underscore _ example: 23_00_000 (FOR READABILITY)

3. Float
Example: print(23.45+12.34)

4. Boolean
Example: print(true)--> true
print(false)-->false

Len() function don't work for integer data type

Note: We cannot use concentenation of integer with strings
Example: num_length= len(input("Enter your name"))
print("Your name having"+num_length+" Characters")

For finding the Data type :
type(num_length)

For concentenation:
Convert the integer into string data type and then use it in the print statement

Example: Num_length= len(input("Enter your name"))
new_Num_length = str(Num_length)
print("Your name has "+new_Num_length+" characters")


Type conversion:

a= str(123)
b= int("12")
c= float("23.56")

Example: print(str(123)+str(456))---> 123456
print(int("12")+float("45.67"))--> 57.67
print(12+float(34.67))--> 46.67
print(str(234)+89)-->Error (cannot concentenate integer with string)


Mathematical operators in Python:

+
-
*
/--> Always gives flating point result
**

Precedence:
PEMDAS

P-Parantheses
E- Exponent
M- Multiplication
D- Division
S- String

Associtivity:
Left to right

Example: 3*3+3/3-3
Output= 7.0

round function:

print(round(2.66666))--> 3
print(round(2.6666,2))--> 2.67

Floor division:

print(a//b) gives the integer result

fstring: used to concentenate the string with other data types
example: a=23
b=2.67
c=true

print(f"The values are {a}, {b}, {c})

Alternative way of round the number to certain decimal points

final_amount = "{:.2f}.format(final_amount)
print(final_amount)



































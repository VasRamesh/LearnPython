from math import *
import Methods

print("Hello World")

str_Name = "John"
int_Number = 4
float_Number = 3.0
bool_YN = 1 > 2
print(bool_YN)

# String Concatenation and literal Characters
print("\n")
print(str_Name + " is a \" loser \" ")

# String is an array of characters: can grab an individual index (Starts from 0)
print(str_Name[2])  # should be 'h'

# Passing a parameter
print(str_Name.index("J"))  # returns the index where char J is located (or starts)
print(str_Name.index("hn"))  # should return 2 (error if not found)

# Replace chars in str
new_string = str_Name.replace("John", "Bob")
print(new_string)  # should return Bob

# Python knows PEMDAS
print("NUMBERS")
print(4 + 2 * 8)
# % Modulus operator returns the remainder // VERY IMPORTANT
print(39 % 2)

# Python only prints out strings together; use str() to convert num to str
num_fav = -7
print(str(num_fav) + " is my fav number")

# Absolute Value Method
abs_num_fav = abs(num_fav)
print(abs_num_fav)

# ** Exponential operator
print(abs_num_fav ** 3)

# Max and min function
print(max(abs_num_fav, num_fav))
print(min(0, 3))

# Round & floor & ceil function
print("ROUNDING")
ex_float = 4.6
print(round(ex_float))
print(floor(ex_float))
print(ceil(ex_float))
print(sqrt(ex_float))

# USER INPUT and OUTPUT
name = input("Please enter your name: ")  # string by default
print("Hi " + name + "!")
age = int(input("Enter your age: "))  # int() / str() / bool() / float() = convert into other data types
new_age = age + 5
print("In 5 years, you will be " + str(new_age) + " years old!")

# Importing files and using external methods <-- Modules
Methods.say_hi("Bob")

# Inheritance in Python - copy classes that are similar (Expert Chef vs General Chef)
# Class ChineseChef(Chef)  # The ChineseChef class will inherit the Chef methods



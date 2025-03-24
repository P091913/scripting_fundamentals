# this is a comment in Python

# Data Types In Python
# String - Any values encased in double quotes or single quotes
# my_string and my_string2 are variables. They're references in
# memory so that we can access the data held within
my_string = "This is a string using double quotes"
my_string2 = 'This is a string using single quotes'
print(my_string)
# display data type tied to my variable
print(type(my_string))

# Int
my_int = 55
print(type(my_int))

# datatype of my_string2 is a string
print(type(my_string2))
# change the value to an integer
my_string2 = 80
# datatype is now a class of int
print(type(my_string2))

# Floats
my_float = 5.33
print(type(my_float))

# example of grabbing user input
# all user input comes in a string value
i_input = int(input("Enter a number "))
print(type(i_input))

# cast typing/ casting
# answer = int(i_input) * 5
answer = i_input * 5
print(type(i_input))

# print will display to the user whatever you're printing
print(answer)
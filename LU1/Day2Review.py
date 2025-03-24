# float - number followed by a decimal
var1 = 25.66

# int = whole number
var2 = 25

# string - any character
# can be encased in single or double quotes
var3 = 'StringValue123'
var4 = "StringValue123"

# concatenation using +
print("This is the value of Var3: " + var3)

# concatenation using f-strings
print(f"This is the value of var3: {var3}")

# retrieve the datatype tied to a variable
print(type(var3))

# grabbing user input and displaying it out to the console
#hold_value = input("Give me a value to continue: ")
#print(f"The value you entered was {hold_value}")

# math operators (+, -, *, /)
# + add
print(5 + 5)

# - subtract
print(5 - 5)

# * - multiply
print(5 * 5)

# / - divide - will always bring back a float value as your answer
print(10 / 6)

# // - floor division - will always bring back a int/whole number
print (10 // 6)
# same as division, take my answer and cast it to an int datatype
# ans = int(10 / 6)

# % - modulus - division - it will the remainder
print(10 % 6)

# isdigit()
# isalpha()
# isnumeric()
# custom function for testing isfloat() because isfloat is not a built in function

str_input = input("Enter a value (numbers 0-9): ")

# test what the user has entered to see if every character is a 0-9
# "23432" - True
# "sadfdas" - False
# "23.534" - False
print(str_input.isdigit())


# Custom Function for testing isfloat()
# parameter value
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

float_input = input("Enter a decimal value (ex: 23.54): ")
# argument - float_input
print(isfloat(float_input))




# "342" - False
# "sdfasdf" - True
# "dsf34" - False
alpha_input = input("Enter a value containing only letters: ")
print(alpha_input.isalpha())


# test whole numbers
# unicode characters
# will not return true if values are not whole numbers (ex: .,- will return False)
numeric_input = input("Enter a value containing only numbers: ")
print(numeric_input.isnumeric())

numeral_input = input("Enter in a roman numeral: ").upper()
roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


if numeral_input in roman_numerals:
    print(True)
else:
    print(False)


def roman_numeral(value):
    if numeral_input in roman_numerals:
        return True
    else:
        return False

print(roman_numeral(numeral_input))

filler_var = "adf"
filler_var2 = 'ADF'
# returns to the true/false if the string referenced is all uppercase or all lowercase
print(filler_var.islower())
print(filler_var2.isupper())



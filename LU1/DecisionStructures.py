# Jarrett
# Feb, 27
# This program will showcase the use of decision structures


# grab user input
# ask the user to give me two numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# check if the first number is higher than the second number
# when doing a comparison, the end result is either true or false
if num1 > num2:
    print("The first number is larger")
else:
    print("The second number is larger")


# setup - ask the user to give me a grade percentage
# ask them if the test has been graded
percent = float(input("Enter a percentage: "))
graded = input("Enter a yes/no: ")

if graded == 'yes':
    # boolean datatype
    graded = True
elif graded == 'no':
    # boolean datatype
    graded = False
else:
    print("Invalid entry for graded, restart and try again")

# these statements do the same thing, just worded differently
#if graded == True:
# adding datatype, doesn't enforce the datatype to the variable
letter_grade: str
if graded:
    if percent >= 90:
        print("A")
        letter_grade = "A"
    # elif is a shortened version of the else: if: structure
    elif percent >= 80:
        print("B")
        letter_grade = "B"
    elif percent >= 70:
        print("C")
        letter_grade = "C"
    # catch all statement
    else:
        print("You'll do better next time")


# if graded:
#    if percent >= 90:
#        print("Letter Grade of A")
#    else:
#        if percent >= 80:
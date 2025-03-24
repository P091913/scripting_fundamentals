# this script, I'm just going grab user data
# validate against checking if it's empty
# check if's a specific data types
# check if it's None

# username = input("Enter your username: ")
# checking to see if the user gave us at least 1 character
# that's not a space
# strip() - strips all spaces from left and right side
# rstrip() - strips all spaces from the right
# lstrip() - strips all the spaces from the left side
while True:
    username = input("Enter your username: ")
    if username.strip() == "":
        print("Invalid username, please try again.")
    else:
        print(username)
        break

while True:
    try:
        account_age = int(input("Enter the number of years you've had this account: "))
        break
    except ValueError:
        print("Please enter an integer")

# validate specific user entry data
while True:
    # a, b or c
    # convert user input before storing the value to lowercase
    user_entry = input("Input 'a', 'b', or 'c': ").lower()
    if user_entry == 'a' or user_entry == 'b' or user_entry == 'c':
        print("Valid Input")
        break
    else:
        print("Invalid Input, please enter 'a', 'b', or 'c'.")

# second way
valid_answers = ['A', 'B', 'C']
while True:
    user_entry = input("Enter 'a', 'b', or 'c': ").upper()
    # if value stored in user_entry string exists in our list, returns True, else returns False
    if user_entry in valid_answers:
        print("Valid Input")
        break
    else:
        print("Invalid Input")


while True:
    try:
        # ex: 56
        account_value = float(input("Enter the estimated account value: "))
        # account_value 56.0
        if account_value < 1000:
            print("Estimated account is too low, must be 1000 or greater")
        else:
            break
    except ValueError:
        print("Invalid value, enter in a number")

# YeS, YES, yes, yE
user_input = input("Do you have more value to enter (yes/no): ").lower()
if user_input == "yes":
    print("Cool")


# checking string without == ""
string_input = input("Type in a random value, not spaces")
if string_input:
    print("String contains a value")
else:
    print("String is empty")





# "" or None = Boolean context is False
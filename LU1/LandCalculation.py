# Jarrett
# Feb, 26
# This program will take square feet entered by the user
# and will calculate the amount of acres

# grab user input
sqft = float(input("Enter square footage: "))

# calculation for acres
c_acres = sqft / 43560

# f-string formatting
print(f"You are trying to buy {c_acres:.2f} acres")

# old concatenation formatting
print("You are trying to buy " + str(c_acres) + " acres")


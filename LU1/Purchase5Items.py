# The purpose of this program is to allow the user to enter the price of 5 items
# The program will calculate the subtotal, tax and final total
# The program will display the results to the user

item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
item4 = float(input("Enter the price of item 4: "))
item5 = float(input("Enter the price of item 5: "))

cSubtotal = item1 + item2 + item3 + item4 + item5
cTax = cSubtotal * .07


# introduce the f-string
# \n - newline
print(f"Subtotal: ${cSubtotal:.2f}\n"
      f"Tax: ${cTax:.2f}\n"
      f"Total: ${(cSubtotal + cTax):.2f}")
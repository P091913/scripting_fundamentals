import re

# setup function to validate income check
def validate_income(amount):
    # should allow the user to enter values
    # such as ex:
    # $25,000
    # $6,534
    # $345
    # $25000
    # $1
    pattern = r"^\$(\d{1,2},\d{3}|\d{1,5})$"
    if re.match(pattern, amount):
        amount = int(amount.replace("$", "").replace(",", ""))
        if amount > 25000:
            print("This check has to go to accounting")
        else:
            print("This check can be processed")
    else:
        print("Invalid value")

validate_income("$25100")
validate_income("$10000")
validate_income("$15,543")
validate_income("$1")
validate_income("3452") # invalid
validate_income("$23,346")


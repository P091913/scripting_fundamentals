import re
# regex library allows us to utilize pattern searching functionality

user_num = input("Enter a valid telephone number: ")
tele_pattern = r"^\d{3}-\d{3}-\d{4}$"

if re.search(tele_pattern, user_num):
    print("We have a valid number")
else:
    print("Number is invalid")



# pattern where the first 3 characters cannot be numbers
track_num = input("Enter a valid tracking number: ex(ABC3:4J45:JC74)")
tracking_pattern = r"^\D{3}\w:\w{4}:\w{4}"

if re.search(tracking_pattern, track_num):
    print("We have a valid tracking number ")
else:
    print("Tracking number is invalid")


person_name = input("Enter the name of the person (first and last): ")
person_pattern = r"\D\s\D"

if re.search(person_pattern, person_name):
    print("We have a valid person name")
else:
    print("Person name is invalid")








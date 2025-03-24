# lists
# 0, 1, 2, 3, 4
my_lists = ["Car1", "Car2", "Car3", "Car4", "TheCar"]

print(my_lists[1])

# list are changable
my_lists.append("ExtendedCar")

print(my_lists[5])

try:
    print(my_lists[6])
except IndexError:
    print("Invalid Index")

def car_loop():
    for i in my_lists:
        print(i)

# display all cars to the user
car_loop()

car_value = input("Enter the car you'd like to remove: ")
if car_value in my_lists:
    my_lists.remove(car_value) # remove the car from the list
else:
    print("Car Doesn't exist")

# display all cars to the user
car_loop()

# tuple - same as list, can't make any changes once it's been initialized
my_tuple = ("Car", "Car2", "Car3")

print(my_tuple)


# dictionary
# this stores value key-value

my_dictionary = {
    # key  :   value
    "name": "Jarrett",
    "work": "IHCC",
    "cans_drink": 4
}

print(my_dictionary["name"])
my_dictionary["name"] = "Person1" # updates the name value
print(my_dictionary["name"])

# loop through my dictionary
for key, value in my_dictionary.items():
    print(key, value)

### Monday 17th #####
# create a list of dictionaries, showcase use of a class
# showcase removing from dictionary
# showcase iterating through a list of dictionary
# showcase remove a specific dictionary set from a list
# walkthrough same example using a class by creating an instance
# updating values based on key in dictionary while looping
# true/false if value exists

# create new list
# store people information using a dictionary
people = [
    {"Name": "Jarrett", "Location": "Iowa", "Car": "Chevy"},  # 0
    {"Name": "Brad", "Location": "Iowa", "Car": "Ford"},      # 1
    {"Name": "Cole", "Location": "Colorado", "Car": "Nissan"} # 2
]

# Update location based on user input
location = input("Enter the updated location: ")
up_name = input("Enter the name for the location you're updating: ").upper()
for person in people:
    if person["Name"].upper() == up_name:
        person["Location"] = location


# display all information is my list using my dictionaries key values
for person in people:
    print(f"{person["Name"]}, {person['Location']}, {person['Car']}")

# remove all car information Cole
people[2].pop("Car")
print(people[2])


name_input = input("Enter a name to remove their location ").upper()
for person in people:
    if person["Name"].upper() == name_input:
        person.pop("Location")

print(people)


name = input("Remove Person Information: ").upper()
# standard for loop with decision structure
#for person in people:
#    if person['Name'].upper() == name:
#        people.remove(person)
#print(people)

# list comprehension
people = [p for p in people if p["Name"].upper() != name]
print(people)








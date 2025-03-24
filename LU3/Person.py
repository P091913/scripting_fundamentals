class Person:
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old. They are from {self.location}"


# create an instance of person
my_person = Person("Jarrett", "Iowa", 25)
print(my_person.name)

# example of a pre-populated list of objects using the Person class
#my_list = [
#    Person("Jarrett", "Iowa", 23),
#    Person("Brad", "Iowa", 30),
#    Person("Cole", "Colorado", 27)
#]

my_list = []
while True:
    break_var = input("Do you want to enter another person? (yes/no)").lower()
    if break_var == "no":
        break
    name = input("What is the name of the person you're adding? ")
    location = input("What is this persons location? ")
    age = input("How old is this person? ")

    if name and location and age:
        person = Person(name, location, age)
        my_list.append(person)

for person in my_list:
    print(person)

# March 17th continuation - 18th
# ask for a name to see if it exists
# name = input("What name are you searching for? ")

# dictionary setup for a true/false return value on whether a result was found
# name_exists = any(my_list["Name"])

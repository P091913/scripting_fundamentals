# variable and initialize to 0
import random
x = 0
while x < 5:
    print(x + 1)
    # x = x + 1
    x += 1

a = 0
while True: # an infinite loop, True is always True
    print(a)
    a += 1
    if a >= 5:
        break # break will pull us out of our always True while loop

num_entry = 0
#while True:
#    user_num = int(input("Enter a number: "))
#    num_entry += user_num
#    if num_entry > 500:
#        break


bugs_accum = 500
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(days_of_week[0])
x = 0
while True:
    bug_entry = int(input(f"Enter the number of bugs you caught on {days_of_week[x]}"))
    bugs_accum -= bug_entry
    x += 1
    if x > 4:
        break

print(bugs_accum)

##
## += 1 - adds one
## -= 1 - subtract one

##names = ["Kathy", "Beau", "Andon", "Timmy", "Jack"]
#rand_item = random.choice(names)
#while True:
#    index = random.randint(0, 4)
#    print(f"Dinosaur Name: {names[index]}")


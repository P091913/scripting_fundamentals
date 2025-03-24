# for loop that uses range

# loop control
    # logic that you want to execute

# start with 0
# range 5
# Won't start at 1 (1 - 5)
# Loop controls by default will start at 0 (0 - 4)

# 1st time through, i = 0
# 2nd time through, i = 1
# ... i = 2
# ... i = 3
# ... i = 4
for i in range(5):
    print(i + 1)

# list - allows us to store multiple values that we can access
#        using an index
# sets up an empty list called days_of_week
# days_of_week = []
#
# setup a pre-initialized list with the days of the week
# index            0          1           2           3           4
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in days_of_week:
    print(i)


#### Bug Collector ####
# track total number of bugs
bugs_accum = 0
bug_per_day = []

for i in range(5):
    num_bugs = int(input(f"Enter the number of bugs that you caught on {days_of_week[i]}"))
    bugs_accum += num_bugs
    # append will add the value within the parenthesis to the list
    bug_per_day.append(num_bugs)
    # bug_per_day [3, 5]


# showcasing iterating through a list that we added values
# and showcasing using the same index/subscript value to iterate through 2 lists
for i in range(5):
    print(f"You caught {bug_per_day[i]} on {days_of_week[i]}")

print(bugs_accum)


##



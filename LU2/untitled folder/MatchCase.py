# validate user input using match case

# function setup
def second_setup_match_case(user_answer):
    match user_answer:
        case "a":
            pass
        case "b":
            print("Correct Answer")
        case "c":
            pass
        # _ other, if you didn't fall into any of your other cases
        case _:
            print("Invalid Answer, try again")


# accept user_answer in as a parameter
def first_setup_if_struc(user_answer):
    if user_answer in answers:
        print("Valid Input")
        if user_answer == "b":
            print("Correct Answer")
            # break
        else:
            # times_wrong += 1
            print("Incorrect Answer, Try Again")

# list for validating user_answer
answers = ["a", "b", "c"]
# assigning int datatype as my initial variable setup
# unlike other languages, python doesn't enforce the datatype
# times_wrong: int
times_wrong = 0
while True:
    user_answer = input("What is the correct answer to the problem? 10/5\n"
                        "A. 1\n"
                        "B. 2\n"
                        "C. 5 ").lower()

    solving_method = input("Would you like to solve this problem using \n"
                           "match:case or an if structure (match/if): ")

    if solving_method == "match":
        # call my function, pass in user_answer as an argument
        # this way we can access the value
        second_setup_match_case(user_answer)
        break
    elif solving_method == "if":
        # pass user_answer in as an argument
        first_setup_if_struc(user_answer)
        break
    else:
        print("Invalid input, try again")


print(f"You guessed incorrectly {times_wrong} time(s)")


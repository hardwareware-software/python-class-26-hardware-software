# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header

print() # prints an empty line
print("My Awesome Quiz on Python Concepts")
print() # prints an empty line
print("*" * 20) # print line of 20 asterics

# ask for users name
print() 
username = input("what is your name? ")
print(f"Hello, {username}!")

# ask if they want to take a quiz

print()
start_quiz = input("Do you want to take my awesome quiz? Y/N ")
if start_quiz.upper() == "Y": # this will make any lowercase input into an uppercase for comparison
    print("Great! Let's get started!")
    # put our quiz questions here all indented
    # start our quiz

    # set our counter to 0
    counter = 0

    # question 1
    q1 = int(input("How would Python solve 2 * 2? "))
    if q1 == 4:
        # update my counter
        counter += 1 #short hand for counter = counter + 1
        print("Yes! You are correct. Python would solve this as 4")
    else: #INCORRECT
        print("Sorry. That is not correct. ")
    # question 2
    q2 = "What is the function that we use to output something to the terminal?"
    print("  A - output()")
    print("  B - print()")
    print("  C - format()")
    print("  D - none of the above")
    if q2 == "B":
        counter += 1
       
        print("Sorry. That is not correct. ")


elif start_quiz == "N":
    print("Ok. Maybe next time")

else:
    print("sorry that is invalid")










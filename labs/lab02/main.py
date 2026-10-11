# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
print("*" * 20) # print line of 20 asterics
print() # prints an empty line
print("My Amazing Quiz")
print() # prints an empty line
print("*" * 20) # print line of 20 asterics

# ask for users name

print() 
username = input("what is your name? ")
print()
print("*" * 20)
print()
print(f"Hello, {username}!")
print()
print("*" * 20)
# ask if they want to take a quiz

print()
start_quiz = input("Do you want to take my awesome quiz? Y/N ")
if start_quiz.upper() == "Y": # .upper will make any lowercase input into an uppercase for comparison
    print()
    print("Great! Let's get started!")
    print()
    print("*" * 20)
   
    # put our quiz questions here all indented
   
    # start our quiz

    # set our counter to 0
    
    counter = 0

    # question 1

    print()
    q1 = int(input("How would Python solve 2 * 2? "))
    if q1 == 4:
        # update my counter
        print()
        counter += 1 # short hand for counter = counter + 1
        print("Yes! You are correct. Python would solve this as 4.")
    else: # INCORRECT
        print("Sorry. That is not correct. ")
    print()
    print("*" * 20)
    print()

    # question 2
    print("What is the function that we use to output something to the terminal?")
    print()
    print("    A - output()")
    print("    B - print()")
    print("    C - format()")
    print("    D - none of the above()")
    print()
    q2 = input("Your Answer - Choose A/B/C/D: ")
    if q2.upper() == "B":
        # update my counter because they got the answer right
        counter += 1 # shorthand for counter = counter + 1
        print()
        print("Yes! You are correct. Python would use the print() function to output something to the terminal.")
    else: # INCORRECT
        print("Sorry. That is not correct.")
    print()
    print("*" * 20)
    print()

    # question 3
    
    print("How many years would have passed since 2010?")
    print()
    print("    A - 5()")
    print("    B - 8()")
    print("    C - 16()")
    print("    D - none of the above()")
    print()
    q3 = input("Your Answer - Choose A/B/C/D: ")
    if q3.upper() == "C":
            # update my counter because they got the answer right
        counter += 1 # shorthand for counter = counter + 1
        print()
        print("Yes! You are correct. It would be 16 year since 2010.")
    else: # INCORRECT
            print("Sorry. That is not correct.")
    print()
    print("*" * 20)
    print()

    # question 4

    q4 = (input("Are dalmations spotted? Y/N "))
    print()
    if q4.upper() == "Y":
            # update my counter
        counter += 1 # short hand for counter = counter + 1
        print()
        print("Yes! You are correct. Dalmations are spotted")
    else: # INCORRECT
        print("Sorry. That is not correct. ")
    print()
    print("*" * 20)
    print()        

    # question 5

    print("Where in the united states is california located on a map?")
    print()
    print("    A - (west coast)")
    print("    B - (east coast)")
    print("    C - none of the above()")
    print()
    q5 = input("Your Answer - Choose A/B/C/D: ")
    if q5.upper() == "A":
               # update my counter because they got the answer right
               counter += 1 # shorthand for counter = counter + 1
               print("Yes! You are correct. California is located on the west coast of the united states.")
    else: # INCORRECT
               print("Sorry. That is not correct.")
    print()
    print("*" * 20)
    print()

    # print final score
    
    print(" ==== YOUR FINAL SCORE ====")
    print()
    print(f"{username}, your final score is: {counter} out of 5.")
    print() 

     # give them feedback on their overall score

    if counter == 5:
        print("Perfect score! Great job!")
        print() 
    elif counter >= 3 and counter < 5:
        print("Good Work!")
    elif counter >= 1 and counter < 3:
        print("Keep studying and try agian!")
    else:
        print("You got 0 answers correct. Try agian.")
        

elif start_quiz.upper == "N":
    print("Sorry, maybe next time!")
else:
    print("Sorry. That is an invalid response. Try agian.")


# farewell message

print("Thanks and have a great day! ")









# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# input info

import nameformat

nameformat.hello_world()

def main():
    # program tital
    print("Welcome to your name")
    print()

    # ask for first?last name
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")

    # menu system
    while True:
        print("* * MENU * *")
        print("1- Say Hello")
        print("2 - Output Full Name")
        print("3 - Output Last Name, First Name")
        print("4 - Read Module Documentation")
        print("5 - Exit Program")
        choice =input("What would you like to do? ")

        # if else block based on choice input
        if choice == "1":
            # call sayHello
            nameformat.sayHello(firstName)
        elif choice == "2":
            # call fullName
            nameformat.fullName(firstName, lastName)
        elif choice == "3":
        # call lastNameFirst 
            nameformat.lastNameFirst(firstName, lastName)
        elif choice == "4":
            print("Documentation")
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)
        elif choice == "5":
            print("Thank you for using our program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
    
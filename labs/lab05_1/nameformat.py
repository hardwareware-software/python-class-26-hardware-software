# module file for lab 5 - nameformat.py

def hello_world():
    print("Hello Halloween 2026!")

def sayHello(firstName):
    """Definition: A simple funtion that takes a firstName input and says hello to that name."""
    print(f"Hello there {firstName}. What a cool name. Welcome to your name!")
    print()

def fullName(firstName, lastName):
    """Definition: A simple funtion that takes a firstName and lastName and input and outputs the first and last name."""
    print(f"{firstName} {lastName}")
    print()

def lastNameFirst(firstName, lastName):
    """Definition: A simple funtion that takes a firstName and lastName input and outputs the last and first name with a comma."""
    print(f"{lastName}, {firstName}")
    print()

def documentation():
    help(sayHello)
    help(fullName)
    help(lastNameFirst)
    
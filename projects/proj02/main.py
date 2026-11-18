# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header

def display_welcome():
    print("The story generator program")
    print()

def story_one():
    print("A day at the park")
    print()

    friend = input("enter a friends name: ")
    animal = input("enter an animal: ")
    color = input ("enter a color: ")
    food = input("Enter a food: ")
    number = input("Enter a number: ")
    activity = input("Enter an activity: ")

    print()
    print("Here is your story:")
    print()

    print(f"One day, I went to the park with {friend}.")
    print(f"We saw a {color} {animal} running around.")
    print(f"We decided to eat {food} while sitting at the park.")
    print(f"After {number} hours, we started {activity}.")
    print("We had a good time and went home.")
    print()

def story_two():
    print("A Trip to the Store")
    print()

    store = input("Enter a store name: ")
    item = input("Enter an item: ")
    person = input("Enter a person's name: ")
    price = input("Enter a price: ")
    transportation = input("Enter a type of transportation: ")
    emotion = input("Enter an emotion: ")

    print()
    print("Here is your story:")
    print()

    print(f"Yesterday, I went to {store} to buy a {item}.")
    print(f"While shopping, I saw my friend {person}.")
    print(f"The {item} cost {price} dollars, so I decided to buy it.")
    print(f"After shopping, I took the {transportation} home.")
    print(f"I felt {emotion} about my purchase.")
    print()

def main():
    display_welcome()

    count = 0

    play = input("Would you like to create a story? (y/n): ")

    while play != "y" and play != "n":
        print("Invalid entry. Please enter y or n.")
        play = input("Would you like to create a story? (y/n): ")

    if play == "y":
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
        print()

    while play == "y":
        print("a. A Day at the Park")
        print("b. A Trip to the Store")
        print()

        choice = input("Choose a story (a/b): ")

        while choice != "a" and choice != "b":
            print("Invalid choice. Please enter a or b.")
            choice = input("Choose a story (a/b): ")

        if choice == "a":
            story_one()
        elif choice == "b":
            story_two()

        count += 1
        print(f"You have created {count} stories.")
        print()

        play = input("Would you like to create another story? (y/n): ")

        while play != "y" and play != "n":
            print("Invalid entry. Please enter y or n.")
            play = input("Would you like to create another story? (y/n): ")

    print("Bye!")


if __name__ == "__main__":
    main()
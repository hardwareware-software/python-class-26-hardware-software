# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 - 72473 Dominic Dongell 10/27/2026
shirt_price = 6.00
hat_price = 5.00

shirt_quantity = 0
hat_quantity = 0

shirt_embroidery_price = 0.00
hat_embroidery_price = 0.00

print()
print("*" * 20)
print()
print("Welcome to TECHnon Embroidery House!")
print()
print("*" * 20)
print()

interest = input("Would you like to get started on your custom embroidered apparel journey? (y/n): ")
print()

if interest == "y":

    print("Great! Lets get started!")
    print()
    print("*" * 20)
    print()

    # Overview of our services
    print("At TECHnon Embroidery House, we specialize in")
    print("custom embroidered apparel for businesses,")
    print("special events, and personal use.")
    print("Our embroidery services allow customers to")
    print("personalize shirts and hats with their own designs.")
    print()

    purchase = input("Would you like to place an order? (y/n): ")
    print()

    if purchase == "y":

        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        email = input("What is your email address? ")
        phone = input("What is your phone number? ")

        print()
        print("-" * 20)
        print()

        print("We offer quality embroidery for both shirts and hats.")
        print()
        print("Which items were you interested in having embroidered?")
        print()
        print("Shirts")
        print("- $6 per")
        print()
        print("Hats")
        print("- $5 per")
        print()
        print("Both")
        print()

        q1 = input("?  ")
        print()
        print("-" * 8)
        print()

        if q1 == "Shirts":
            print("Wonderful! Lets now discuss the number of units you are looking for.")
            print()
            shirt_quantity = int(input("How many shirts would you like? "))

        elif q1 == "Hats":
            print("Awesome! Lets now discuss the number of units you are looking for.")
            print()
            hat_quantity = int(input("How many hats would you like? "))

        elif q1 == "Both":
            print("Great! Lets now discuss the number of units you are looking for.")
            print()
            shirt_quantity = int(input("How many shirts would you like? "))
            hat_quantity = int(input("How many hats would you like? "))

        else:
            print("Sorry, we do not carry that item.")

        print()
        item_quantity = shirt_quantity + hat_quantity

        if item_quantity > 0:

            print("Total items:", item_quantity)

            print()
            print("-" * 8)
            print()

            print("We offer a base pricing depending on the size of the embroidery.")
            print()
            print("Please specify the size from small to large in order to provide you with an accurate quote for your total.")
            print()
            print("S")
            print("- $5 per")
            print()
            print("M")
            print("- $10 per")
            print()
            print("L")
            print("- $15 per")
            print()

            q2 = input("?  ")
            print()
            print("-" * 8)
            print()

            if q2 == "S":
                shirt_embroidery_price = 5.00
                hat_embroidery_price = 5.00
                print("Great! Lets now continue to your final quote!")
                print()

            elif q2 == "M":
                shirt_embroidery_price = 10.00
                hat_embroidery_price = 10.00
                print("Great! Lets now continue to your final quote!")
                print()

            elif q2 == "L":
                shirt_embroidery_price = 15.00
                hat_embroidery_price = 15.00
                print("Great! Lets now continue to your final quote!")
                print()

            else:
                print("Sorry, that is not a valid embroidery size.")

            if q2 == "S" or q2 == "M" or q2 == "L":

                shirt_blank_total = shirt_quantity * shirt_price
                hat_blank_total = hat_quantity * hat_price

                blank_total = shirt_blank_total + hat_blank_total

                # Calculate embroidery costs
                shirt_embroidery_total = shirt_quantity * shirt_embroidery_price
                hat_embroidery_total = hat_quantity * hat_embroidery_price

                embroidery_total = shirt_embroidery_total + hat_embroidery_total

                # Calculate subtotal
                subtotal = blank_total + embroidery_total

                # Calculate sales tax
                tax = subtotal * 0.10

                # Calculate final total
                total_cost = subtotal + tax

                # Calculate price per item
                shirt_unit_price = shirt_price + shirt_embroidery_price
                hat_unit_price = hat_price + hat_embroidery_price

                print()
                print("*" * 30)
                print()
                print("FINAL QUOTE")
                print()
                print("*" * 30)
                print()

                print("Total shirts:", shirt_quantity)
                print("Total hats:", hat_quantity)
                print("Total items:", item_quantity)
                print()

                print("Blank shirt cost: $", shirt_blank_total)
                print("Blank hat cost: $", hat_blank_total)
                print()
                print("-" * 30)
                print()

                print("Blank garment total: $", blank_total)
                print("Embroidery total: $", embroidery_total)
                print("Subtotal: $", subtotal)
                print("Sales tax (10%): $", tax)
                print()
                print("TOTAL DUE: $", total_cost)

                # Customer receipt
                print()
                print("*" * 30)
                print()
                print("TECHnon EMBROIDERY HOUSE")
                print("ORDER RECEIPT")
                print()
                print("*" * 30)
                print()

                print("Customer:", first_name, last_name)
                print("Email:", email)
                print("Phone:", phone)
                print()

                print("Total shirts:", shirt_quantity)
                print("Total hats:", hat_quantity)
                print("Total items:", item_quantity)
                print("Embroidery size:", q2)
                print()

                print("Blank shirt cost: $", shirt_blank_total)
                print("Blank hat cost: $", hat_blank_total)
                print()
                print("Shirt embroidery: $", shirt_embroidery_total)
                print("Hat embroidery: $", hat_embroidery_total)
                print()
                print("-" * 30)
                print()

                print("Subtotal: $", subtotal)
                print("Sales tax (10%): $", tax)
                print()
                print("TOTAL DUE: $", total_cost)
                print()
                print("*" * 30)
                print()

                print("Thank you for your order,", first_name + "!")
                print()
                print("We appreciate your business! We will contact you via email to continue further with your order. ")
                print("Have a wonderful day!")
                print()
                print("-" * 20)

        else:
            print("No valid items were selected.")
            print("Thank you for visiting TECHnon Embroidery House!")

    else:
        print("Thank you for considering TECHnon Embroidery House!")
        print("We hope to work with you in the future!")

else:
    print("Ok. Please let us know if we could be of any service in the future!")

# Starting file for LAB 7
# Include your course number, student first and last name, and date in the comment header

import csv

# create a filename for our csv file
filename = "trips.csv"

def write_trips(trips):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()
    # create placeholder list
    trips = []

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # create a list for the 3 values of this calculation

        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        # now append this entire row to my trips list
        trips.append(trip)
        print(trips)
        
        more = input("More entries? (y or n): ")

    write_trips(trips)
    
    print("Bye!")

if __name__ == "__main__":
    main()

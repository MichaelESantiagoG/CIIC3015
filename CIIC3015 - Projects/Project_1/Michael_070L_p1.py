# Filename: project_1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Michael E. Santiago
# STUDENT ID: ###-##-####
# SECTION: 070L
############      DEFINE CONSTANTS BELOW      ############

KILOMETERS_PER_MILE = 1.60934
MILE_PER_KILOMETERS = 0.62137
KILOGRAMS_PER_POUNDS = 2.20462
POUNDS_PER_KILOGRAMS = 0.45359


############       ADD YOUR CODE BELOW        ############


############ DO NOT MODIFY THE SECTION BELOW  ############


def print_program_menu():  # this function was created to print the menu
    print("\n--------")
    print("Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Miles/hour to kilometers/hour")
    print("6. Exit")


def main():
    done = False
    while not done:
        print_program_menu()  # this function prints the menu, you don't need to change it
        userOption = input("Enter option: ")
        # Start writing your code below- don't modify the code lines of this base code
        if userOption.isdigit():  # This Verify that a number was input
            numericOption = int(userOption)
            # Check if the selection is within permitted range. If it is valid proceed to do the correcponding conversion

            if numericOption == 1:
                units_to_BC = input("Enter the <units> to be converted: ")
                if units_to_BC.isdigit():
                    units_to_BC = float(units_to_BC)
                    print(
                        units_to_BC,
                        "miles are equivalent to",
                        round(units_to_BC * KILOMETERS_PER_MILE, 3),
                        "kilometers",
                    )
                else:
                    print("Invalid option\n")

            elif numericOption == 2:
                units_to_BC = input("Enter the <units> to be converted: ")
                if units_to_BC.isdigit():
                    units_to_BC = float(units_to_BC)
                    print(
                        units_to_BC,
                        "kilometers are equivalent to",
                        round(units_to_BC * MILE_PER_KILOMETERS, 3),
                        "miles",
                    )
                else:
                    print("Invalid option\n")

            elif numericOption == 3:
                units_to_BC = input("Enter the <units> to be converted: ")
                if units_to_BC.isdigit():
                    units_to_BC = float(units_to_BC)
                    print(
                        units_to_BC,
                        "pounds are equivalent to",
                        round(units_to_BC * POUNDS_PER_KILOGRAMS, 3),
                        "kilograms",
                    )
                else:
                    print("Invalid option\n")

            elif numericOption == 4:
                units_to_BC = input("Enter the <units> to be converted: ")
                if units_to_BC.isdigit():
                    units_to_BC = float(units_to_BC)
                    print(
                        units_to_BC,
                        "kilograms are equivalent to",
                        round(units_to_BC * KILOGRAMS_PER_POUNDS, 3),
                        "pounds",
                    )
                else:
                    print("Invalid option\n")

            elif numericOption == 5:
                units_to_BC = input("Enter the <units> to be converted: ")
                if units_to_BC.isdigit():
                    units_to_BC = float(units_to_BC)
                    print(
                        units_to_BC,
                        "<mph> (miles per hour)  are equivalent to",
                        round(units_to_BC * KILOMETERS_PER_MILE, 3),
                        "<kmh> (kilometers per hour) ",
                    )
                else:
                    print("Invalid option\n")

            elif numericOption == 6:
                print("Thanks for using the unit conversion program!")
                done = True
            elif numericOption < 1 or numericOption > 6:
                print("Invalid option\n")
        else:
            print("Invalid option\n")
            # Option was invalid


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()

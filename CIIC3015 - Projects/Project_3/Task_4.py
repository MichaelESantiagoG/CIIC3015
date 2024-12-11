import sys

# my proj. code pt 2
# menu on the list
menu = []  # List of dictionaries of the ingredients
menu_list = []  # list of plates
doc = open("recipe.txt", "r")
for line in doc:
    if line[0].isalpha():
        menu_list.append(line.strip())
        line = {}
        menu.append(line)
    elif line[0].isdigit():
        sline = line.strip().split(" ", 1)
        plate = menu[-1]
        plate[sline[1]] = float(sline[0])

# _____________________________________________________
# Base Code
# data structured
pantry = {}  # dictionaries of available inventory
units = list(menu[0].keys())
ingredients = list(menu[0].values())

# _____________________________________________________
# modified:\/


# ask for ingredients available
def pantry_ingredients():
    for i in range(len(units)):
        unit = units[i]
        item = float(input(f"How many {unit} do you have? "))
        pantry[unit] = item


# ______________________________________________________
# Mod in progress
# show the ingredients of an exisiting pantry


def show_pantry():
    # print(pantry)
    for i in pantry:
        unit = i
        print(f"{pantry[i]} {unit}")


show_pantry()

# ______________________________________________________


def docopyfunc():
    doc = open("recipe.txt", "r")
    docopy = open("recipe2update.txt", "w")
    for line in doc:
        docopy.write(line)
    docopy.close()
    return docopy


def checkif():
    # pantryinlist = list(pantry.values())
    # menuaslist = list(menu[i].values())
    menuirecipe = []
    for i in range(len(menu)):
        for key, val in pantry.items():
            if menu[i].get(key) * int(servings) > val:
                menuirecipe.append(i)
                break

    for j in range(1, len(menuirecipe) + 1):
        negative_index = j * -1
        del menu[menuirecipe[negative_index]]
        del menu_list[menuirecipe[negative_index]]
        # if menu[i] >= pantrylist[i]:
        #   return True
        # else:
        #   False


def removalindex():
    return


# show the menu options
def recipe_menu():
    checkif()
    print("What would you like to cook? Here's the recipe book:")

    # options already in the menu
    for i in range(len(menu_list)):
        print(i + 1, ". ", menu_list[i], sep="")
    if len(menu_list) == 0:
        i = -1

    # add new recipe
    print(i + 2, ". Add new recipe.", sep="")

    # exit program
    print(i + 3, ". Nevermind, I don't want to cook anything (Exit).", sep="")

    option = int(input("Select an option by typing its number here:"))

    # if new recipe selected
    if option == i + 2:

        docopyfunc()
        doc = open("recipe2update.txt", "a")

        new_recipe_name = input("Name of the new recipe: ")
        menu_list.append(new_recipe_name)
        doc.write(new_recipe_name + "\n")
        new_recipe = {}

        for i in range(len(units)):
            unit = units[i]
            item = input(f"How many {unit} are required? ")
            new_recipe[unit] = float(item)
            doc.write(item + " " + unit + "\n")
        menu.append(new_recipe)
        checkif()

    # return option selected
    return option


# check valid option
def valid_option(option):
    while True:
        # valid option
        if option in range(1, len(menu_list) + 1):
            recipe = menu[option - 1]
            # global servings
            # servings = int(input("How many servings? "))
            break

        # exit program
        elif option == len(menu_list) + 2:
            print("See you later!")
            sys.exit(0)

        # invalid option
        else:
            print("Please select a valid option")
            option = recipe_menu()
    return recipe


# update pantry
def pantry_update():
    # list of updated ingredients available
    for i in pantry:
        leftover = pantry[i] - (recipe[i] * servings)
        if leftover < 0:
            # if not enough ingredients
            return False
        pantry[i] = float(leftover)
    # if enough ingredients
    return True


# ask user to input ingredients available
pantry_ingredients()
cook = True

# initialize servings to 1
servings = 1
while cook:
    # ask user what they'd like to make (from options)
    servings = int(input("How many servings? "))

    option = recipe_menu()
    print(f"You selected option {option}")

    # verify the selected option is valid
    recipe = valid_option(option)

    # if the option is valid and want to cook

    # while not enough ingredients
    while not pantry_update():
        print("Not enough ingredients!")
        pantry = {}
        print("Update the ingredients.")
        pantry_ingredients()

    # enough ingredients.
    print("Great choice. That was delicious!")
    print("Here's what's left in the pantry: ")
    show_pantry()

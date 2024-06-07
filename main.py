import easygui

# author: luka
# date: 12:09 noon, May 16, 2024
# user welcome
# v8

# welcomes the user to the program giving them multiple options
def welcom():

    # Displaying a choice box with options
    choices = easygui.choicebox("Welcome to the recipe program!!!", "Quiz", [
        "Start",
        "Exit",
        "Help",
        "About",
    ])
    # Handling user's choice
    if choices == "Start":
        easygui.msgbox("Lets get started")
    elif choices == "Exit":
        exit()  # Exiting the program
    elif choices == "Help":
        easygui.msgbox('To utilize the recipe cost calculator,\
                       begin by launching the program. When prompted,\
                       input the name of the recipe you wish to calculate the cost for,\
                       along with the serving size. Next, add each ingredient required\
                       for the recipe, providing details such as the ingredient name,\
                       amount needed, and cost per unit. Once all ingredients are\
                       entered, the program will compute the cost per serving based on\
                       the provided inputs. You have the option to save the recipe for\
                       future reference, with the program prompting you to overwrite\
                       existing recipes if necessary. If you input a recipe name\
                       that is already saved, you can choose whether to use the\
                       existing recipe or overwrite it with new inputs. Additionally,\
                       if using a saved recipe, you can adjust the serving\
                       size, and the program will recalculate the cost per serving\
                       accordingly. Once you have finished calculating the recipe cost,\
                       you can exit the program. If you made any modifications to a\
                       saved recipe, the program will prompt you to save the changes\
                       before exiting. Saved recipes are stored in a JSON file named\
                       "recipes.json", allowing you to view, modify, or delete them\
                       as needed.')
    elif choices == "About":
        easygui.msgbox('This program was created by Luka Karunaratne\
                       and was designed to help users calculate the cost of\
                       cooking recipes. The program was created using the')

    else:
        easygui.msgbox("Invalid input")
        welcom()

# author: luka
# date: 10:10 am, May 15, 2024
# user welcome
# v6

# asks the user if they want to use metric or imperial units
def metricpick():

    #
    while True:
        # Displaying a choice box for measurement units
        measurment = easygui.choicebox(
            "Enter measurement (grams, milliliters): ", "units",
            ['grams', 'milliliters'])
        # If the user chooses grams, the program will continue
        if measurment == 'grams':
            # Asking for the amount in grams
            amount = easygui.integerbox("Enter amount in grams: ",
                                        '',
                                        0,
                                        lowerbound=1,
                                        upperbound=10000)
            return amount, measurment
        # If the user chooses milliliters, the program will continue
        elif measurment == 'milliliters':
            # Asking for the amount in milliliters
            amount = easygui.integerbox("Enter amount in milliliters: ",
                                        '',
                                        0,
                                        lowerbound=1,
                                        upperbound=10000)
            return amount, measurment
        else:
            print("Invalid measurement. Please enter 'g' or 'ml'.")

# author: luka
# date: 9:48 am, May 15, 2024
# user welcome
# v8

# main function that runs the program
def main():


    welcom()
    # Asking for recipe name and serving size
    recipe_name = easygui.enterbox("Enter recipe name: ")
    serving_size = easygui.integerbox("Enter serving size: ")
    easygui.msgbox(f"Recipe: {recipe_name}, serving size: {serving_size}")
    total_cost = 0
    ingredients = []
    # Loop to gather all ingredients until the user chooses to exit
    while True:
        ingredient_name = easygui.enterbox(
            "Enter ingredient name and when you want to exit type 'exit' ")
        # If statement is for when the user wants to exit
        if ingredient_name == 'exit':
            break
        # Asking for unit and amount of the ingredient
        unit = metricpick()
        cost = easygui.integerbox(
            f"Enter cost for {unit} of {ingredient_name}")
        total_cost += float(cost)
        ingredients.append(ingredient_name)
        easygui.msgbox(f"Ingredient: {ingredient_name}, {unit}, cost: {cost}")
    easygui.msgbox(f"Ingredients: {ingredients} \n \
    Total cost: {total_cost} \n \
    Total cost per serving: {total_cost/float(serving_size)}")


main()

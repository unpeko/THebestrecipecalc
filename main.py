from types import ClassMethodDescriptorType
import easygui
import math


def welcom():
  choices = easygui.choicebox("Welcome to the recipe program!!!", "Quiz", [
      "Start",
      "Exit",
      "Help",
      "About",
  ])
  if choices == "Start":
    easygui.msgbox("Lets get started")


def metricpick():
  while True:
    measurment = input("Enter measurment (g, ml): ")
    if measurment == 'g':
        amount = float(input("Enter amount in grams: "))
        return amount
    elif measurment == 'ml':
        amount = float(input("Enter amount in milliliters: "))
        return amount
    else:
        print("Invalid measurment. Please enter 'g' or 'ml'.")

def main():
    welcom()
    recipe_name = input("Enter recipe name: ")
    serving_size = input("Enter serving size: ")
    print(f"Recipe: {recipe_name}, serving size: {serving_size}")
    total_cost = 0
    ingredients = []
    while True:
        ingredient_name = input("Enter ingredient name and when you wan to exit type\
        'exit' ")

        if ingredient_name == 'exit':
            break 
        unit = metricpick()
        cost = input(f"Enter cost of {ingredient_name} for {unit} g/ml: ")
        total_cost += float(cost)
        ingredients.append(ingredient_name)

    print(ingredients)
    print(f"Total cost: {total_cost}")
    print(f"Total cost per serving: {total_cost/float(serving_size)}")
main()
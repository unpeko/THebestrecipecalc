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
    metricpick()
    recipe_name = input("Enter recipe name: ")
    serving_size = input("Enter serving size: ")
    print(f"Recipe: {recipe_name}, serving size: {serving_size}")
    while True:
        ingredient_name = input("Enter ingredient name and when you wan to exit type 'exit' ")
        if ingredient_name == 'exit':
            break 
        ingredients = []
        ingredients.append(ingredient_name)

    print(ingredients)
main()
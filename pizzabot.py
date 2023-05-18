# pizzabot program
import random
from random import randint

# names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", "Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

# welcome text
def welcome():
  '''
  Purpose: To generate a random name from a list and print out a welcome message
  Parameters: None
  Returns: None
  '''
  num = randint(0,10)
  name = (names[num])
  print("· ⋆ ★ Welcome to Doug's Dream Pizza ★ ⋆ ·")
  print("Hey, my name is", name + ",")
  print("and I will help you order your pizza.")
  print("")

# delivery and pick-up menu
def deliverypickup():
  print("Would you like to order for pick-up or delivery?")
  print("Enter 1 for pick-up")
  print("Enter 2 for delivery (will incur a $3 surcharge)")

  # while loop to avoid invalid inputs
  while True:
    try:
      delpick = int(input("Enter number here > "))
      if delpick >= 1 and delpick <= 2:

        if delpick == 1:
          print("Pickup!")
          break

        elif delpick == 2:
          print("Delivery!")
          break

      else:
        print("Number must be 1 or 2, please try again")
        print("Enter 1 for pick-up")
        print("Enter 2 for delivery (will incur a $3 surcharge)")

    except ValueError:
      print("Invalid input, please try again")
      print("Enter 1 for pick-up")
      print("Enter 2 for delivery (will incur a $3 surcharge)")

# runs all functions
def main():
  '''
  Purpose: Run all functions
  Parameters: None
  Returns: None
  '''
  welcome()
  deliverypickup()

main()
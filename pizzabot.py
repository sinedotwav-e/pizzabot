# pizzabot program
# bugs
  #30/05/23
    # pickinfo: name input allows number and name input allows letters
    # pickinfo: number input allows any amount of digits (9 - 11 digits)

import random
from random import randint

# names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", "Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

# customer details dictionary
userdetails = {}

# function for blank inputs

def notblank(query):
  valid = False
  while not valid:
    response = input(query)

    if response != "":
      print("")
      return response.title()
  
    else:
      print("")
      print("Entry cannot be blank, try again.")


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
      print("")
      if delpick >= 1 and delpick <= 2:

        if delpick == 1:
          print("Ordering for pick-up...")
          pickinfo()
          break

        elif delpick == 2:
          print("Delivery!")
          break

      else:
        print("")
        print("Number must be 1 or 2, please try again")
        print("Enter 1 for pick-up")
        print("Enter 2 for delivery (will incur a $3 surcharge)")

    except ValueError:
      print("")
      print("Invalid input, please try again")
      print("Enter 1 for pick-up")
      print("Enter 2 for delivery (will incur a $3 surcharge)")

def pickinfo():
  query = ("Please enter your name > ")
  userdetails['name'] = notblank(query)

  query = ("Please enter your phone number > ")
  userdetails['phone'] = notblank(query)

  # print user details
  # print(userdetails['name'])
  # print(userdetails['phone'])
  print(userdetails)

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
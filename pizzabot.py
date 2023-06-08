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

# pizza name
pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan',
          'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe', ]

# pizza prices
prices =  [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 
           13.50, 13.50, 13.50, 13.50, 13.50, ]

# blank space code (bs = blank space lb = linebreak)
def bs():
  lb = 50

  while lb >= 0:
    print("")
    lb = lb - 1

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
      print("! Entry cannot be blank, try again. !")


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
  print("")

  # while loop to avoid invalid inputs
  while True:
    try:
      delpick = int(input("Enter number here > "))
      print("")
      if delpick >= 1 and delpick <= 2:

        if delpick == 1:
          print("Ordering for pick-up...")
          pickinfo()
          print("")
          break

        elif delpick == 2:
          print("Ordering for delivery...")
          delinfo()
          print("")
          break

      else:
        print("")
        print("! Number must be 1 or 2, please try again !")
        print("Enter 1 for pick-up")
        print("Enter 2 for delivery (will incur a $3 surcharge)")

    except ValueError:
      print("")
      print("! Invalid input, please try again !")
      print("Enter 1 for pick-up")
      print("Enter 2 for delivery (will incur a $3 surcharge)")

# component that collects user data when pick-up is selected
def pickinfo():
  '''
  Purpose: To collect user data and store in a dictionary for later use when pick-up is selected
  Parameters: None
  Returns: None
  Bugs: Name input allows numbers, vice versa
  '''
  query = ("Please enter your name > ")
  userdetails['name'] = notblank(query)

  query = ("Please enter your phone number > ")
  userdetails['phone'] = notblank(query)

  print("")

def delinfo():
  '''
  Purpose: To collect user data and store in a dictionary for later use when delivery is selected
  Parameters: None
  Returns: None
  Bugs: Same issue as pickinfo()
  '''
  query = ("Please enter your name > ")
  userdetails['name'] = notblank(query)

  query = ("Please enter your phone number > ")
  userdetails['phone'] = notblank(query)

  query = ("Please enter your house number > ")
  userdetails['house'] = notblank(query)

  query = ("Please enter your street name > ")
  userdetails['street'] = notblank(query)

  query = ("Please enter your suburb > ")
  userdetails['suburb'] = notblank(query)

  print("")

# menu of pizzas
def menu():
    pizzatotal = 12

    print("How many pizzas would you like (max. 5)")
    pizza_num = int(input())

    print("")
    print("· ⋆ ★ The Menu ★ ⋆ ·")

    for count in range (pizzatotal):
        print("{} {} ${:.2f}" .format(count+1, pizzas[count], prices[count]))
    
    print("")
        

# runs all functions
def main():
  '''
  Purpose: Run all functions
  Parameters: None
  Returns: None
  '''
  welcome()
  deliverypickup()
  menu()

main()

# Lesson 16 Part 1 7:10/32:48
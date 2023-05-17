# pizzabot program
import random
from random import randint

# names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", "Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

# welcome screen
def welcome():
  '''
  Purpose: To generate a random name from a list and print out a welcome message
  Parameters: None
  Returns: None
  '''

  num = randint(0,10)
  name = (names[num])

  # welcome message with random name
  print("· ⋆ ★ Welcome to Doug's Dream Pizza ★ ⋆ ·")
  print("Hey, my name is", name + ",")
  print("and I will help you order your pizza.")

# delivery and pick-up menu
def delpick():
  print("nothing")

def main():
  '''
  Purpose: Run all functions
  Parameters: None
  Returns: None
  '''
  welcome()

main()
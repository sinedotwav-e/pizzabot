# pizzabot program
import random
from random import randint


names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", "Dùbhghlas", "Thrangott the Devourer", "Gab"]

def  welcome():
  '''
  Purpose: To generate a random name from the list and print out a welcome message
  Parameters: None
  Resturns: None
  '''
  num = randint(0,9)
  name = (names[num])
  print("Welcome to ∙ ⋆ ★ Doug's Dream Pizzas™ ★ ⋆ ∙")
  print("My name is", name)
  print("How may I help you?")

def main():
  '''
  Purpose: To run all functions
  Parameters: None
  Returns: None
  '''
  welcome()
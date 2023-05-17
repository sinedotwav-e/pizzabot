# bugs
# welcome message with randomly generated name
import random
from random import randint

# names for the random name generator
names = ["Doug", "Douglas", "Dougington", "Dougie", "Duggie", "Doogie", "Dougalasa", "Dùbhghlas", "Thrangott the Devourer", "Gab", "Doug Doug"]

num = randint(0,10)

name = (names[num])

print("· ⋆ ★ Welcome to Doug's Dream Pizza ★ ⋆ ·")
print("Hey, my name is", name + ",")
print("and I will help you order your pizza.")
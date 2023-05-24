# bugs
# numbers valid in name entry and letters valid in number entry
# echo of inputs is odd

# information to be collected after the pickup option is selected

# customer details dictionary
userdetails = {}

# basic intructions
print("Please enter your information for pick-up...")

# customer name
valid = False

while not valid:
  userdetails['name'] = input("Enter name here > ")
  print("")
  
  if userdetails['name'] != "":
    break

  else:
    print("Input cannot be blank.")

# customer phone number
valid = False
while not valid:
  userdetails['phone'] = input("Enter phone number here > ")
  print("")

  if userdetails['phone'] != "":
    break
  
  else:
    print("Input cannot be blank.")

print(userdetails)
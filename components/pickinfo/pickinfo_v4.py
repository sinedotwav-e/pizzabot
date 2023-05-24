# bugs
# numbers valid in name entry and letters valid in number entry
# echo of inputs is odd

# information to be collected after the pickup option is selected

# customer details dictionary
userdetails = {}

# function for blank inputs
def notblank(query):
  valid = False
  while not valid:
    response = input(query)

    if response != "":
      print("")
      return response
  
    else:
      print("")
      print("Entry cannot be blank, try again.")

# basic intructions
query = ("Please enter your name > ")
userdetails['name'] = notblank(query)

query = ("Please enter your phone number > ")
userdetails['phone'] = notblank(query)

# print user details
print(userdetails['name'])
print(userdetails['phone'])

# bugs

# information to be collected after the delivery option is selected

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

def delinfo():
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

  # print user details
  # print(userdetails['name'])
  # print(userdetails['phone'])
  # print(userdetails['house'])
  # print(userdetails['street'])
  # print(userdetails['suburb'])
  print(userdetails)

delinfo()
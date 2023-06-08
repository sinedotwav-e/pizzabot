# bugs

# information to be collected after the delivery option is selected

# customer details dictionary
userdetails = {}

detail = ['name', 'phone number', 'house number', 'street name', 'suburb']

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
  detailtotal = 5

  for count in range (detailtotal):
    query = ("Please enter your {} > " .format(detail[count]))
    userdetails[detail[count]] = notblank(query)

  print(userdetails)

delinfo()

# experimental delinfo function using a list instead of repeating the line of code 5 times
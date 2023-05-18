# bugs

# menu for selecting either pickup or delivery

print("Would you like to order for pick-up or delivery?")
print("Enter 1 for pick-up")
print("Enter 2 for delivery (will incur a $3 surcharge)")

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
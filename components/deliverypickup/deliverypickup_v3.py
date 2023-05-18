# bugs
# does not restart upon an invalid input

# menu for selecting either pickup or delivery

print("Would you like to order for pick-up or delivery?")
print("Enter 1 for pick-up")
print("Enter 2 for delivery (will incur a $3 surcharge)")

delpick = int(input("Enter number here > "))

if delpick == 1:
  print("Pickup!")

elif delpick == 2:
  print("Delivery!")

else:
  print("Invalid input, please try again")
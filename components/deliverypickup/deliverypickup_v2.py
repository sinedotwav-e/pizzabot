# bugs
# invalid input triggers else statement, but does not let the user try again

# menu for selecting either pickup or delivery

print("Would you like to order for pick-up or delivery?")
print("Enter p for pick-up")
print("Enter d for delivery (will incur a $3 surcharge)")

delpick = input()

if delpick == "p":
    print("Pickup!")

elif delpick == "d":
    print("Delivery!")

else:
    print("Invalid response, please try again")
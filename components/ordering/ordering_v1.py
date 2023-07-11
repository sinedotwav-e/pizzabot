# ask for a total number of pizzas for order
pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan',
          'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe', ]

prices =  [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 
           13.50, 13.50, 13.50, 13.50, 13.50, ]

# list storing current ordered pizzas
ordlist = []
# list storing pizza prices 
ordcost = []

def menu():
    pizzatotal = 12

    for count in range (pizzatotal):
        print("{} {} ${:.2f}" .format(count+1, pizzas[count], prices[count]))

menu()

# total number of ordered pizzas
pizzasnum = 0 

pizzasnum = int(input("How many pizzas would you like to order? > "))

print(pizzasnum)

# choose pizza from menu
print("Please select a pizza using the index number (the one on the far left)")

for item in range(pizzasnum):
    while pizzasnum > 0:
        ordnum = int(input())
        ordlist.append(pizzas[ordnum])
        ordcost.append(prices[ordnum])
        print("You have ordered", (pizzas[ordnum]), "pizza")
        pizzasnum = pizzasnum - 1

print(ordlist)
print(ordcost)
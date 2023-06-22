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
pizzas_num = 0 

pizzas_num = int(input("How many pizzas would you like to order? > "))

print(pizzas_num)

# choose pizza from menu
print("Please select a pizza using the index number (the one on the far left)")

for item in range(pizzas_num):
    while pizzas_num > 0:
        order = int(input())
        ordlist.apped(pizzas[order])
# bugs

# menu to display all pizzas, their prices and index number

pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan',
          'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe', ]

prices =  [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 
           13.50, 13.50, 13.50, 13.50, 13.50, ]

def menu():
    pizzatotal = 12

    print("How many pizzas would you like (max. 5)")
    pizza_num = int(input())

    print("")
    print("· ⋆ ★ The Menu ★ ⋆ ·")

    for count in range (pizzatotal):
        print("{} {} ${:.2f}" .format(count+1, pizzas[count], prices[count]))

menu()
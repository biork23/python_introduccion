from stringprep import in_table_a1


print('Welcome to the Shopping Cart Program!')

cart_items = []
items_prices = []

action = 0
total = 0


while action != 5 :

    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. quit')
    
    action = int(input('Please enter an action: '))

    if action == 1:
        item = input('What item would you like to add? ')
        price = float(input(f"What is the price of '{item}'? "))
        cart_items.append(item)
        items_prices.append(price)
        print(f"'{item}' has been added to the cart")
        print()

    elif action == 2:  

        print("The contents of the shopping cart are: ")
        print()

        for i in range(len(cart_items)):
            print(f'{i + 1}. {cart_items[i]} - ${items_prices[i]}') 
            print() 

    elif action == 3:
        item_removed = int(input('Which item would you like to remove? '))
        if item_removed > len(cart_items):
            print('Sorry, that is not a valid item number.')
        else:
            cart_items.pop(item_removed - 1)
            items_prices.pop(item_removed - 1)
            print('Item removed') 

    elif action == 4:
        for i in range(len(items_prices)):

            total += items_prices[i]
        print(f'The total price of the items in the shopping cart is {total:.2f}')

    elif action == 5:
        print('Thank you. Goodbye.')
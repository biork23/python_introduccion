print('Welcome to the Shopping Cart Program!')

cart_items = []

action = 0


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
        cart_items.append(item)
        print(f"'{item}' has been added to the cart")
        print()

    elif action == 2:  

        print("The contents of the shopping cart are: ")
        print()

        for item in cart_items:
            print(item)        
    elif action == 5:
        print('Thank you. Goodbye.')
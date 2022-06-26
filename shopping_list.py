
print('Please enter the items of the shopping list (type: quit to finish): ')

list_items = []
items = None

while items != 'quit':
    items = input('item: ')

    if items != 'quit':
        list_items.append(items)
        

print("\nThe shopping list is:")
for item in list_items:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(list_items)):
    item = list_items[i]
    print(f"{i}. {item}")    

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

list_items[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(list_items)):
    item = list_items[i]
    print(f"{i}. {item}")    
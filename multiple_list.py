

print("Enter the names and balances of bank accounts (type: quit when done)")

acounts = []
balances = []

name = None

highest_value = 0

while name != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        balance = float(input("What is the balance? "))

        acounts.append(name)
        balances.append(balance)

total = 0


# While the user wants to update, give them the list and ask what number they want to change
update = ""
while update != "n":
    for i in range(len(acounts)):
        print(f"{i + 1} - {acounts[i]} - ${balances[i]}")

    update = input("Do you want to update an acount? (y/n): ")

    if update == "y":
        index = int(input("Type the acount number to update: ")) - 1
        new_amount = float(input("What is your new amount? "))

        balances[index] = new_amount



# Ask for the index of the element to change

# Ask for the new amount
print("\nAccount Information:")
for i in range(len(acounts)):
    
    total += balances[i]
    if highest_value < balances[i]:
        highest_value = balances[i]

average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
print(f"Your highest value is: ${highest_value:.2f}")







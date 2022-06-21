

child_meal_price = float(input("What is the price of a child's meal? $" ))
adult_meal_price = float(input("What is the price of a adult's meal? $" ))
childrens = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? $'))

childs_meal_total = child_meal_price * childrens

adult_meal_total = adult_meal_price * adults

subtotal = childs_meal_total + adult_meal_total
print()
print(f'Subtotal:  ${subtotal:.2f}')
sales_tax = subtotal * tax_rate / 100
print(f'Sales tax: ${sales_tax:.2f}')
total = subtotal + sales_tax
print(f'Total: ${total:.2f}')
print()

payment_amount = float(input('What is the payment amount? $'))
change = payment_amount - total
print(f'change: ${change:.2f}')



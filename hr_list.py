with open("hr_system.txt") as hr_list:
    for line in hr_list:
        line = line.strip().split(' ')
        name = line[0]
        id_number = line[1]
        title = line[2]
        salary =  float(line[3])
        pay_check = salary / 24

        if title == 'Engineer':
            pay_check += 1000
        print(f"Name: {name}, (id:{id_number}) Title: {title} - ${pay_check:,.2f} ")


print('The file is closed now')












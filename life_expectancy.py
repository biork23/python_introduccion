# import statistics 

# chosen_year = int(input('Enter the year of interest: '))
# print()

# with open('life-expectancy.csv') as life_expectancy:
#     next(life_expectancy)
    
    
#     output = []
#     value = 0
#     average = 0


    
#     for data in life_expectancy:
#         clean_data = data.strip()
#         split_data = clean_data.split(',')

#         entity = split_data[0]
#         code = split_data[1]
#         year = int(split_data[2])
#         expectancy = float(split_data[3])
#         value += expectancy
      
    
#         output.append({'entity': entity, 'code': code, 'year': year, 'expectancy': expectancy})



# max_life = max(output, key=lambda x: x['expectancy'])
# min_life = min(output, key=lambda x: x['expectancy'])

# average = value / len(output)



# print(f'The overall max life expectancy is {max_life["expectancy"]:.2f} in {max_life["entity"]}')
# print(f'The overall min life expectancy is {min_life["expectancy"]:.2f} in {min_life["entity"]}')
# print()
# if chosen_year == year:
#     year = chosen_year

# print(f'For the year {chosen_year}:')
# print()
# print(f'The average life expectancy across all countries was {average:.2f}')


import csv

year_input = input('Enter the year: ')

with open('life-expectancy.csv') as file:
    reader = csv.reader(file)
    lines = []    

    
    for line in reader:
        if line == ['Entity', 'Code', 'Year', 'Life expectancy (years)']:
            pass
        else:
            if line[2] == year_input:
                lines.append(line)
                
   

    average = sum(map(lambda x: float(x[3]), lines))/len(list(map(lambda x: x[3], lines)))
    minimum = min(map(lambda x: x[3], lines))
    maximum = max(map(lambda x: x[3], lines))
    
    print('For the year ' + year_input + ':')
    print('The average life expectancy across all countries was ' + str(average))
    
   
    
    for line in lines:
        if line[3] == minimum:
            print('The min life expectancy was in ' + line[0] + ' with ' + line[3])
        if line[3] == maximum:
            print(f'The max life expectancy was in ' + line[0] + ' with ' + line[3])








        
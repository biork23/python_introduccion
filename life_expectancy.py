import statistics 

chosen_year = int(input('Enter the year of interest: '))
print()

with open('life-expectancy.csv') as life_expectancy:
    next(life_expectancy)
    
    
    output = []
    value = 0
    average = 0


    
    for data in life_expectancy:
        clean_data = data.strip()
        split_data = clean_data.split(',')

        entity = split_data[0]
        code = split_data[1]
        year = int(split_data[2])
        expectancy = float(split_data[3])
        value += expectancy
      
    
        output.append({'entity': entity, 'code': code, 'year': year, 'expectancy': expectancy})



max_life = max(output, key=lambda x: x['expectancy'])
min_life = min(output, key=lambda x: x['expectancy'])

average = value / len(output)



print(f'The overall max life expectancy is {max_life["expectancy"]:.2f} in {max_life["entity"]}')
print(f'The overall min life expectancy is {min_life["expectancy"]:.2f} in {min_life["entity"]}')
print()
if chosen_year == year:
    year = chosen_year

print(f'For the year {chosen_year}:')
print()
print(f'The average life expectancy across all countries was {average:.2f}')








        
# print('Hello world!')

# color = input('Please type your favorite color!')
# print('Awesome your favorite color is')
# print(color)

# first_name = input('What is your first name?')
# second_name = input('What is your second name?')

# # output = 'your name is {}, {} {}'.format(second_name, first_name, second_name)
# output = f'Your name is {second_name}, {first_name} {second_name}.'
# print(output)

# print('Please enter the folowing: ')

# adjective = input(' Enter an adjective: ')
# animal = input('Enter an animal: ')
# verb1 = input('Enter a verb: ')
# exclamation = input('Enter an exclamation: ')
# verb2 = input('Enter a verb: ')
# verb3 = input('Enter a verb: ')

# output = f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.'

# print (output)

# age = input('How old are you? ')
# user_age = int(age)
# year_older_age = user_age + 1
# older_age_str = str(year_older_age)
# print('On your next birthday, you will be ' + older_age_str)


# eggs_cartons = input('How many eggs cartons do you have? ')
# user_eggs_cartons = int(eggs_cartons)
# total_of_eggs = user_eggs_cartons * 12
# total_of_eggs_str = str(total_of_eggs)
# print('You have ' + total_of_eggs_str + ' ' + 'eggs')

# cookies = input('How many cookies do you have? ')
# people = input('How many people are there? ')
# number_of_cokies = int(cookies)
# number_of_people = int(people)
# cookies_per_person = number_of_cokies / number_of_people
# cookies_per_person_str = str(cookies_per_person)
# print('Each person may have ' + cookies_per_person_str + ' ' + 'cookies')

import math


square_side= input('What is the length of a side of the square? ')
square_int = int(square_side)
square_area = square_int ** 2
print(f'The area of the square is: {square_area}')


rectangle_length = input('What is the length of the rectangle? ')
rectangle_length_int = int(rectangle_length)
rectangle_width = input('What is the width of the rectangle? ')
rectangle_width_int = int(rectangle_width)
rectangle_area = rectangle_length_int * rectangle_width_int
print(f'The area of the rectangle is: {rectangle_area}')

radius = input('What is the radius of the circle? ')
circle_radius = float(radius)
circle_area = math.pi * circle_radius ** 2
print(f'The area of the circle is: {circle_area}')


length_value = input('What is the value of a length? ')
value = float(length_value)
square_area = value ** 2
circle_area = math.pi * value ** 2
cube_volume = square_area ** 3
sphere_volume = 4/3 * math.pi * value ** 3
print(f'The are of square is: {square_area}, The area of the circle is: {circle_area}, The volume of the cube is: {cube_volume} and the volume of the sphere is: {sphere_volume}')



#




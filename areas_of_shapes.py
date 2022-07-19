
import math

def compute_area_square(side):
    return compute_area_rectangle(side, side)

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

def compute_area(shape, value, val2 = 1):
    if shape == "square":
        return compute_area_square(value)
    elif shape == "circle":
        return compute_area_circle(value)
    elif shape == "rectangle":
        return compute_area_rectangle(value, val2)







shape = ""

while shape != "quit":
    shape = input("What shape do you have? ")

    shape = shape.lower()

    area = 0

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area("square", side)
    
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area("rectangle", length, width)
        
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area("circle", radius)
    print(f"The area is {area}")

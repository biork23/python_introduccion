import math

def windspeed_calculation ():
    for x in range (0, 60, 5 ):
        x += 5  
        if si_temperature == "C":
            temperature_new = (temperature *9/5) + 32
            Wind_Chill = 35.74 + (0.6215*temperature_new) - 35.75*(x**0.16) + (0.4275*temperature_new *(x**0.16))
            print (f"At temperature {temperature_new}F, wind speed at {x}MPH. The windchill is: {Wind_Chill:.2f}F")
        elif si_temperature == "F":
            Wind_Chill = 35.74 + (0.6215*temperature) - (35.75* (x**0.16)) + (0.4275*temperature*(x**0.16))
            print (f"At temperature {temperature}F, and wind speed at {x}MPH. The windchill is: {Wind_Chill:.2f}F. ")
    

    
temperature = float(input("What is the temperature? "))
si_temperature = input ("Fahrenheit or Celsius (F/C)? " ).upper()   
print()
windspeed_calculation()



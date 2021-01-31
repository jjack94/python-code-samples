# James Jack
# 1/28/21
# this program takes input as degrees F and converts it to degrees C
fahrenheit = input("what is the temperature in degrees fahrenheit?")
fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * 5 / 9
print('your conversion from Fahrenheit to Celsius is %0.2f degrees Celsius' % celsius)

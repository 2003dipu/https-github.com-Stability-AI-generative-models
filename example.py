# This is our created module. We can use this entire file as a module on other files
# Module = a file containing code you want to use in your program
#          use 'import' to include a module (built-in or create your own)
#          useful to breakup a large program into reusable separate files

#print(help("modules"))
#import math # or import mast as m
#import math as m
#from math import pi = is more abmiguious. Better not use it

pi = 3.1416

def square(x):
    return x**2
def cube(x):
    return x **3
def circumference(radius):
    return 2*pi * radius
def area(radius):
    return pi* radius **2
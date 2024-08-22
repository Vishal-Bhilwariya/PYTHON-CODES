#functions

# 1)IN-BUILT FUNCTIONS -> int()  & str() & bool() etc.

# 2)MODULE FUNCTION -> Multiple function stored in a single function called MODULE FUNCTION. Eg:math
import math
print(dir(math))  #by this we can print all function which is in math

#to use any function from math
from math import pow
print(pow(2,10))
from math import sqrt
print(sqrt(625))

#if u wants to use multiple function fro math then
from math import *
print(pow(2,10))
print(sqrt(625))

# 3)USER DEFINED FUNCTION ->

def sum(a,b,c): #user defined function
    print(a+b+c) 
sum(14,54,32)      #call the function
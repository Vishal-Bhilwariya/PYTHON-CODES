#PYHTON_NOTES_BY_APNA_COLLEGE_BY_SHRADHA_MAM

#**************************************** < NEW TOPIC > *****************************************#
#variables

# here 'name' and 'age' are variables

name = "VISHAL BHILWARIYA"    # string
age = 18                      #number

# we can modify name and age

name = "himanshu"
age = 19
print(name)
print(age)

is_adult = True   # boolean varibale

# variable can be integer,float ,string and boolean(true or false)

#**************************************** < NEW TOPIC > *****************************************#
#type conversion

old_age = input("your age = "  )

# new_age = old_age + 2  
# this is syntax error as old_age is consider as string by compiler and 2 is as number . So, we cant add them 

# to overcome this problem we do "TYPE CONVERSION OR TYPECASTING"

new_age = int(old_age) + 2

print(new_age)

''' 
Type conversion can be of four types :
   1) int()
   2) float()
   3) str()
   4) bool()
'''

num = 34
print(float(num))

#sum of two number
num = input("a = ")
num2 = input("b = ")

# sum = num + num2  # this will not add ( if num =1 & num2 = 4 then output according to this line is 14)
# print("sum of a and b = " + sum) # this will also give error bcoz can only add string not intger to an string

#to overcome this problem we use type conversion

sum = int(num) + int(num2)
print("sum of a and b = " + str(sum))

#**************************************** < NEW TOPIC > *****************************************#
#string

name = "Vishal Bhilwariya"

print(name.upper())   #this will convert string in upper case in new string
print(name.lower())   #this will convert string in lower case in new string
print(name.find('w')) #this will find 'w' in string and will return the index ( note - if not present in string then -1 will print)
print(name.replace("Vishal" , "SIR")) #this will replace the required string with new one

# NOTE - THE ABOVE CHANGES WILL NOT REFLECT IN ORIGINAL STRING . IT WILL REMAINS SAME

print(name) 

#**************************************** < NEW TOPIC > *****************************************#
#shortcuts and operator precedence
# shortcuts

i = 2
i += 2  
i -= 2
i *= 2

# precedence ->   " / * + - "

#**************************************** < NEW TOPIC > *****************************************#
#keywords
# to check the character or string is present or not

name = "VISHAL SIR"
print('S' in name)
print('y' in name)

#input by user

name = input("WHAT IS YOUR NAME : ")
print("HELLO " + name)   # concatation ( means adding two string )

#comparison

print(4 > 5)
print(4 < 5)
print(4 >= 5)
print(4 <= 5)
print(4 == 5)
print(4 != 5)

# the above data will give output in boolean (true or false only)

#**************************************** < NEW TOPIC > *****************************************#
#arthimetic

print(2+4)
print(2-4)
print(2*4)
print(2/4)  #this will give int or float both
print(2//4)  # this will give only int
print(2%4)
print(2**4)  # 2 pow 4

#**************************************** < NEW TOPIC > *****************************************#
#logical operators

print( 2>3 or 2<4 )   # or means any one of them should be true to get true
print( 2>3 and 2<4 )  # and means both have to true to get true
print( not 2>3 )      # not means reverse of the condition if it is true then it will print false and vice versa

#**************************************** < NEW TOPIC > *****************************************#
#if else

age = int(input())
if age>=18:
    print("you can vote")
    print("id generate")
elif age<18 and age>3:
    print("you can not vote")
    print("id not generate")
else:
    print("INCORRECT DATA")    
print("THANK YOU")    

# Note -> the spaces in 5 and 6 lines tells that both lines are in if condition and 10 line telling that line is not in if condition

#**************************************** < EXERCISE > *****************************************#
#CALCULATOR (a mini project)

sign = input("symbol(+,-,/,*,%) =" )
a = int(input("a = ") )
b = int(input("b = ") )

if sign == '+' :
    print("a+b = ",a+b)
elif sign == '-' :
    print("a-b = ",a-b)
elif sign == '/' :
    print("a/b = ",a/b)
    print("a//b = ",a//b)
elif sign == '*':
    print("a*b = ",a*b)
elif sign == '%' :
    print("a%b = ",a%b)    
else:
    print("WRONG CHOICE")                             

#**************************************** < NEW TOPIC > *****************************************#
#range

print(range(5)) # means 0 1 2 3 4
print(range(10)) # means 0 1 2 3 4 5 6 7 8 9
 
#**************************************** < NEW TOPIC > *****************************************#
#while loop

i = 0
while i<=5:   #CONDITION
    print(i)   #STATEMENT
    i+=1       #INCREMENT 

# star triangle
j=0
while j<=5:   #CONDITION
    print(j* "*")   #STATEMENT
    j+=1       #INCREMENT     

print(" ")
# star reverse triangle
k=5
while k>=0:   #CONDITION
    print(k* "*")   #STATEMENT
    k-=1       #DECREMENT         

 #for loop

for i in range(5):   #range(0,5)
    print(i)
    i+=1

#**************************************** < NEW TOPIC > *****************************************#
#lists

marks = [23,45,6,78,'maths']  #marks are lists here containing number as well as character

print(marks)  #it will print whole list
print(marks[0])   #it will only print value at index o (marks[0] = 23)
print(marks[-1])  #it will print value start from last index {last index will consider as -1 and then decreasing to left }

#if we want between index value then
print(marks[1:4]) #it will include index from 1 to 4 (4 is not included)

#FOR loops in LISTS

for score in marks:
    print(score)   #score starts from 0 , end with last index of marks and print their respective value

#to add any data to lists at end 
marks.append('air')    
print(marks)

#to add any data in between any index
marks.insert(3,'vishal')
print(marks)

#to check any data which is present in lists or not
print(6 in marks)   #here "in" function is working for check

#to find lenght of lists
print(len(marks))

#WHILE loops in LISTS
i=0
while i<len(marks):
    print(marks[i])
    i=i+1

#to clear (delete) the lists
marks.clear()
print(marks)    

#**************************************** < NEW TOPIC > *****************************************#
#break and continue 

#use of break { to stop printing after that match }
name = ['VISHAL','HIMANSHU','ROHIT','SANDEEP','HARSH','SIR']
for name in name:
    if name == "HARSH" :
        break          #it will break the loop when if condition satsified
    print(name)

#use of continue { to skip that match part and continue }
name = ['VISHAL','HIMANSHU','ROHIT','SANDEEP','HARSH','SIR']
for name in name:
    if name == "HARSH":
        continue
    print(name)          

#**************************************** < NEW TOPIC > *****************************************#
#tuple
marks = (1,2,3,4,1,1,4,3,2,5,4,1)

print(marks.index(1))
print(marks.count(1))

# NOTe :  IN LISTS WE CAN MODIFY AFTER DECLARATION BUT IN TUPLE WE CAN'T.
#**************************************** < NEW TOPIC > *****************************************#
#sets
marks = {1,2,3,1,4,1,34,12,1}
print(marks)    # in sets all unique value will print { repeated value will not}

# sets does not contain index thats why they called as unordered

#**************************************** < Note > **********************************************#
#Note :a> [] is used for LISTS
#      b> () is u sed for TUPLES -> if not used () it is correct. 
#        name = "r","fg"  -> this is tuple by default 
#      c> {} is used for SETS  

#**************************************** < NEW TOPIC > *****************************************#
#dictionary
marks = {"phy" : 63,"chem" : 75,"maths" : 92  }
print(marks)  #it will print whole
print(marks["maths"]) #it will print only maths marks
marks["eng"] = 99  #it will add engl marks
print(marks)

marks["phy"] = 72  #can modify
print(marks)

#**************************************** < NEW TOPIC > *****************************************#
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

#**************************************** < THE END > *****************************************#
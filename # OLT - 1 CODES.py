## => OLT - 1 CODES <= ##

""" 1: Simple Interest
Scenario: You are given Principal Amount P, rate R and time T. Calculate Final Amount with Simple Interest on it.
Input Format
A single line containing P, R and T space separated
Constraints
0 < P,R, T < 100000
Output Format
An integer representing the total amount.
Sample Input 0
Sample Output 0
2000 """
p = int(input("Enter principle amount => "))
r = int(input("Enter rate => "))
t = int(input("Enter time => "))
final_amt = ( p * r * t ) /100
print("The final amount => ",final_amt)

""" 2): Compound for 2 years
Scenario: You are given time = 2 Years. You have to take the Principal Amount P and rate R from the user and calculate and print compound interest.
Input Format
A single line containing P and R space separated
Constraints
0 < PR < 100000
Output Format
A number representing compound interest rounding upto 2 decimal places.
Sample Input 0
10000 2
Sample Output 0
404.00 
"""
p = int(input("Enter principle amount => "))
r = int(input("Enter rate => "))
t = int(input("Enter time => "))
n = 2
final_amt = p * ( 1 + r / 100 )**(t)
print("The final amount => ",final_amt)

""" 3: Wonderful Chocolate Offer
Scenario: You have an uncle who daily gives you D chocolates up to N days. Also, you have C chocolates already but your parents allow you only to eat one chocolate per day. Calculate the total chocolates at the end of N days.
Input Format
Space separated C, N and D
Constraints
0 <C., N < 1000000
Output Format
Single Integer representing the total chocolates at the end of N days.
Sample Input 0
555
Sample Output 0 """ 

c = int(input("Enter chocalate u have already => "))
n = int(input("Enter total days  => "))
d = int(input("Enter chocalate uncle gives u per day => "))
res = (c + n*d ) - n
print(f"Total chocalate at end of {n} day => ",res)

""" 5: Encoded Name
Scenario: It is given that the name contains five characters. You are given the ASCII value of each character separated by &. Now you have to decode it and find that Funny name.
Input Format
Five & symbol-separated integers representing the ASCII value of the character at that position.
Constraints
0 <W1,W2,W3,W4,W5 < 255
Output Format
A single line containing five characters representing the name.
Sample Input 0
80&69&65&75&85
Sample Output 0
PEAKU 
"""

a = int(input("Enter total character => "))
b = input("Enter the code => ").split("&")
for i in range(len(b)):
    print(chr(int(b[i])),end="")

""" 6: Number System
Scenario: Print an entered value in Decimal, Octal and Hexadecimal format.
Input Format
1. Take an integer number n from the user.
Constraints
1. n<=100000000
2. n>=-100000000
Qutput Format
1. Print the value in Decimal.
2. Print the value in Octal.
3. Print the value in Hexadecimal(small letters).
4. Print the value in Hexadecimal(capital letters).
ALL in one single line
Sample Input 0
15
Sample Output 0
15 17 f
"""

n = int(input("Enter any number =>"))
print(n,(oct(n))[2:],(hex(n))[2:])

""" FLOOR AND CEIL FUNCTION"""
import math
a = float(input("enter a float number => "))
print(math.floor(a))
print(math.ceil(a))

""" ASCII VALUE """
a = input("enter a charcter => ")
print(ord(a))

""" 10) HELLO ME """
name = input("enter your name => ")
print("Welcome ",name)

""" 11) SWAPPING """
a = int(input("enter first number => "))
b = int(input("enter second number => "))
print("befor swap :",a,b)
a,b = b,a
print("after swap :",a,b)

""" 12) REMAINDER """
import math
n1 = int(input("enter first number => "))
n2 = int(input("enter second number => "))
c = n1 / n2
rem = (c - int(c))*n2
print(rem) # without using math module
print(math.remainder(n1,n2)) # by the use of math module

""" 13) PLUS OPERATOR => WITHOUT USING PLUS OPERATOR , add two number  """ 
n1 = int(input("enter first number => "))
n2 = int(input("enter second number => "))
lst = [n1,n2]
print(sum(lst))

""" 14) FEET TO INCHES """
a = int(input("enter number in feets => "))
print("In inches => ",a*12)

""" FIND MAX THREE WITHOUT USING IF ELSE """
a = int(input("Enter first number = > "))
b = int(input("Enter second number = > "))
c = int(input("Enter third number = > "))
lst = [a,b,c]
print("max number => ",max(lst))

""" 16) even or odd """ 
a = int(input("enter a number => "))
if a%2 == 0 :
    print("even")
else :     
    print("odd") 

""" 17) """
a = input("enter a number => ")
b = a.count("-")
if b == 1 :
    print("negative number => ",int(a))
elif int(a) == 0 :
     print("zero number => ",int(a))   
else : 
     print("positive number => ",int(a))   

""" 18) vowel or consonent """
a = input("enter any character => ")
if a in "aeiouAEIOU":
    print("vowel")
else :
    print("consonent")  

""" 19) leap year """
a = int(input("Enter a year => "))
if (a % 4 == 0 and a % 100 != 0 ) or a % 400 == 0:
    print("leap year")
else :
    print("non-leap year")   

"""  21) prime number """
a = int(input("enter a number => "))
count = 0
for i in range(2,a):
    if a % i == 0 :
        count = 1
if count == 0:
    print("prime")
else :            
    print("not prime")  

""" 22) factorial """
a = int(input("enter a number => "))
fact = 1
for i in range(1,a+1):
    fact *= i
print(fact)      

""" 23) divisible by 5 and 7 """
a = int(input("enter a number => "))
if a % 5 ==0  and a % 7 == 0:
    print("divisible")
else :        
    print(" not divisible")    

""" 24) palidrome check """
a = input("enter = >")
if a == a[::-1]:
    print("palidrome")
else :    
    print("not palidrome")

""" 25) check alphabets """
a = input("enter => ")
if a.isalpha() :
    print("alphabet")
else :    
    print("not a alphabet")

""" 26) perfect square """
from math import sqrt
a = int(input("enter a number => "))
root = sqrt(a)
if root == int(root):
    print("perfect square")
else :    
    print("not a perfect square")

""" 27) absolute number """
a = input("enter = ")
if a.count("-") >= 1 :
    print(int(a[1:]))
else :
    print(a)    

""" 28) sum till n """
a = int(input("enter a number => "))
sum = 0
for i in range(1,a+1):
    sum += i
print(sum)  

""" 29) canddies left """
a = int(input("enter total candies => "))
for i in range(a):
    a -= 1
    print(a,end=" ")

""" 30) even number """
a = int(input("enter a number => "))
for i in range(2,a,2):
    print(i,end=" ")

""" 32) largest number divisible by 3 """
a = list(map(int,input("enter => ").split()))
for i in range(len(a)):
    b = max(a)
    if b % 3 == 0 :
        print(b)
        break
    else :
        a.remove(b)  

""" 33) """
a = input("enter => ").split()
b = len(a[0])
c = a[0]
for i in range(1,len(a)):
    if b > len(a[i]) :
        c = a[i]
print(c)        

""" 34) """
a = int(input("enter first side => "))
b = int(input("enter second side => "))
c = int(input("enter third side => "))
if a == b and b == c and c == a :
    print("equilateral triangle")
elif a == b or b == c or c == a :
    print("isosclenes triangle")
else :
    print("scalene triangle")
  
""" 39) reverse the string """
a = input("enter a string => ")
print(a[::-1])

""" 35) password checker """

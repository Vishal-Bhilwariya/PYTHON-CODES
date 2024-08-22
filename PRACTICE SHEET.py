# # PRATICE QUESTIONS 
# """(1)Write a Python program that takes a student's score as input and prints out their grade according to the following grading system:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# Test Cases:
# Input: 95, Output: A
# Input: 75, Output: C
# Input: 60, Output: D
# Input: 45, Output: F """

# while True :
#     try :
#         score = int(input("Enter student score : "))
#         grade = [90,80,70,60]
#         if score > grade[0]:
#             print("Grade => 'A'")
#         elif score > grade[1]:    
#             print("Grade => 'B'")
#         elif  score > grade[2]:
#             print("Grade => 'C'")
#         elif score >grade[3]:
#             print("Grade => 'D'")
#         else :
#             print("Grade => 'F'")
#         break       
#     except :
#         print("INVALID ENTRY GIVEN BY THE USER .\n<<< PLEASE ENTER AGAIN >>>")    

# """ (2)Write a Python program that calculates the price of a movie ticket based on the age of the person.
# Age 0-3: Free
# Age 4-12: $10
# Age 13-59: $15
# Age 60 and above: $12
# Test Cases:
# Input: 2, Output: Free
# Input: 8, Output: $10
# Input: 45, Output: $15
# Input: 70, Output: $12 """

# while True :
#     try :
#         age = int(input("Enter age :- "))
#         ages = [3,12,59]
#         if age < ages[0]:
#             print("The price of movie ticket is 'FREE'")
#         elif age < ages[1]:
#             print("The price of movie ticket is '$10'")
#         elif age < ages[2]:
#             print("The price of movie ticket is '$15'")
#         else :
#             print("The price of movie ticket is '$12'")
#         break    
#     except :
#         print("INVALID ENTRY GIVEN BY THE USER .\n<<< PLEASE ENTER AGAIN >>>")

# """ (3)Write a Python program that checks whether a given year is a leap year or not. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
# Test Cases:
# Input: 2020, Output: Leap Year
# Input: 1900, Output: Not Leap Year
# Input: 2000, Output: Leap Year
# Input: 2021, Output: Not Leap Year """

# while True :
#     try :
#         year = int(input("Enter the year => "))
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             print("LEAP YEAR")
#         else :
#             print("NOT LEAP YEAR")
#         break
#     except :
#         print("ENTER A VALID YEAR")    

# """ (4) Write a Python program that converts temperature from Celsius to Fahrenheit if the input temperature is greater than or equal to 0, otherwise, convert from Fahrenheit to Celsius.
# Test Cases:
# Input: 100, Output: 212°F
# Input: -40, Output: -40°C
# Input: 68, Output: 20°C
# Input: 10, Output: 50°F """

# while True :
#     try :
#         temp = int(input("Enter temperature => "))
#         if temp <= 0 : 
#             cel = (temp - 32) * (5/9) # from fehrenheit to celsius
#             print("Temperature => ",cel,"°C",sep="")
#         else :
#             feh = (9/5)*temp + 32    # from celsius to fehrenheit
#             print("Temperature => ",feh,"°F",sep="")
#         break
#     except :
#         print("ENTER A VALID TEMPERATURE")  

# """ (5) Write a Python program to calculate the total cost after applying a discount based on the purchase amount. If the purchase amount is greater than 100, apply a 10% discount; otherwise, apply a 5% discount.
# Test Cases:
# Input: 80, Output: $76.00
# Input: 150, Output: $135.00
# Input: 95, Output: $90.25
# Input: 200, Output: $180.00 """        

# while True :
#     try :
#         price = int(input("Enter price of the product => "))
#         dis = 0
#         if price > 100 :
#             dis = (price * 10 ) / 100
#         else :
#             dis = (price * 5 ) / 100
#         print("Final Amount => ",f"{price - dis : .2f}")
#         break
#     except :
#         print("ENTER A VALID PRICE")    

# """ (6) Write a Python program that simulates a traffic light. The program should take an integer input representing the time in seconds, and based on that, determine the color of the traffic light. The timing for each light is as follows:
# Green light: 30 seconds
# Yellow light: 5 seconds
# Red light: 20 seconds
# Test Cases:
# Input: Time: 10, Output: Green
# Input: Time: 35, Output: Yellow
# Input: Time: 60, Output: Red
# Input: Time: 15, Output: Green """

# while True :
#     try :
#         time = int(input("Enter time in seconds => "))
#         total = 30 + 5 + 20 # => green + yellow + red 
#         time %= total
#         if time <= 30 :
#             print("GREEN LIGHT")
#         elif time <= 35 :    
#             print("YELLOW LIGHT")
#         else :
#             print("RED LIGHT")
#         break
#     except :
#         print("<ENTER A VALID TIME >")    

# """ (7) Write a Python program that calculates the total cost of an order based on the purchase amount. If the purchase amount is less than 50, no discount is applied. If the purchase amount is between 50 and 100 (inclusive), apply a 10% discount. If the purchase amount is greater than 100, apply a 20% discount.
# Test Cases:
# Input: Amount: 30, Output: Total cost: $30.00
# Input: Amount: 80, Output: Total cost: $72.00
# Input: Amount: 150, Output: Total cost: $120.00
# Input: Amount: 55, Output: Total cost: $49.50 """

# while True :
#     try :
#         cost = int(input("ENter the price of the product => "))
#         dis = 0
#         if cost < 50 :
#             dis = 0
#         elif cost >= 50 and cost <= 100 :
#             dis = (cost*10)/100
#         else :
#             dis = (cost*20)/100
#         print("Final amount => $",f"{cost - dis : .2f}",sep="")           
#         break 
#     except :
#         print("ENTER A VALID PRICE") 

# """ (8) Write a Python program that takes a single character (a letter) as input and determines whether it is a vowel or a consonant.
# Test Cases:
# Input: Character: b, Output: Consonant
# Input: Character: e, Output: Vowel
# Input: Character: z, Output: Consonant
# Input: Character: i, Output: Vowel """

# while True :
#         a = input("Enter a alphabet => ")
#         if len(a) == 1 and a.isalpha():
#             if a in "aeiouAEIOU":
#                 print(a,"is a vowel")
#             else :
#                 print(a,"is a consonent")
#             break 

# """ (9) Write a Python program that takes three coefficients (a, b, c) of a quadratic equation (ax^2 + bx + c) as input and determines the nature of its roots: real and distinct, real and equal, or imaginary.
# Test Cases:
# Input: Coefficients: 1, -4, 4, Output: Real and equal roots
# Input: Coefficients: 2, 4, 5, Output: Imaginary roots
# Input: Coefficients: 1, -2, 1, Output: Real and equal roots
# Input: Coefficients: 3, 6, 3, Output: Real and equal roots """

# while True :
#     try :
#         a = int(input("Enter coefficient of x^2 => "))
#         b = int(input("Enter coefficient of x => "))
#         c = int(input("Enter  constant => "))
#         check = b**2 - 4*a*c
#         if check > 0 :
#             print("REAL AND DISTINCT ROOTS")
#         elif check < 0 :
#             print("IMAGINARY ROOTS")
#         else :       
#             print("REAL AND EQUAL ROOTS")
#         break    
#     except :
#         print("ENTER A VALID INTEGERS")    

# """ (10) Write a Python program that takes an integer input representing the day number (1 for Monday, 2 for Tuesday, etc.) and prints out the corresponding day of the week.
# Test Cases:
# Input: Day Number: 7, Output: Sunday
# Input: Day Number: 2, Output: Tuesday
# Input: Day Number: 5, Output: Friday
# Input: Day Number: 1, Output: Monday """

# while True :
#     try:
#         a = int(input("Enter number(1-7) => "))
#         if str(a) in "1234567":
#             dct = {1:"MONDAY",2:"TUESDAY",3:"WEDNESSDAY",4:"THURSDAY",5:"FRIDAY",6:"SATURDAY",7:"SUNDAY"}
#             print(dct.get(a))
#             break    
#     except :
#         print("ENTER A VALID NUMBER BETWEEN (1-7)")    

# """ (11) Write a Python program that takes a string as input and determines whether it is a palindrome or not. A palindrome is a word that reads the same backward as forward.
# Test Cases:
# Input: Word: hello, Output: Not a palindrome
# Input: Word: level, Output: Palindrome
# Input: Word: racecar, Output: Palindrome
# Input: Word: python, Output: Not a palindrome """

# a = input("Enter a string => ")
# if a == a[::-1]:
#     print("PALIDROME")
# else :
#     print("NOT A PALIDROME")

# """ (12) Write a Python program that takes a person's age as input and classifies them into one of the following categories:
# Infant: 0-2 years
# Toddler: 3-5 years
# Child: 6-12 years
# Teenager: 13-17 years
# Adult: 18+ years
# Test Cases:
# Input: Age: 1, Output: Infant
# Input: Age: 4, Output: Toddler
# Input: Age: 10, Output: Child
# Input: Age: 16, Output: Teenager """

# while True :
#     try :
#         a = int(input("Enter age => "))
#         if a < 3 :
#             print("Infant")
#         elif a < 6 :
#             print("Toddler")    
#         elif a < 13 :
#             print("Child")    
#         elif a < 18 :
#             print("Teenager")
#         else :
#             print("Adult")  
#         break
#     except :
#         print("Enter a valid age")                                  

# """ (13) Write a Python program that takes a person's weight (in kilograms) and height (in meters) as input, calculates their Body Mass Index (BMI), and then categorizes them into the following categories:
# Underweight: BMI less than 18.5
# Normal weight: BMI between 18.5 and 24.9
# Overweight: BMI between 25 and 29.9
# Obesity: BMI 30 or greater
# Test Cases:
# Input: Weight: 60, Height: 1.70, Output: BMI: 20.76, Normal weight
# Input: Weight: 80, Height: 1.80, Output: BMI: 24.69, Normal weight
# Input: Weight: 90, Height: 1.65, Output: BMI: 33.06, Obesity
# Input: Weight: 50, Height: 1.60, Output: BMI: 19.53, Normal weight """

# while True :
#     try :
#         wt = int(input("Enter weight in kg => "))
#         h = float(input("Enter height in meters => "))
#         BMI = wt/(h**2)
#         if BMI < 18.5 :
#             print("UNDERWEIGHT WEIGHT")
#         elif BMI < 24.9 :
#             print("NORMAL WEIGHT")  
#         elif BMI < 29.9 :
#             print("Overweight") 
#         else :
#             print("OBESITY")   
#         break     
#     except :
#         print("INVALID DETAILS")    

# """ (14) Write a function count_vowels(s) that takes a string s as input and returns the count of vowels (a, e, i, o, u) in the string.
# Test cases:
# Input: "hello"
# Output: 2
# Input: "Python"
# Output: 1
# Input: "programming"
# Output: 3
# Input: "aeiou"
# Output: 5 """

# def count_vowels(s):
#     count = 0
#     for i in range(len(s)):
#         if s[i] in "aeiouAEIOU":
#             count += 1
#     return count
# s = input("Enter a string => ")
# print(count_vowels(s))

# """ (15) Write a function reverse_string(s) that takes a string s as input and returns the reversed string.
# Test cases:
# Input: "hello"
# Output: "olleh"
# Input: "Python"
# Output: "nohtyP"
# Input: "programming"
# Output: "gnimmargorp"
# Input: "racecar"
# Output: "racecar" """

# def rev(s):
#     return s[::-1]
# s = input("Enter a string => ")
# print(rev(s))

# """ (16) Write a function sum_of_squares(n) that takes an integer n as input and returns the sum of squares of all numbers from 1 to n.
# Test cases:
# Input: 5
# Output: 55
# Input: 3
# Output: 14
# Input: 7
# Output: 140
# Input: 1
# Output: 1 """

# def sum_of_squares(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i**2
#     return sum
# print(sum_of_squares(int(input("Enter a number => "))))      

# """ (17) Write a function is_palindrome(s) that takes a string s as input and returns True if the string is a palindrome, and False otherwise.
# Test cases:
# Input: "radar"
# Output: True
# Input: "python"
# Output: False
# Input: "level"
# Output: True
# Input: "racecar"
# Output: True """  

# def palindrome(s):
#     if s == s[::-1]:
#         print("True")
#     else :    
#         print("False")
# palindrome(input("enter a string => "))        

""" (18) Write a function prime_factors(n) that takes an integer n as input and returns a list of prime factors of n.
Test cases:
Input: 12
Output: [2, 2, 3]
Input: 30
Output: [2, 3, 5]
Input: 56
Output: [2, 2, 2, 7]
Input: 97
Output: [97] """

# def prime(a):


# def prime_factors(n):
#     lst = []
#     for i in range(2,n+1):
#         if n % i == 0 :
#             count = 0
#             for j in range(2,i):
#                 if i % j == 0 :
#                     count = 1
#             if count == 0:
#                 lst.append(i)
#     pro = 1
#     for i in range(len(lst)) :
#         pro *= lst[i]
#     if pro == n :
#         return lst
#     else :
#         for i in range(len(lst)) :
#             n = n // lst[i]
#         for i in range(2,n+1):
#             if n % i == 0 :
#                 count = 0
#                 for j in range(2,i):
#                     if i % j == 0 :
#                         count = 1
#                 if count == 0:
#                     lst.append(i)        

# n = int(input("enter a number = > "))
# print(prime_factors(n))   

""" (19) Write a function pascals_triangle(n) that takes an integer n as input and returns the first n rows of Pascal's triangle as a list of lists.
Test cases:
Input: 3
Output: [[1], [1, 1], [1, 2, 1]]
Input: 5
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
Input: 7
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
Input: 1
Output: [[1]] """                     

""" (20) Write a function sum_of_primes(n) that takes an integer n as input and returns the sum of the first n prime numbers.
Test cases:
Input: 5
Output: 28
Input: 7
Output: 58
Input: 10
Output: 129
Input: 15
Output: 583 """

# def sum_of_primes(n) :
#     s = 0
#     count = 0
#     a = 2
#     while n > 0 :
#         for i in range(2,a):
#             if a % i == 0 :
#                 count = 1
                
#         if count == 0 :
#             s += a    
#             n -= 1
#         a += 1
#     return s    

# k = int(input("enter a number => "))
# print(sum_of_primes(k))            

""" (21) Write a function is_magic_square(matrix) that takes a list of lists matrix representing a square matrix as input and returns True if the matrix is a magic square (the sum of numbers in each row, each column, and each diagonal are the same), and False otherwise.
Test cases:
Input: [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
Output: True
Input: [[16, 23, 17], [78, 32, 21], [17, 16, 15]]
Output: False
Input: [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
Output: True
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: False """

def is_magic_square(matrix):
    row = []
    coul = []
    dia = 0
    order = len(matrix)
    for i in range(order):
        a = 0
        for j in range(len(matrix[i])) :
            a += matrix[i][j]
        row.append(a)

    b = 0
    for i in range(order):
            b += matrix[i][0]


    print(row)
a = eval(input("enter your matrix => "))
is_magic_square(a)                
# # python questions

# """
# Question 1: Add Two Numbers Without Using Arithmetic Sum Operator
# Scenario: You're tasked with adding two integers without using the '+' operator.

# Sample Test Cases:

# Inputs: a = 5, b = 3
# Output: 8
# Inputs: a = 10, b = 7
# Output: 17
# Inputs: a = 8, b = 15
# Output: 23
# Inputs: a = 20, b = 20
# Output: 40
# """



# """ Question 5: Find the Bitwise AND of Two Integers
# Scenario: You are working with a system that requires finding the bitwise AND of two integers.

# Sample Test Cases:

# Inputs: a = 5, b = 3
# Output: 1
# Inputs: a = 10, b = 7
# Output: 2
# Inputs: a = 8, b = 15
# Output: 8
# Inputs: a = 20, b = 20
# Output: 20
# """
# # a = int(input("enter first number => "))
# # b = int(input("enter second number => "))
# # print(a&b) 

# # -> working : value of a and b will be converted into binary and then add them and then convert it to original

# """ Question 1: Arithmetic Operators - Addition
# Scenario: You are building a calculator program and need to implement addition functionality using arithmetic operators.

# Sample Test Cases:

# Inputs: a = 5, b = 3
# Output: 8
# Inputs: a = -10, b = 7
# Output: -3
# Inputs: a = 0, b = 0
# Output: 0
# Inputs: a = 100, b = -50
# Output: 50

# Question 2: Arithmetic Operators - Division
# Scenario: You are creating a program to calculate the average of a set of numbers and need to implement division functionality using arithmetic operators.

# Sample Test Cases:

# Inputs: numerator = 10, denominator = 2
# Output: 5.0
# Inputs: numerator = 15, denominator = 3
# Output: 5.0
# Inputs: numerator = 7, denominator = 2
# Output: 3.5
# Inputs: numerator = 20, denominator = 6
# Output: 3.3333333333333335

# """

# def print_formatted(number):
#     for i in range(1,number+1):
#         a = oct(i)
#         b = hex(i)
#         c = bin(i)
#         print(i,a[2:],b[2:].capitalize(),c[2:],sep=" ")

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
age = 34.9

def add(a,b):
    while b != 0 :
        carry = a & b
        a = a ^ b
        b = carry << 1
        return a
print(add(2,3))        
# FUNCTIONS IN PYTHON

# def average(a,b,c,d):
#     return (a+b+c+d)/4

# print(average(12,21,34,5))

"""Practice questions on python lambda functions:
1) Sorting a List of Tuples based on the Second Element:
data = [(1, 5), (3, 2), (8, 10), (4, 3)]
"""


"""
2) Filtering Even Numbers from a List:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = lambda a : a % 2 == 0
# for i in range(len(numbers)):
#     check = even(numbers[i])
#     if check == True :
#         print(numbers[i],end=" ")

"""
3) Mapping Squares of Numbers in a List:
numbers = [1, 2, 3, 4, 5]
"""
# numbers = [1, 2, 3, 4, 5]
# sq = lambda a : a**2
# for i in range(len(numbers)):
#     print(sq(numbers[i]),end=" ")

"""
4) Calculating Exponential Values using Lambda."""


"""
1.Square root of a number
Given a number A. Return square root of the number if it is perfect square otherwise return
-1.
Note: A number is a perfect square if its square root is an integer
"""

# def prfsq(a):
#     out = a**(1/2)
#     if float(int(out)) == out :
#         return int(out)
#     else :
#         return -1

# num = int(input("Enter a number :"))
# print(prfsq(num))

"""
2.Area of Square
You are given a positive integer A denoting the side of a square. You have to calculate the
area of the square.
Area of a square having side S is given by (S * S).
"""

# def sq(s):
#     return s*s
# print(sq(int(input("Enter a number : "))))    

""" 
3.Area of Circle
You are given a positive integer A denoting the radius of a circle. You have to calculate the
area of the circle
"""

# def sq(s):
#     return 3.14*(s**2)
# print(sq(int(input("Enter radius of circle : "))))  





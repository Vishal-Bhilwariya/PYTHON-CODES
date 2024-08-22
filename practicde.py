""" 2. Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

# st = input("enter any string : ")
# lst = []

# for i in range(len(st)):
#     a = st[i] + " : " + str(st.count(st[i]))
#     lst.append(a)
# print(lst)    

""" 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

# st = input("enter any string : ")
# if len(st) > 4 :
#     new_st = st[0] + st[1] + st[len(st)-2] + st[len(st)-1]
#     print(new_st)
# elif len(st) < 2 :
#     print("")
# elif len(st) == 2 :
#     print(st+st,sep="")

""" 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
Sample String : 'restart'
Expected Result : 'resta$t'
"""

# st = input("enter ")
# a = st[0]
# res = "" + st[0]
# for i in range(1,len(st)):
#     if a == st[i]:
#         c = st[i].replace(st[i] , "#")
#         res += c
#     else :
#         res += st[i]    
# print(res)        


""" 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

# st1 = input("enter : ")
# st2 = input("enter : ")

# a = ""
# b = ""
# for i in range(2):
#     a += st2[i]
#     b += st1[i]

# res1 = "" + a
# res2 = "" + b

# for i in range(2,len(st1)):
#     res1 += st1[i]
# for i in range(2,len(st2)):
#     res2 += st2[i]
    

# print("'" + res1 + " " + res2 + "'")      
 

""" 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

# st = input("enter : ")
# a = len(st)
# if a >= 3 and not st.endswith("ing") :
#     print(st + "ing")
# elif st.endswith("ing") :
#     print(st + "ly")    

# else :
#     print(st)

""" 9. Write a Python program to remove the nth index character from a nonempty string. """

# st = input("enter : ")
# res = ""
# for i in range(len(st)-1):
#     res += st[i]
# print(res)    

"""10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. """

# st = input("enter : ")
# a = st[0]
# b = st[len(st)-1]

# res = "" + b
# for i in range(1,len(st)-1):
#     res += st[i]
# print(res + a)    

"""11. Write a Python program to remove the characters which have odd index values of a given string."""

# st = input("enter : ")
# res = ""
# for i in range(len(st)):
#     if i%2 == 0:
#         res += st[i]
#     else :
#         pass
# print(res)        

""" 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""

# lst = ["red", "white", "black", "red", "green", "black"]
# lst.sort()
# res = ""
# a = ""
# for i in range(len(lst)):
#     if lst[i] not in res:
#         res += lst[i]
#         res += ","  
# print(res)

""" Write a python program that takes a single input from the user. If the input is of type integer, print the cube of the integer. If the input value is a float, print the square of the input. If the input is a string, print the string reversed """

# a = eval(input("enter : "))
# if str(a) == a :
#     print(a[::-1])
# elif int(a) == a :
#     print(a*a*a)
# elif float(a) == a:
#     print(a*a)     

""" 15.Count Occurrences
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
Input:
"abobc"

Output:
1
Input:
 "bobob"

Output:
2"""



# string=input()
# substring=input()
# c=0
# for i in range(len(string)):
#     if string[i:].startswith(substring):
#         c+=1
# print(c)

"""
questions = [
    "What is your name?",
    "How old are you?",
    "Where are you from?"
]

for i in range(len(questions)):
    print("Question" , i+1 , ":" , questions[i],end="")
    a = input()
    print("You answered:",a) """

""" A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not. 
Examples: 

Input: n = 15
Output: false
Divisors of 15 are 1, 3 and 5. Sum of 
divisors is 9 which is not equal to 15.

Input: n = 6
Output: true
Divisors of 6 are 1, 2 and 3. Sum of 
divisors is 6.
"""

# n = int(input("enter : "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum += i
# print(sum)        
# if sum == n :
#     print("Number is a prefect number")
# else :
#     print("Number is not a prefect number")        

"""A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits. 
Examples : 

Input : 1412
Output : Spy Number
Explanation : 
sum = (1 + 4 + 1 + 2) = 8
product = (1 * 4 * 1 * 2) = 8
since, sum == product == 8

Input : 132
Output : Spy Number
Explanation : 
sum = (1 + 3 + 2) = 6
product = (1 * 3 * 2) = 6
since, sum == product == 6
"""

# n = input("enter : ")
# sum = 0
# prod = 1
# for i in range(len(n)):
#     sum += int(n[i])
#     prod *= int(n[i])
# if prod == sum :
#     print("a Spy number")
# else :
#     print("not a Spy number")    

"""A number is called an Automorphic number if and only if its square ends in the same digits as the number itself.

Examples : 

Input  : N = 76 
Output : Automorphic
Explanation: As 76*76 = 5776

Input  : N = 25
Output : Automorphic
As 25*25 = 625

Input : N = 7
Output : Not Automorphic
As7*7=49"""

# n = input("enter : ")
# sqr = int(n)*int(n)
# s = str(sqr)
# if s[len(s)-1] == n[len(n)-1]:
#     print("Automorphic number")
# else : 
#     print("not Automorphic number")    

""" The tribonacci series is a generalization of the Fibonacci sequence where each term is the sum of the three preceding terms. 
The Tribonacci Sequence: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852… so on"""

# n = int(input("terms : "))
# a = 0
# b = 0
# c = 1
# print(a,b,c,end=" ")
# for i in range(n):
#     temp = a + b +c
#     a = b
#     b = c
#     c = temp
#     print(temp,end=" ")

""" print and Sum of the series 1 + (1+2) + (1+2+3) + (1+2+3+4) + …… + (1+2+3+4+…+n) """

# n = int(input("term : "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     print(sum,end=" + ")

""" Program to find the sum of a Series 1/1! + 2/2! + 3/3! + 4/4!+…….+n/n! """ 

# n = int(input("term : "))
# a = 1
# for i in range(1,n+1):
#     fact = 1
#     for i in range(1,i+1):
#         fact *= i   
    
#     print(a,"/",fact,sep="",end=" + ")
#     a += 1

""" Program to find sum of series 1 + 1/2 + 1/3 + 1/4+..+1/n """
# n = int(input("term : "))
# a,b,sum = 1,1,1
# for i in range(1,n):
#     b += 1
#     sum += a/b
# print(sum)    

""" Print and Find sum of the series 1-2+3-4+5-6+7…… """ 

# n = int(input("term : "))
# sum = 0
# sum2 = 1
# print("series")
# print(1,end=" - ")
# for i in range(2,n+1):
#     if i%2 != 0:
#         print(i,end=" - ")
#         sum += i
#     else :
#         print(i,end=" + ")   
#         sum2 -= i
# print("")        
# print("sum is ",sum+sum2)   


""" Given a number N. The task is to write a program to find the N-th term in the below series: 
 

0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 6, 14, 7, 16, 8,…..


Examples: 
 

Input : N = 10
Output : 4

Input : N=7
Output:6"""

# lst = [0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 6, 14, 7, 16, 8]
# n = int(input("enter nth number :"))
# print(lst[n+1])

""" Here we are going to find the sum of the series 1 + 11 + 111 + 1111 +…..upto N terms (where N is given).
Example : 
Input : 3
Output : 1 + 11 + 111 +....
Total sum is : 123

Input : 4
Output : 1 + 11 + 111 + 1111 +..... 
Total sum is : 1234

Input : 7
Output : 1 + 11 + 111 + 1111 + 11111 + 
         111111 + 1111111 +..... 
Total sumis:1234567"""


# n = int(input("term : "))
# lst = []
# for i in range(1,n+1):
#     print("1"*i, end= " + ")
#     lst.append("1"*i)

# sum = 0
# for i in range(n):
#     sum += int(lst[i])  
# print("\n",sum)    
    
""" prime number """
# n = int(input("enter number : "))
# count = 0
# for i in range(2,n):
#     if n % i == 0:
#         count = 1
# if count == 0:
#     print("prime")
# else :
#     print("not prime")                

""" armstrong number """
# n = input("enter number : ")
# a = len(n)
# sum = 0
# for i in range(a):
#     sum += int(n[i])**a
# if int(n) == sum :
#     print("armstrong numbee")
# else:
#     print("not a armstrong numbee") 



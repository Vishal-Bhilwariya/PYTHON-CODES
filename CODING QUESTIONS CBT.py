#_______________________CODING-QUESTIONS-1-CBT_______________________________#

# ---------------------- < PART - 1 > ----------------------------------

# 1. Read a number and check if it is divisible by 7.
"""a = int(input("enter a number => "))
print("TRUE") if a % 7 == 0 else print("FALSE")"""
# 2. WAP to check if number last digit is 4. 
"""a = input("enter a number => ")
print("TRUE") if a[len(a)-1] == "4" else print("FALSE")"""
# 3. WAP to check the number is divisible by 3 and last digit is 4
"""a = input("enter a number => ")
print("TRUE") if a[len(a)-1] == "4" and int(a) % 3 == 0 else print("FALSE")"""
# 4. WAP to check the number is divisible by 7 or last digit is 5.
"""a = input("enter a number => ")
print("TRUE") if a[len(a)-1] == "5" and int(a) % 7 == 0 else print("FALSE")"""
# 5. Take an integer A as input. You have to tell whether A is divible by both 5 and 11 or not
"""a = int(input("enter a number => "))
print("TRUE") if a % 5 == 0 and a % 11 == 0 else print("FALSE")"""
# 6. Read three integers and print their maximum. 
"""a , b , c = int(input("first number => ")) , int(input("second number => ")) , int(input("third number => "))
if a > b and a > c : print("max=>",a)
elif b > c and b > a : print("max=>",b)
else : print("max=>",c)"""
# 7. Read Three angles of triangles and determine its types(Right traingle,Obtuse triangle,actute triangle)
"""a , b , c = int(input("first angle => ")) , int(input("second angle => ")) , int(input("third angle => "))
if a + b + c == 180 :
    if a == 90 or b == 90 or c == 90: print("RIGHT ANGLED TRIANGLE")
    elif a < 90 and b < 90 and c < 90 : print("ACUTE TRIANGLE")
    elif a > 90 and b > 90 and c > 90 : print("OBTUSE TRIANGLE")
    else : print("OTHER TYPE OF TRINAGLE")
else :
    print("INVALID TRIANGLE")    """
# 8. WAP to check to check whether a person is eligible for voting or not. 
"""age = int(input("enter age => "))
print("ELIGIBLE TO VOTE") if age > 17 else  print("NOT ELIGIBLE TO VOTE")"""
# 9. WAP to check whether an year is a leap year or not. 
"""a = int(input("enter year => "))
print("leap year") if (a % 4 == 0 and  a % 100 != 0 ) or a % 400 == 0  else print("not a leap year")"""
# 10. WAP to accept a number from 1 to 7 and display the name of day like 1 for sunday, 2 for monday, etc.
"""dt = {1:"MONDAY",2:"TUESDAY",3:"WEDNESSDAY",4:"THURSDAY",5:"FRIDAY",6:"SATURDAY",7:"SUNDAY"}
a = int(input("enter =>"))
print(dt[a]) """
# 11. Given 5 numbers A, B, C, D, E as input. Print the average of these 5 numbers. 
"""a , b , c , d , e = int(input("first no. => ")) , int(input("second no. => ")) , int(input("third no. => ")) , int(input("fourth no. => ")) , int(input("fifth no. => "))
print((a+b+c+d+e)/5)"""
# 12. You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.A triangle is valid if sum of its angles equals to 180. 
"""a , b , c = int(input("first angle => ")) , int(input("second angle => ")) , int(input("third angle => "))
print("valid") if a + b + c == 180 else print("not valid")"""
# 15. Accept the percentage from the user and display the grade according to the following criteria.
# ● Below 25 – D
# ● 25 to 45 – C
# ● 45 to 65 – B
# ● 65 to 85 – A
# ● Above 85 – A+ 
"""a = int(input("enter percentage = >"))
if a > 85 : print("A+")
elif a > 65 : print("A")
elif a > 45 : print("B")
elif a > 25 : print("C")
else : print("D")"""

# ---------------------- < PART - 2 > ----------------------------------

# 1.Write a program that takes a positive integer N as input from the user and prints all natural numbers from 1 to N, with each number followed by a space.
# Input:- N = 5
# Output:- 1 2 3 4 5
"""a = int(input("number => "))
for i in range(1,a+1) : print(i,end=" ")"""
# 2.Write a program to print all Natural numbers from N to 1 where you have to take N as input from user.
# Input:- N = 5
# Output:- 5 4 3 2 1
"""a = int(input("number => "))
for i in range(a,0,-1) : print(i,end=" ")"""
# 3.Write a program to print all even numbers from 1 to N where you have to take N as input from the user.
# Input:- N = 10
# Output:- 2 4 6 8 10
"""a = int(input("number => "))
for i in range(2,a+1,2) : print(i,end=" ")"""
# 4.Write a program to print all odd numbers from 1 to N where you have to take N as input from user.
# Input:- N = 10
# Output:- 1 3 5 7 9 
"""a = int(input("number => "))
for i in range(1,a+1,2) : print(i,end=" ")"""
# 5.Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user
# Input:- N = 10
# Output:- 55
"""a = int(input("number => "))
sum = 0
for i in range(1,a+1) : sum += i
print(sum)"""
# 6.You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A. Even numbers are those numbers that are divisible by 2.
# Input:- A = 5
# Output:- 6
# Explaination:- Even numbers between [1, 5] are (2, 4).
"""a = int(input("number => "))
sum = 0
for i in range(a+1):
    if i %  2 == 0:
        sum += i
print(sum)"""
# 7.Take an integer A as input. You have to print the sum of all odd numbers in the range [1,A].
# Input:- A= 4
# Output:- 4
# Explaination:- For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. Sum = 1 + 3 = 4
"""a = int(input("number => "))
sum = 0
for i in range(a+1):
    if i %  2 != 0:
        sum += i
print(sum)"""
# 8.Take integer N as input and Print the count of digits of that number.
# Input:- N = 10101
# Output:- 5
# Explaination:- 10101 has 5 digits 
"""a = input("numer = >")
print(len(a))"""
# 9.Take integers N as input. Your task is to calculate and print the sum of the digits of the given number N.
# Input:- N = 1589
# Output:- 23
# Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23. 
"""a = input("number => ")
sum = 0
for i in range(len(a)):
    sum += int(a[i])
print(sum)  """  
# => or
"""a = int(input("number => "))
sum = 0
for i in range(len(str(a))):
    rem = a % 10
    sum += rem
    a //= 10 
print(sum) """
# 10.You are given an integer A as input and you need to determine whether it is a palindrome or not. A palindrome integer is one whose digits, when reversed, result in the same number.
# For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome because its reverse is 321.Note: The given integer will not have any leading zeros.
# Input:- A = 131
# Output:- Yes
# Explaination:- For A = 131, reverse(A) = reverse(131) = 131, which is same as A. 
"""a = input("number => ")
print("palidrone") if a == a[::-1] else print("not a palidrone")"""
# 11.Take a number A as input, print its multiplication table having the first 10 multiples.
# Input:-3
# Output:-
# 3 * 1 = 3
#  3 * 2 = 6
#  3 * 3 = 9
#  3 * 4 = 12
#  3 * 5 = 15
#  3 * 6 = 18
#  3 * 7 = 21
#  3 * 8 = 24
#  3 * 9 = 27
#  3 * 10 = 30
"""a = int(input("number => "))
for i in range(1,11):
    print(a,"*",i,"=",a*i)"""
# 12.You are given two integers A and B. You have to find the value of A^B.
# Input:- A = 2 , B = 3
# Output:- 8
# Explaination:- For A=2 and B=3, the value of 2^3 = 2 * 2 * 2 = 8.     
"""a , b = int(input("first number => ")) , int(input("second number => "))
print(a**b)"""

# ---------------------- < PART - 3 > ----------------------------------

# 1.Sum of list
# Given an array compute the sum of all elements.
# Input :-
# A = [1 2 3 4 5]
# Output:
# 15 
"""a = eval(input("enter a list => "))
print(sum(a))"""
# => or
"""a = int(input("enter length of list => "))
lst = []
for i in range(a):
    b = int(input(f"enter number {i+1} => "))
    lst.append(b)
sum = 0
for i in range(a):
    sum += lst[i] 
print(sum)""" 
# 2.Copy the Array
# You are given a constant array A and an integer B.
# You are required to return another array where Arr[i] = A[i] + B.
# Input :-
# A = [1 2 3 2 1]
# B = 3
# Output:
# [4 5 6 5 4]      
"""a = eval(input("enter a list => "))
b = int(input("enter number = >" ))
for i in range(len(a)):
    a[i] += b
print(a) """ 
# 3.Max and Min of an Array
# Take input an array A of size N and write a program to print maximum and minimum
# elements of the input array .Here N represents the length of the array .
# Input :-
# A = [1 2 3 4 5]
# Output:
# 5 1 
"""a = eval(input("enter a list => "))
print(max(a),min(a))"""
# => or 
"""a.sort() 
print(a[len(a)-1],a[0])"""
# => or
"""min = a[0]
max = -1
for i in range(len(a)):
    if min > a[i] :
        min = a[i]
    if max < a[i] :
        max = a[i]
print(max,min)"""            
# 4.Search Element
# You are given array A and an integer B. You have to tell whether B is present in array A or not.
# Input:-
# A = [1 5 9 1]
# B = 5
# Output: 1
"""a = eval(input("enter a list => "))
b = int(input("number => "))
for i in range(len(a)):
    if a[i] == b :
        print(1)
        break """
# 5.Negative Integers
# Write a program to print all negative numbers from input array A of size N.
# Input:-
# A = [1 -5 2 -8 -4]
# Output:
# -5
# -8
# -4 
"""a = eval(input("enter a list => "))
for i in range(len(a)):
    if a[i] < 0 :
        print(a[i])"""
# 6.Even Odd Elements
# For array A, you have to find the value of absolute difference between the counts of even and odd elements in the array.
# Input:
# A = [1 2 3 4]
# Output: 0 
"""a = eval(input("enter a list => "))
ev , od = 0 , 0
for i in range(len(a)):
    if a[i] % 2 == 0 :
        ev += 1 
    else :
        od += 1
print(ev-od) if ev > od else  print(od - ev)"""      
# 7.Separate Odd Even
# You are given an integer array A. You have to print the odd and even elements of array A in 2 separate lines.
# Input: A = [1 2 3 4 5]
# Output:
# 1 3 5
# 2 4 
"""a = eval(input("enter a list => "))
for i in range(len(a)):
    if a[i] % 2 == 0 :
        print(a[i],end=" ") 
print()        
for i in range(len(a)):
    if a[i] % 2 != 0 :
        print(a[i],end=" ")"""
# 8.Square of Array
# You are provided with an integer array A. Return another array B of size same as that of A such that B[i] = A[i]^2
# Input: A=[2, 6, 8, 1]
# Output: [4, 36, 64, 1] 
"""a = eval(input("enter a list => "))
b = []
for i in range(len(a)):
    b.append(a[i]**2)
print(b)    """
# 9.Cube of Array
# You are provided with an integer array A. Return another array B of size same as that of A such that B[i] = A[i]^3
# Input: A=[2, 6, 8, 1]
# Output: [8, 216, 512, 1] 
"""a = eval(input("enter a list => "))
b = []
for i in range(len(a)):
    b.append(a[i]**3)
print(b)"""
# 10.Reverse
# Given an array A, Find the reverse of it. (Solve this question with for loop)
# Input: A = [3, 5, 1, 2, 1, 2]
# Output: [2, 1, 2, 1, 5, 3] 
"""a = eval(input("enter a list => "))
ls = []
for i in range(len(a)-1,-1,-1):
    ls.append(a[i])
print(ls)  """  
# 11. Add two list element:
# Given two lists A1 and A2, each containing integers, write a Python program to compute the element-wise sum of the corresponding elements in the two lists and store the result in a new list.
# Input: A1=[1, 2, 3,4]
# A2=[4, 5, 6,7]
# Output: [5, 7, 9, 11]
"""a = eval(input("enter a list => "))
b = eval(input("enter a list => "))
res = []
if len(a) == len(b):
    for i in range(len(a)):
        res.append(a[i]  + b[i])
    print(res)
else :
    print("both list lenght should be equal") """       
# 12. Find the output :
"""list = [2,4,6,8,10,12,14,16,18,20]
print(list[:]) # => [2,4,6,8,10,12,14,16,18,20]
print(list[::]) # => [2,4,6,8,10,12,14,16,18,20]
print(list[2:5]) # => [6,8,10]
print(list[2:]) # => [6,8,10,12,14,16,18,20]
print(list[2::]) # => [6,8,10,12,14,16,18,20]
print(list[:2]) # => [2,4]
print(list[::2])# => [2,6,10,14,18]
print(list[1::2]) # => [4,8,12,16,20]
print(list[2:10:2]) # => [6,10,14,18]"""
# 13. Find the output :
"""list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(len(list))
print(list[-2 :-5: -1]) 
print(list[-2:])
print(list[-2::])
print(list[:-2])
print(list[::-2])
print(list[::-1])"""
# 14. Find the output :
"""mylist = [1.4, 2, 3, 4, 5]
mylist.reverse()
print(mylist)"""
# 15. Find the output :
"""s = "Hello everyone how are you"
print(s.split())
s = "Hello-everyone-how are you"
print(s.split("-"))
word = 'Suyash:Chaudhary:Noida'
print(word.split(':'))
t = "23456"
print(t.split())
t = "2 3 4 5"
print(t.split())"""
# 16. Find the output :
"""l1 = [1, 2, 3, 5, 8, 9]
l2 = [3, 4, 5 , 6, 7, 10]
result = l1 + l2
print(result)
result1 = l1 * 3
print(result1) """

# ---------------------- < PART - 4 > ----------------------------------

# 1.Vowels vs Consonants
# Write a program to input T strings (S) from user and print count of vowels and consonants in it.
# Input: 2
# List
# Apple
# Output:
# 1 3
# 2 3 
"""n = int(input("enter total string => "))
lst = []
for i in range(n):
    lst.append(input(f"enter {i+1} string => "))
for i in range(n):
    v = 0
    for j in range(len(lst[i])):
        if lst[i][j] in "aeiouAEIOU":
            v += 1
    print(v,len(lst[i])-v) """           
# 3.Is is Palindrome?
# Write a program to input T strings (S) from user and print 1 if it is palindrome otherwise print 0. NOTE:A string is palindrome if it reads the same from backward as from forward.
# Input: 3
# abcba
# axax
# abba
"""a = int(input("enter total string => "))
lst = []
for i in range(a):
    lst.append(input(f"enter {i+1} string => "))
for i in range(a):    
    print(1) if lst[i] == (lst[i])[::-1] else print(0)"""
# 4.Trim (*)
# You are given a character string A. You to trim both leading and trailing asterisk characters('*') in the string and print the resultant string.
# Input: A = "**h*e*l*lo*"
# Output: h*e*l*lo 
# 5.Trim left (*)
# You are given a character string A. You to trim leading asterisk characters('*') in the string and print the resultant string.
# Input:
# A = "**h*e*l*lo*"
# Output: h*e*l*lo*
# 6.Trim right (*)
# You are given a character string A. You to trim leading asterisk characters('*') in the string and print the resultant string.
# Input: A = "**h*e*l*lo*"
# Output: **h*e*l*lo
"""def count(a):
    cou = 0
    for i in range(len(a)):
        if a[i] == "*": cou += 1
        else : break
    return cou        

a = input("enter string => ")
st = count(a) 
b = a[::-1]
en = count(b)
print(a[st:len(a)-en])
print(a[st:]) # trim left
print(a[:len(a)-en]) # trim right
"""
#  7.Reverse the word
# You are given string (A) and you have to print after reversing that. 
"""print(input("enter string = > ")[::-1])"""
# 8.Reverse the order of words
# You are given string (A) and you have to print the reverse order of words.
# Input: Suyash Chaudhary
# Output: Chaudhary Suyash
"""a = input("enter= >" ).split()
res = ""
for i in range(len(a)-1,-1,-1):
    res += a[i] + " "
print(res)    """
# 9.Reverse string
# Write a program to reverse the words present in a string. Check example input/output.
# Input: Everyone loves data science
# Output: enoyrevE sevol atad ecneics
"""a = input("enter a sentence => ").split()
res = ""
for i in range(len(a)):
    res += (a[i])[::-1] + " "
print(res)    """
# 9. tolower()-> Input: A = PythoN Output: python
# 10.toupper() -> Input: A = pYthON Output: PYTHON
# 11.Isalnum() -> Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, print 0.
# Input: A = Python45 Output: 1
# 12.Isalpha()
# Print 1 if all the characters of the character array are alphabetical (a-z and A-Z), else print 0.
# Input: A = Python Output: 1 
"""print(input("enter => ").lower())
print(input("enter => ").upper())
print(input("enter => ").isalnum())
print(input("enter => ").isalpha())"""
# 13.First Occurrence
# You are given a character string A, having length N and an integer ASCII code B.
# You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or report that it does not exist.
# Input: A = "aabbcc"
# B = 98
# Output: 2
"""a = input("enter a string => ")
b = int(input("enter ascii code => "))
for i in range(len(a)):
    if chr(b) == a[i]:
        print(i)
        break"""
# 14.First Occurrence Of Word
# You are given two character strings A and B.
# You have to find the first occurrence of string B in string A, as a substring, and return the starting position of first occurrence.
# A substring is a contiguous sequence of characters within a string. For e.g "at" is a substringin "catalogue".
# Input:
# A = "aabababaa"
# B = "ba"
# Output: 2 
"""a = input("enter a string => ")
b = input("enter sub-string => ")
print(a.find(b))"""
# 15.Count Occurrences
# Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
# Input: "abobc"
# Output: 1
# Input: "bobob"
# Output: 2 
"""a = input("enter string => ")
b = input("enter sub-string => ")
count = 0
for i in range(0,len(a)-len(b)+1):
    if b[:len(b)] == a[i:len(b)+i]:
        count += 1
print(count)"""
# 16.String operations
# Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
# Concatenate the string with itself. Delete all the uppercase letters.
# Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets. Return
# the resultant string after applying the above operations.
# NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
# Input:
# A="aeiOUz"
# Output:
# "###z###z"
"""a = input("enter a string => ")
a += a
res = ""
for i in range(len(a)):
    if a[i] in "aeiou":
        res += "#"
    elif a[i].isupper():
        pass
    else :
        res += a[i]
print(res) """       

# ---------------------- < PART - 5 > ----------------------------------

# Q1.Frequency of Number
# Given N array elements . Find the frequency of element in array. (Solve it by usingdictionary.)
# Input 1: A = [2, 6, 3, 8, 2, 8, 2, 3, 8, 8]
#          B = 2
# Output 1: 3 
"""a = eval(input("enter = > "))
b = int(input("enter a number => "))
count = 0
for i in range(len(a)):
    if a[i] == b :
        count += 1
print(count)
# => or
st = ""
for i in range(len(a)):
    st += str(a[i])
print(st.count(str(b)))"""  
# Q2.Find the first non-repeating element
# Given N array elements . Find the first non-repesting element
# Input 1: A = [1, 2, 3, 1, 2, 5]
# Output 1: 3          
"""a = eval(input("enter a list => "))
for i in range(len(a)):
    if a.count(a[i]) == 1 :
        print(a[i])
        break """
# Q3. Check Palindrome
# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Print 1 if it is possible to rearrange the characters of the string A such that it becomes a
# palindrome else print 0.
# Example Input
# Input 1: A = "abcde"
# Input 2: A = "abbaee"
# Example Output
# Output 1: 0
# Output 2: 1 
"""st = input("enter a string => ")
if len(st) % 2 == 0 :
    for i in range(len(st)):
        if st.count(st[i]) % 2 != 0 :
            count = 0
            break
        else :
            count = 1
    print(0)  if count == 0 else print(1)
else :
    c1 , c2 = 0 , 0
    for i in range(len(st)): 
        if st.count(st[i]) % 2 == 0:
            c1 += 1
        else :
            c2 +=1
    print(1) if c2 == 1 and c1 == len(st) -1 else print(0) """               
# Q4. First Repeating element
# Given an integer array A of size N, find the first repeating element in it.
# We need to find the element that occurs more than once and whose index of the first
# occurrence is the smallest.
# If there is no repeating element, print -1.
# Example Input
# Input 1:A = [10, 5, 3, 4, 3, 5, 6]
# Input 2:A = [6, 10, 5, 4, 9, 120]
# Example Output
# Output 1:5
# Output 2:-1
"""a = eval(input("enter a list => "))
for i in range(len(a)):
    if a.count(a[i]) >= 2 :
        print(a[i])
        break
else :
    print(-1)    """
# Q5. Merge two Python dictionaries into one
# Input 1: dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Output 1: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 
"""dt1 = eval(input("enter dict-1 => "))
dt2 = eval(input("enter dict-2 => "))
res_dt = {}
dt1.update(dt2)
print(dt1)     """  
# Q6.Check if a value exists in a dictionary
# Input 1: dict1 = {'a': 100, 'b': 400, 'c': 300}
# Output 1: 400 present in a dict 
"""a = eval(input("enter dictionary => "))
b = int(input("enter value => "))
for i in a.values():
    if i == b :
        print(1) 
        break
else :
    print(0)"""
# Q7.Iterate through the keys in the dictionary.
# Input 1: person = {"name": "abc", "age": 25}
# Output 1:
# name
# age    
# Q8.Iterate through the values in the dictionary.
# Input 1:
# person = {"name": "abc", "age": 25}
# Output 1:
# abc
# 25
"""a = eval(input("enter dictionary => "))
print(a.keys())
print(a.values())"""
# Q9 .Iterate through both keys and values in the dictionary.
# Input 1: person = {"name": "abc", "age": 25}
# Output 1:
# name abc
# age 25 
"""a = eval(input("enter dictionary =>  "))
for i,j in zip(a.keys(),a.values()):
    print(i,j)"""
# Q10.Remove all elements from a dictionary.
# Input 1:person = {"name": "abc", "age": 25}
# Output 1:{} 
"""dt = eval(input("enter dictinoary => "))
dt.clear()
print(dt)"""
# Q11.Get a list of all keys in a dictionary.
# Input 1: person = {"name": "abc", "age": 25}
# Output 1: [‘name’ , ‘age’]
# Q12.Get a list of all values in a dictionary.
# Input 1: person = {"name": "abc", "age": 25}
# Output 1: [‘abc’ , 25’]
"""dt = eval(input("enter dictinoary => "))
lst , lst1 = [] , []
for i,j in zip(dt.keys(),dt.values()):
    lst.append(i)
    lst1.append(j)
print(lst)    
print(lst1)  """  
# Q13. Generate a dictionary
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Input 1: N=5
# Output 1: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
"""a = int(input("enter a number => "))
dt = {}
for i in range(1,a+1):
    dt[i] = i**2
print(dt)    """
# Q14. Create a list of tuples from the dictionary
# Input 1: dict1 = { 1: 'a', 2: 'b', 3: 'c' }
# Output 1: [(1, 'a'), (2, 'b'), (3, 'c')] 
"""a = eval(input("enter dictionary => "))
lst = []
for i in range(len(a)):
    tp = ()
    tp = (i+1,a[i+1])
    lst.append(tp)
print(lst)"""
# Q15.Write a code to sort dictionaries using a key.
# Input 1: {2: ‘Apple’, 1:’Mango’, 3:’Orange’, 4:’Banana’}
# Output 1:
# 1 Mango
# 2 Apple
# 3 Orange
# 4 Banana
"""a = eval(input("enter dictionary => "))
lst = []
for i in a.keys():
    lst.append(i)
lst.sort()
for i in range(len(lst)):
    print(a[lst[i]])  """  
# Q16. Common Elements
# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the
# common elements in both the array.
# NOTE:
# ● Each element in the result should appear as many times as it appears in both arrays.
# ● The result can be in any order.
# Example Input
# Input 1:
# A = [1, 2, 2, 1]
#  B = [2, 3, 1, 2]
# Input 2:
# A = [2, 1, 4, 10]
# B = [3, 6, 2, 10, 10]
# Example Output
# Output 1: [1, 2, 2]
# Output 2: [2, 10]
"""a = eval(input("enter first list => "))
b = eval(input("enter second list => "))
lst = []

l1 , l2 = len(a) ,len(b)
for i in range(l1):
    for j in range(l2):
        if a[i] == b[j] :
            lst.append(a[i])
            b[j] = " "
            break
print(lst) """           
# for i in range(l1):
#     c1 = 0
#     for j in range(l2):
#         c2 = 0
#         if a[i] == b[j] :
#             c1 = a.count(a[i])
#             c2 = b.count(b[j])
#             if c1 == c2 :
#                 for i in range(c1//c2):
                    
#                     lst.append(a[i])
#             elif c1 > c2 :
#                 for i in range(c1-c2):
#                     lst.append(a[i])
#             else :
#                 for i in range(c2-c1):
#                     lst.append(a[i])
#         break            
# print(lst)            

# Q17. list of squares
# WAP a Program to Generate a list of squares using list comprehensions.
# Output 1 [1, 4, 9, 16, 25] 
"""a = int(input("enter number => "))
x = [i**2 for i in range(1,a+1)]
print(x)"""
# Q18. Filter even numbers
# WAP a Program to Filter even numbers using list comprehensions.
# Output 1 [2, 4, 6, 8, 10]
"""def check(a):
    if a % 2 == 0:
        return True
a = int(input("enter number => "))
a_c = [i for i in range(1,a+1)]
x = list(filter(check,a_c))
print(x)
# => or
y = [i for i in range(2,a+1,2)]
print(y)"""

# Q19.List of uppercase characters
#  WAP a Program to Create a using list comprehensions
# Input 1:
# text = "hello"
# Output 1:
# ['H', 'E', 'L', 'L', 'O']
"""a = input("enter string => ").upper()
lst = [a[i] for i in range(len(a)) ]
print(lst)"""

# ---------------------- < PART - 6 > ----------------------------------

# 1.Square root of a number
# Given a number A. Return square root of the number if it is perfect square otherwise return -1
# Note: A number is a perfect square if its square root is an integer.
"""from math import sqrt 
a = int(input("enter a number => "))
res = sqrt(a)
print(int(res)) if res == float(int(res)) else print(1)"""
# 2.Area of Square
# You are given a positive integer A denoting the side of a square. You have to calculate the area of the square. Area of a square having side S is given by (S * S). 
"""n = eval(input("side of square => ")) 
print(n*n)  """
# 3.Area of Circle
# You are given a positive integer A denoting the radius of a circle. You have to calculate the area of the circle. 
"""r = eval(input("radius => "))
print(3.14*r*r)"""
# 4.Power function
# You are given two integers A and B.You have to find the value of A^B. 
# 5.Cube It!
# You are given an integer A.You have to find the value of cube of A i.e, A^3. 
"""a , b = eval(input("first number => ")) , eval(input("second number => "))
print(a**b)
print(a**3)
"""
# 6.Volume Of Sphere
# You are given a positive integer A denoting the radius of a sphere. You have to calculate the volume of the sphere.
# Volume of a sphere having radius R is given by (4 * π * R3) / 3.
# NOTE: Since, the answer can be a real number, you have to return the ceil value of the volume. Ceil value of a real number X is the smallest integer that is greater than or equal to X
"""import math
r = eval(input("radius => "))
print(math.ceil(4*3.14*(r**3)/3))"""
# 7.Area Of Ellipse
# Given the lengths of semi-major axis A and semi-minor axis B of an ellipse, calculate the
# Area of the Ellipse.
# Area of ellipse having semi-major axis length a and semi-minor axis length b is given by π * a * b.
# NOTE: Since, the answer can be a real number, you have to return the ceil value of the area.
"""import math
a ,b = eval(input("lenght of semi-major axis A => ")) , eval(input("lenght of semi-major axis B => "))
print(math.ceil(3.14*a*b))"""
# 8.Sum the Array
# Write a program to print sum of elements of the input array A of size N. 
"""n = int(input("enter size of array => "))
# matrix input
lst = []
for i in range(n):
    ls = []
    for j in range(n):
        ls.append(int(input(f"enter element of lst[{i}][{j}] => ")))
    lst.append(ls)   
# matrix element sum
sum = 0
for i in range(n):
    for j in range(n):
        sum += lst[i][j]
print(sum)        """

# ---------------------- < PART - 7 > ----------------------------------

# 1.Add the matrices
# You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
# Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.
# Input:A = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# B = [[9, 8, 7],
#  [6, 5, 4],
#  [3, 2, 1]]
# Output:
# [[10, 10, 10],
#  [10, 10, 10],
#  [10, 10, 10]] 
"""n = int(input("size of matrix => "))
A = []
for i in range(n):
    A.append(eval(input(f"enter {i+1} row for A => ")))
B = []
for i in range(n):
    B.append(eval(input(f"enter {i+1} row for B => ")))    
res = []
for i in range(n):
    ls = []
    for j in range(len(A[i])):
        ls.append(A[i][j] + B[i][j])
    res.append(ls)
print(res)   """ 
# 2.Matrix Transpose
# Given a 2D integer array A, return the transpose of A.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# Input: A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]        
"""n = int(input("size of matrix => "))
A = []
for i in range(n):
    A.append(eval(input(f"enter {i+1} row for A => ")))
res = []
for i in range(n):
    ls = []
    for j in range(n):
        ls.append(A[j][i])
    res.append(ls)
print(res)      """      
# 3.Is It Identity Matrix?
# You are given a N X N square integer matrix A. You have to tell whether A is an identity matrix or not.
# Identity matrix is a special square matrix whose main diagonal elements are equal to 1 and all other elements are 0.
# Input: [[1, 0], [0, 1]]
# Output: 1 
"""n = int(input("size of matrix => "))
A = []
for i in range(n):
    A.append(eval(input(f"enter {i+1} row for A => ")))
c1 , c2 = 0 , 0
for i in range(n):
    for j in range(n):
        if i == j :
            if A[i][j] == 1 :
                c1 += 1
        else :
            if A[i][j] == 0 :
                c2 += 1        
print(1) if c1 == n and c2 == n*n - c1 else print(0)""" 
# 4.Matrix Subtraction
# You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M). You have to subtract matrix B from A and return the resultant matrix. (i.e. return the matrix A - B).
# If A and B are two matrices of the same order (same dimensions). Then A - B is a matrix of the same order as A and B and its elements are obtained by doing an element wise subtraction of A from B.
# Input:
# A = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# B = [[9, 8, 7],
#  [6, 5, 4],
#  [3, 2, 1]]
# Output:
# [[-8, -6, -4],
#  [-2, 0, 2],
#  [4, 6, 8]]                  
"""n = int(input("size of matrix => "))
A = []
for i in range(n):
    A.append(eval(input(f"enter {i+1} row for A => ")))
B = []
for i in range(n):
    B.append(eval(input(f"enter {i+1} row for B => ")))    
res = []
for i in range(n):
    ls = []
    for j in range(len(A[i])):
        ls.append(A[i][j] - B[i][j])
    res.append(ls)
print(res) """
# 5.Are Matrices Same ?
# You are given two matrices A and B of equal dimensions and you have to check whether two matrices are equal or not.
# NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j.
# Input:
# A = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# B = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Output: 1 
"""n = int(input("size of matrix => "))
A = []
for i in range(n):
    A.append(eval(input(f"enter {i+1} row for A => ")))
B = []
for i in range(n):
    B.append(eval(input(f"enter {i+1} row for B => ")))
count = 0    
for i in range(n):
    for j in range(n): 
        if A[i][j] == B[i][j] :
            count += 1
        else :
            count = 0    
print(1) if count == n**n else print(0) """         
# 6. Row & Column Sums
# You are given a matrix A, you have to return an array containing sum of each row elements followed by sum of each column elements of the matrix.
# NOTE: If the matrix given is of size (N x M), then the array you return would be of size (N + M), where first N elements contain the sum of each N rows, and the next M elements contain the sum of each M columns.
# Input: A = [[1, 2],[4, 5],[8, 9]]
# Output: [3, 9, 17, 13, 16] 
"""r , c = int(input("rows of matrix => ")) , int(input("coulmns of matrix => "))
A = []
for i in range(r):
    A.append(eval(input(f"enter {i+1} row for A => ")))
lst = []
for i in range(r):
    sum = 0
    for j in range(c):
        sum += A[i][j]
    lst.append(sum)
for i in range(c):
    sum = 0
    for j in range(r):
        sum += A[j][i]
    lst.append(sum)
print(lst)"""

#-----------------------------------< THANK YOU >---------------------------------------#
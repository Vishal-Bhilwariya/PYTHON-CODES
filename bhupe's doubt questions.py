""" -> : STRING ASSIGNMENT :  <- """

""" 1.Vowels vs Consonants
Write a program to input T strings (S) from user and print count of vowels and consonants in
it. """

# st = input("enter your string : ")
# vowel = 0
# consonent = 0
# vo = "aeiou"
# for i in range(len(st)):
#     for j in range(len(vo)):
#         if vo[j] == st[i] :
#             vowel += 1
# consonent = len(st) - vowel

# print("Total vowels present in string is :",vowel)            
# print("Total consonent present in string is :",consonent)  

""" 2. Length of String - II
You have a string (A).You have to print length of input string """

# st = input("enter your string : ")
# print("The lenght of string is : ",len(st))         

""" 3 Write a program to input T strings (S) from user and print 1 if it is palindrome otherwise print
0. NOTe:A string is palindrome if it reads the same from backward as from forward. """ 

# st = input("enter your string : ")
# rev = st[::-1]
# if st == rev :
#     print("palidrome")
# else :
#     print(0)    

""" 4.Trim (*)
You are given a character string A. You to trim both leading and trailing asterisk
characters('*') in the string and print the resultant string.
Input:
A = "**h*e*l*lo*"
Output:
h*e*l*lo """

# a = "**h*e*l*lo*"

# b = a.removeprefix("*") 
# c = b.removeprefix("*")  
# d = c.removesuffix("*")  
# print(d)        

""" 5.Trim left (*)
You are given a character string A. You to trim leading asterisk characters('*') in the string
and print the resultant string.
Input:
A = "**h*e*l*lo*"
Output:
h*e*l*lo*  """

# a = "**h*e*l*lo*"
# b = a.removeprefix("*") 
# c = b.removeprefix("*")  
# print(c)  

""" 6.Trim right (*)
You are given a character string A. You to trim leading asterisk characters('*') in the string
and print the resultant string.
Input:
A = "**h*e*l*lo*"
Output:
**h*e*l*lo """

# a = "**h*e*l*lo*"
# c = a.removesuffix("*")  
# print(c) 


""" 7.Reverse the word
You are given string (A) and you have to print after reversing that.
Input:
String
Output:
gnirtS """

# st = input("enter ur string : ")
# rev = st[::-1]
# print("reverse string is : ",rev)

""" 8.Reverse the order of words
You are given string (A) and you have to print the reverse order of words.
Input:
Suyash Chaudhary
Output:
Chaudhary Suyash """

# st = input("enter ur string : ")
# total_len = len(st)
# count = 0
# for i in range(total_len):
#     if st[i] != " ":
#         count +=1
#     else :
#         break

# first_part = st[count+1 : ]
# second_part = st[ : count]

# res = first_part + " " + second_part
# print("final string is : ",res)

""" 9.Reverse string
Write a program to reverse the words present in a string. Check example input/output.
Input:
Everyone loves data science
Output:
enoyrevE sevol atad ecneics """

# a = input("enter your string : ")
# b = a.split(" ")
# c = []
# for i in b:
#     c.append(i[::-1])
# print(" ".join(c))

"""10.toupper()
Convert each character of String A into Uppercase character if it exists. If the Uppercase of a
character does not exist, it remains unmodified.The lowercase letters from a to z is converted
to uppercase letters from A to Z respectively.
Print the uppercase version of the given the string.
Input:
A = pYthON
Output:
PYTHON """

# a = input("enter your string : ")
# b = a.upper()
# print(b)        

""" 11.Isalnum()
Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else,
print 0.
Input:
A = Python45
Output:
1
"""

# a = input("enter : ")
# b = a.isalnum()
# if b == True:
#     print(1)
# else :
#     print(0)   


""" 12.Isalpha()
Print 1 if all the characters of the character array are alphabetical (a-z and A-Z), else print 0.
Input:
A = Python
Output:
1"""

# a = input("enter : ")
# if True == a.isalpha():
#     print(1)
# else :
#     print(0)    

""" 13.First Occurrence
You are given a character string A, having length N and an integer ASCII code B.
You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A
or report that it does not exist.
Input:
A = "aabbcc"
B = 98
Output:
2
"""

# a = input("enter ur string : ")
# b = int(input("emter ascii code : "))
# c = chr(b)         # converting ascii code 
# d = a.count(c)
# print(d)

""" 14.First Occurrence Of Word
You are given two character strings A and B.
You have to find the first occurrence of string B in string A, as a substring, and return the
starting position of first occurrence.
A substring is a contiguous sequence of characters within a string. For e.g "at" is a substring
in "catalogue".
Input:
A = "aabababaa"
B = "ba"
Output:
2"""

# a = input("enter string : ")
# b = input("enter sub string : ")

# for i in range(len(b)):
#     for j in range(len(a)):
#         if b[i] == a[j]:
#             print(j) 
#             break
#     break    

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

# a = input("enter any string : ")
# b = "bob"

# print(a.count(b))

""" 16.String operations
Akash likes playing with strings. One day he thought of applying following operations on the
string in the given order:
Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return
the resultant string after applying the above operations.
NOTe: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
Input:
A="aeiOUz"
Output:
"###z###z" """

# a=input("enter your string : ")
# b = a+a
# c = ""
# for i in b:
#     if i.lower() == i:
#         c = c + i
# d = ""
# for i in c:
#     if i in "aeiou":
#         d = d + "#"
#     else:
#         d = d + i
# print(d)     
# 
# 
# ----------------------------------------------------------------------------------------------------------- 
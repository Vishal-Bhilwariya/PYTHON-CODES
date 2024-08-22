# tribonacci seies -> 0 0 1 1 2 4 7 13 24 .....
'''
num = int(input("enter total term : "))
a = 0
b = 0
c = 1
print(a,b,c,end=" ")
for i in range(num):
    temp = c
    c += a + b
    a = b
    b = temp
    
    print(c,end=" ")
    '''



""" 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
       Sample String : 'restart'
       Expected Result : 'resta$t'
"""

# a = input("enter string : ")
# c= a[0]
# b = ""
# for i in range(1,len(a)):
#     if a[i] == 'r':
#         b += "$"
#     else :
#         b += a[i]

# print(c+b)            

"""5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
      Sample String : 'abc', 'xyz'
      Expected Result : 'xyc abz'
"""
# str1 =  input("enter ur string : ")
# str2 =  input("enter ur string : ")

# lst1 = []
# lst2 = []
# for i in range(len(str1)): 
#     if i == 0 or i == 1:
#         lst1.append(str2[i])
#     else :
#         lst1.append(str1[i]) 
# for i in range(len(str2)):
#     if i == 0 or i == 1:
#         lst2.append(str1[i])
#     else :
#         lst2.append(str2[i])        

# # lst1 = lst1 + lst2   
# str1 = ' '.join(lst1)       # join function is used to convert list into string
# str2 = ' '.join(lst2)
# print("'",str1,"  ",str2,"'",sep="") 

# or this solution(below) is taken from chatgpt

# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")

# # Swapping first two characters of each string
# new_str1 = str2[:2] + str1[2:]
# new_str2 = str1[:2] + str2[2:]

# # Combining both strings with a space between them
# result = new_str1 + ' ' + new_str2

# print("'",result,"'",sep="")


'''
n=5
1/1 + 2/2 + 3/6 + 4/24 + 5/120
'''

# a = int(input("enter total terms : "))
# b = 1
# c = 1
# print(c,"/",b,sep="",end="")
# for i in range(2,a+1):
#     c = i
#     b *= c
#     print(" + ",c,"/",b,sep="",end="")

# def fact(a):
#     fact = 1
#     for i in range(1, a+1):
#         fact = fact * i
#     return fact

# num = int(input("Enter max number: ")) #1234567890
# for i in range(1, num+1): # 1 to 1234567890
#     temp = 0
#     for j in str(i):
#         temp = temp + fact(int(j))
#     if temp == i:
#         print(i, end=", ")   
    

""" print all strong number till the maximum number"""  ''' -> strong number is factorial of individual and their sum is equal to that number'''

# for checking only one strong number
# max_num = input("Enter max number(1-9) : ")
# Sum = 0
# for i in range(len(max_num)):       # work only till the lenght of number
#     fact = 1
#     for j in range(1,int(max_num[i])+1):  # work from individual number from that original number 
#         fact = fact * j                   
#     Sum = Sum + fact   

# if Sum == int(max_num):
#     print(Sum,"=",int(max_num),"is a strong number")
# else :    
#     print(Sum,"!=",int(max_num),"is not a strong number")

# for print all strong number till the max number entered by the user


""" #1, 11, 111, 1111,....nth term """
# n = int(input("Enter total term : "))
# k = input("Enter the series term : ")
# print(k,end="")
# for i in range(2, n+1):
#     print(" ,",k*i,end="")

# print("")

"""# code - 1
lst = ["Abhay", "Adarsh", "Ashlesh", "Arjun"]
lstStu = list(enumerate(lst))
for rollno, name in lstStu:
    print("\nRoll No:", rollno+1)
    print("Student Name:",name)  

# code - 2
lst = ["Abhay", "Adarsh", "Ashlesh", "Arjun"]
for i in range(len(lst)):
    print("\nRoll no. : ",i+1)
    print("Student name : ",lst[i]) """


""" enumerate function in python """
# lst = [3,45,7,8,743,56765432,56765,4]
# for i , value in enumerate(lst):
#     print(i,value)

""" check the neon number 
A positive integer whose sum of digits of its square is equal to the number itself is called a neon number """

# num = int(input("Enter a number : "))
# sq = num*num
# sum1 = 0
# while sq > 0:
#     rem = sq % 10
#     sum1 += rem 
#     sq = sq // 10  
# if sum1 == num :
#     print(num,"is a neon number")  
# else:
#     print(num,"is not a neon number")  


"""Given a number x, determine whether the given number is Armstrong’s number or not.

A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Example: 

Input:153
Output: Yes
153 is an Armstrong number.
1*1*1 + 5*5*5+3*3*3=153 """

# num = int(input("enter any number : "))
# copy = copy2 = num
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# sum1 = 0    
# for i in range(count): 
#     rem = copy % 10
#     sum1 += (rem*rem)*rem
#     copy //= 10    
# if copy2 == sum1 :
#     print(copy2,"is a armstrong number ")
# else :        
#     print(copy2,"is not a armstrong number ")

""" find the max occurance of a number in a list """
num = int(input("Enter total term in a list : "))
lst = []
for i in range(num):
    lst.append(int(input("enter list items for index : ")))
print(lst)

max_occ = 0
value = 0
a = len(lst)
print(a)
for i in range(a):
    b = lst.count(lst[i])
    if max_occ < b:
        max_occ == b
        value = lst[i]
    
print(max_occ)        
print(value)        
    


# top 3
       
a = [2,3,4,5,78,56,98,45,67,0]
a.sort()
print(a)
print("first max : ",a[len(a)-1])
print("second max : ",a[len(a)-2])
print("third max : ",a[len(a)-3])


lst = ["vishal","harsh","mayank","mohan","aaditya"]
for rollno , name in enumerate(lst):
    print(rollno,name)


a = int(input())
while a < 4 :
    print("t")
    break
else :
    print("Df")

for i in range(1,4):
    print("t")
    break
else :
    print("f")


# TEST CASE - 01
"""lst1 = [12,3,4,64,2,5]
lst2 = [1,45,64,13,99,10]
lst3 = [100,32,23,99,345]"""
# TEST CASE - 02
"""lst1 = [1,3,4,64,2,5]
lst2 = [10,45,64,13,99,10]
lst3 = [100,32,23,99,345]"""
# TEST CASE - 03
lst1 = [12,3,4,64,2,5]
lst2 = [123,45,64,13,99,10]
lst3 = [1,32,23,99,345]

if lst1[0] < lst2[0] and lst1[0] < lst3[0]:
    if lst2[0] < lst3[0]:
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst1 + lst2 + lst3
        print(lst)
    else :
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst1 + lst3 + lst2 
        print(lst)
elif lst2[0] < lst1[0] and lst2[0] < lst3[0]:
    if lst1[0] < lst3[0]:
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst2 + lst1 + lst3
        print(lst)
    else :
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst2 + lst3  + lst1 
        print(lst)
else :
    if lst1[0] < lst2[0]:
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst3 + lst1 + lst2 
        print(lst)
    else :
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst3 + lst2 + lst1  
        print(lst)

        






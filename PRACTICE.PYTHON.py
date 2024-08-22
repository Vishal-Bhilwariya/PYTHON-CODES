# factorial number
# num = eval(input("enter any number :"))
# sum = 1
# for i in range(1,num+1):
#     sum = sum*i
# print("s=factorial of ",num,"is:",sum)

# # prime number check
# num = eval(input("enter any number : "))
# count = 0
# for i in range(2,num):
#     if num % i == 0:
#         count += 1
# if count == 0:
#     print(num,"is a prime number")
# else :
#     print(num,"is not a prime number")

# # reverse the string
# string = input("enter any string :")
# print(string[::-1])

# #  Write a Python program to check if a given string is a palindrome.

# string = input("enter any string :")
# rev_string = string[::-1]
# count = 0
# for i in range(len(string)):
#     if string[i] == rev_string[i]:
#         count = count + 1
# if count == len(string):
#     print("palidrome")
# else :
#     print("not palidrome")

# # Write a Python program to find the sum of all numbers in a list.
# lst = []
# num = int(input("enter total element in list :"))
# for i in range(num):
#     b = input("enter element:")
#     lst = lst.append("b")
# print("list :",lst)
# sum = 0
# for i in range(num):
#     sum = sum + lst[i]
# print(lst,"is the sum of all element in list")

# Write a Python program to find the largest element in a list.
#size  = int(input("enter size of an list :"))
#lst = []
#for i in range(size):
#    lst.append(int(input()))
#print(lst)    

#max = -1
#for i in range(size):
#    if lst[i] > max:
#        max = lst[i]
#print("maximum number from given list :",max)

# Write a Python program to count the number of vowels in a string.

#str = input("enter any string :")
#count = 0
#for i in range(len(str)):
#    if ( str[i] == 'a' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'e'
#         or str[i] == 'A' or str[i] == 'I' or str[i] == 'E' or str[i] == 'O' or str[i] == 'U' ):
#        count += 1
#print("total vowels present in string :",str,": is ",count)

# Write a Python program to find the intersection of two lists.

#size = int(input("enter size :"))
#lst = []
#lst2 = []
#for i in range(size):
#    lst.append(int(input()))
#print(lst)                
#for i in range(size):
#    lst2.append(int(input()))
#print(lst2)                

#for i in range(size):
#    for j in range(size):
#        if lst[i] == lst2[j]:
#            meet = lst[i]
#print(meet)            

# Write a Python program to sort a list of integers in ascending orde
size = int(input("enter size "))
lst = []
for i in range(size):
    lst.append(int(input()))
print(lst)

max = -1
for i in range(size):
    if max < lst[i]:
        max = lst[i]

for i in range(1,size):
    if max > lst[i] and lst[i] > lst[i+1]:
        lst[i]

        


        

#_______________________CODING-QUESTIONS-2-CBT_______________________________#

#(1)
"""num = input("Enter a number => ")
count = 0
for i in range(len(num)):
    if num[i] in "0" and num[0] != 0:
        count = 1
        break
print("DN") if count == 1 else print("NDN")"""
#(2)
"""num = input("Enter a number => ")
sum = 0
for i in range(len(num)):
    sum += int(num[i])**2
print(sum)"""
#(3)
"""st = input("enter any string => ") 
res_st = ""
for i in range(len(st)):
    if st[i] not in res_st:
        res_st += st[i]
print(res_st) """ 
#(4)
"""lst = eval(input("enter list of numbers => "))
print(max(lst))  """
# (5)
"""def prime(n):
    count = 0
    for i in range(2,n):
        if n % i == 0 :
            count = 1
            break
    if count == 0 : return True 
    else : return False

num = int(input("enter a number => "))
if prime(num) == True and prime(int(str(num)[::-1])) == True :
    print(num,"is a twisted number")"""
# (5)
"""num = int(input("enter a number => "))
temp = 2
while True :
    if temp > num :
        break
    else :
        temp *= 2
print("The number is a Mersenne number") if temp - 1 == num else print("The number is not a Mersenne number") """   
# (6)
"""num = int(input("enter number => "))
temp = str(bin(num))
print(num," is an evil number.") if temp.count("1") % 2 == 0  else print(num, "is not an evil number.")"""
# # (7)
# import random
# name = input("enter name => ")
# if len(name) > 4 :
#     temp = name[1:len(name)-1]
#     ch = random.shuffle(temp)
#     print(name[0]+ch+name[len(name)-1])
# else :
#     print("Name must be at least 4 characters long")    
# (8)
"""st = input("enter a name => ")
if st[0] in "aeiouAEIOU":
    print(st+"way")
else :
    rs = ""
    for i in range(len(st)):
        if st[i] not in "aeiouAEIOU":
            rs += st[i]
        else :
            break
    print(st[len(rs):]+rs+"ay")  """  

# (9) Rhyme Detector

# (10) Caesar Cipher

# (11) Balanced Parentheses
"""ab = input("enter syntax => ")
dt = {"(":")","{":"}","[":"]"}
if len(ab) % 2 == 0 :
    count = 0
    j = len(ab) - 1
    for i in range(len(ab)//2):
        if dt[ab[i]] == ab[j]:
            count += 1
        else :
            break    
        j -= 1
    print("true") if count == len(ab)//2 else  print("false") 
else :
    print("false")    """
#
# (13) Price Formatte        
"""price = eval(input("enter price => "))
print( "$" + f"{price:.2f}")"""
# (14) Password Strength Checker
passw = input("enter your password => ")
l,u,n,s = 0,0,0,0
for i in range(len(passw)):
    if passw[i].islower() : l = 1
    elif passw[i].isupper() : u = 1
    elif passw[i].isnumeric() : n = 1
    elif passw[i] in "!@#$%^&*()_<>?/" : s = 1
if l == 1 and u == 1 and n == 1 and s == 1 and 8 < len(passw) < 10 :
    print("strong password")
else :
    print("weak password")

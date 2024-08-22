#_______________________CODING-QUESTIONS-4-CBT_______________________________#

# (1) 1. Profit or Loss 1
"""cp = int(input("enter cp => "))
sp = int(input("enter sp => "))
if cp < sp :
    print("profit")
    a = (( sp - cp ) / cp ) * 100
    print(f"{a:.2f}")
else :
    print("loss")
    a = (( cp - sp ) / cp ) * 100
    print(f"{a:.2f}")""" 
# (2) Wish me
"""time = list(map(int,input().split() ))
if 4 <= time[0] <= 11 and 0 <=time[1] <= 59  : print("GOOD MORNING")
elif 12 <= time[0] <= 15 and 0 <=time[1] <= 59  : print("GOOD AFTERNOON")
elif 16 <= time[0] <= 20 and 0 <=time[1] <= 59  : print("GOOD EVENING")
else : print("GOOD NIGHT")"""
# (3) Trip or Not 
# N,S,C,H,L,T 
"""a = list(map(int,input().split()))
time =a[1]*a[2]*a[3] # (s*c*h)
left = (a[0] - a[5])*a[4] #(N - T)*L
if left > time :
    print("chalenge")
else:
    print("padenge")  """  
# (4) Funny or Not 
# N B G I D
"""a = list(map(int,input().split()))
anger = 0
anger = a[1]*a[3] - a[2]*a[4] # ( I - D )
if anger > 0:
    print("simple question")
else :
    print("funny question") """   
# (5)Find the Operator
"""a = int(input("a = ")) 
b = int(input("b = ")) 
c = int(input("c = "))
if a + b == c : print("+")
elif a - b == c : print("-") 
elif a * b == c : print("*") 
elif a / b == c : print("/") 
elif a // b == c : print("//")
elif a % b == c : print("%")
else : print("invalid data")"""
# (6)
"""a = int(input("u have => "))
b = int(input("first price => "))
c = int(input("second price => "))
d = int(input("third price => "))
print(a/b,a/c,a/d)"""
# () Days in Month 
"""a = int(input("enter month => "))
if 1 <= a <= 12 :
    if a == 2 :
        print(28)
    elif str(a )in "135781012":
        print(31)
    else :
        print(30)  
else :
    print("invalid month")  """      
# () Valid Triangles
""""t = int(input("total test case => "))
lst = []
for i in range(t):
    a = int(input("first angle => "))      
    b = int(input("second angle => "))      
    c = int(input("third angle => "))  
    lst.append(a)
    lst.append(b)
    lst.append(c)
   
for i in range(t):  
    if lst[i] + lst[i+1] + lst[i+2] == 180 :
        print("valid")
    else :
        print("invalid")  """
 
# () Leap Years 
"""a = int(input("enter a number => "))
for i in range(1,a+1):
    if (i % 4 == 0 or i % 100 == 0 ) and i % 400 != 0 :
        print(i,end=" ")     """ 

# () Perfect Number
"""a = int(input("enter a number => "))
b  = a
lst = []
for i in range(1,a+1):
    if b > 0 :
        if b % i == 0 :
            lst.append(i)
            b /= i
print(lst)

if sum(lst) == a :
    print(1)
else :
    print(0) """ 
# () Farmar Ramu 
"""def prime(n):
    count = 0
    for i in range(2,n):
        if n% i == 0 :
            count = 1
    if count == 0 :
        return n        
a = int(input("test case => "))
lst = []
for i in range(a):
    l = []
    l.append(int(input()))
    l.append(int(input()))
    lst.append(l)  
for i in range(a):
    c = lst[i][0] + lst[i][1] + 1
    while True :
        if prime(c) == c :
            print(c -(lst[i][0] + lst[i][1]) )
            break
        else :
            c += 1"""

"""num = input("enter number -> ")
if num[0] == "0" or num[len(num)-1] == "0" or "0" not in num[1:len(num)]:
    print("NDN")    
else :
    for i in range(len(num)):
        if num[i] == "0":
            print("DN")
            break"""
   
"""a  = input("enter = > ") 
if a == "Value Error":
    raise Exception(f"{a}") """ 

a = [1,4,-3,2,-6,4]
for i in range(len(a)):
    if a[i] < 0 :
        a[i] = ""
c = a.count("")
for i in range(c):
    a.remove("")
print(a)        
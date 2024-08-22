# 0 1 1 2 3 5 8 13 fibnoccii series

c = int(input("Enter total terms :"))
a = 0
b = 1
print(a,b,sep=" ",end=" ")
for i in range(c):
    temp = a + b
    a = b
    b = temp
    print(b,end=" ")

print("\n")    
# prime number

c = int(input("Enter number :"))
count = 0
for i in range(2,c):
    if c%i==0:
        count = count + 1
if count == 0:
    print(c,"is a prime number")
else:
    print(c,"is not a prime number")


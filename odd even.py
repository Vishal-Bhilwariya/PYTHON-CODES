# odd even

#method 1
print("\nEVEN NUMBERS TILL 100 ARE : ")
for i in range(100):
    if i%2 == 0:
        print(i,end=" ")
print("\n\nODD NUMBERS TILL 100 ARE : ")
for i in range(100):        
    if i%2 != 0:
        print(i,end=" ")  

print("\n")
#method 2
print("\n\nEVEN NUMBERS TILL 100 ARE : ")
for i in range(2,100,2):
        print(i,end=" ")
print("\n\nODD NUMBERS TILL 100 ARE : ")
for i in range(1,100,2):        
        print(i,end=" ")  

#method 3
a= int(input("enter starting number = "))
b= int(input("enter ending number = "))

for i in range(a,b,2):
    print(i,end=" ")
print("\n")
for i in range(a-1,b,2):
        print(i,end=" ")    

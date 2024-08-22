n=int(input())
A=[]
for i in range(0,n):
    list=int(input())
    A.append(list)

b =-1
for i in range(0,n):  # for max
    if b<A[i]:
        b = A[i] 
    
print("WINNER :",b)
c = -1
for j in range(0,n):   # for second max
   if c<A[j] and A[j] != b:
    c = A[j] 
print("RUNNER UP :",c)

# prime number

print("ALL PRIME NUMBERS TILL 100 ARE :")
i=2
for i in range(100):
   j=2
   for j in range(100):
    if i%j == 0 and i!=0:
        print(i)
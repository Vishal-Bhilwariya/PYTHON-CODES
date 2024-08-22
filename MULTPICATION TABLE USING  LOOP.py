# MULTPICATION TABLE USING FOR LOOP

a = int(input("Table of : "))
for i in range(1,11):
    print( a,"*",i ,"=",i*a )

# MULTPICATION TABLE USING WHILE LOOP

a = int(input("Table of :"))
i=1
while i<=10:
    print(a,"*",i,"=",a*i)
    i +=1


# REVERSE MULTPICATION TABLE USING WHILE LOOP

a = int(input("Table of :"))
i=10
while i>0:
    print(a,"*",i,"=",a*i)
    i -=1        
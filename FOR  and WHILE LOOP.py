#FOR LOOP

a = "vishal"
for i in a:
    print(i,"\n")
for i in a:
    print(i, end = "_")
print("\n")    
for i in range(len(a)):
    print(i)    

b = ["BLUE","RED","YELLOW","GREEN","PINK"]
for color in b:
    print(color)
for color in range(len(b)):
    print(color)    

# -> print namste 100 times 

for i in range(100):
    print("NAMSTE",end=",")    

for i in range(6,34)    :
    print("V","I","S","H","A","L",sep="_",end = "_@90\n")
  

print("Can give three argumnets in range")
for i in range(1,30,2):  # -> range ( a , b , c) :- a) a is starting value
    print(i,end=" ")     #                          b) b - 1 is ending value
                         #                          c) c is gap between any two values

print("\n")
         

# while loop

i = 0
while i<=3:  # or while (i<=3)
    print(i)
    i+=1

    


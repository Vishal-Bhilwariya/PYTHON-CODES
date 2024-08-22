import time
t1 = int(time.strftime('%H'))
t2 = int(time.strftime('%M')) 
t3 = int(time.strftime('%S'))

print("TIME = ",t1,":",t2,":",t3)
print(t1,"Hours ",t2,"Minutes",t3,"Seconds")

if t1 <= 12 and t2 <60 and t3<60:
    if (t1>=5 and t2<60 and t3<60) or (t1<12 and t2<60 and t3<60):
        print("GOOD MORNING")
else :
    if (t1>=12 and t2<60 and t3<60) or (t1<24 and t2<60 and t3<60):
        if t1>=12 and t1<17 :
            print("GOOD AFTERNOON")
        elif t1>=17 and t1<=22:
            print("GOOD EVENING")
        else :
            print("GOOD NIGHT")            
         

# same program but in shorter lines

import time
t1 = int(time.strftime('%H'))
t2 = int(time.strftime('%M')) 
t3 = int(time.strftime('%S'))

print("TIME = ",t1,":",t2,":",t3)
print(t1,"Hours ",t2,"Minutes",t3,"Seconds")

if t1 <= 12 and t2 <60 and t3<60:
    if (t1>=5 and t2<60 and t3<60) or (t1<12 and t2<60 and t3<60):  print("GOOD MORNING")
else :
    if (t1>=12 and t2<60 and t3<60) or (t1<24 and t2<60 and t3<60):
        if t1>=12 and t1<17 : print("GOOD AFTERNOON")
        elif t1>=17 and t1<=22: print("GOOD EVENING")
        else : print("GOOD NIGHT")            
         
''' in this program we can see that we can use single statement in just front of condition but if there are multiple statement 
inside condition then indentation is must '''
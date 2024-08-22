import time 
a = int(time.strftime("%H"))
b = int(time.strftime("%M"))
c = int(time.strftime("%S"))

print("Time = ",a,"h :",b,"m :",c,"s")

if a >= 5 and a<12:
    print("GOOD MORNING")
    print("It's ur time = ",a,"h :",b,"m :",c,"s")
    print("THANK YOU")
elif a >= 12 and a < 16:
    print("GOOD AFTERNOON")
    print("It's ur time = ",a,"h :",b,"m :",c,"s")
    print("THANK YOU")
elif a>=16 and a < 19:
    print("GOOD EVENING")
    print("It's ur time = ",a,"h :",b,"m :",c,"s")
    print("THANK YOU")
else :
    print("GOOD NIGHT")
    print("It's ur time = ",a,"h :",b,"m :",c,"s")
    print("THANK YOU")        

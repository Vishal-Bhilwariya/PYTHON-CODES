# FILE HANDLING

import csv
f = open("RECORDS.csv","w",newline="")
a = csv.writer(f)
a.writerow(["S NO.","NAME","GRADE"])
lst = []
s = 1
while True :
    nm = input("enter name => ").upper()
    gd = input("enter grade => ").upper()
    lst.append([s,nm,gd])
    ch = input("if u want to quit here enter 'n' otherwise enter any key => ")
    if ch.lower() == "n":
        break
    s += 1
a.writerows(lst)    

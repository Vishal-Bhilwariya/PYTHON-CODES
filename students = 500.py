cell_phone = 1
# roll_no = 1
count =0
for roll_no in range(500):
    a=1
    if roll_no % a == 0:
        b = roll_no
        for b in range(500):
         if cell_phone == 1 :
            cell_phone = 0
        else :
            cell_phone = 1   
    if cell_phone == 0:
        count += cell_phone 
roll_no += 1            
 
print(count)


# 500 students -> on 
# now 500 of
# 2 4 6 8 ....... 500 -> 250 on 
# 1 3 5 7 ......... 499 -> 250 of

# 3 6 9 12 ...... 498 -> 


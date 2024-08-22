lst1 = [12,3,4,64,2,5]
lst2 = [1,45,64,13,99,10]
lst3 = [100,32,23,99,345]

if lst1[0] < lst2[0] and lst1[0] < lst3[0]:
    if lst2[0] < lst3[0]:
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst1 + lst2 + lst3
        print(lst)
    else :
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst1 + lst3 + lst2 
        print(lst)
elif lst2[0] < lst1[0] and lst2[0] < lst3[0]:
    if lst1[0] < lst3[0]:
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst2 + lst1 + lst3
        print(lst)
    else :
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst2 + lst3  + lst1 
        print(lst)
else :
    if lst1[0] < lst2[0]:
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst3 + lst1 + lst2 
        print(lst)
    else :
        lst1.sort()
        lst2.sort()
        lst3.sort()
        lst = lst3 + lst2 + lst1  
        print(lst)
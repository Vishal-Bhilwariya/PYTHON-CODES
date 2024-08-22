''' DICTIONARY '''
# -> collection of pair of keys and values 

# a = {'name':"vishal",'age':18,'dob':"10-08-2005"}
# print(a)
# print(type(a))
# print(a["name"])
# print(a["dob"]) # -> this will give the respective values followed by keys . If not found then throws an error

# print(a.get("age")) #-> this will give the respective values followed by keys . If not found then print NONE 

"""
Questions on python dictionary:
Q1) You have a dictionary containing student names as keys and their respective grades as values. Write a function to calculate the average grade for all students.
"""

 

"""
Q2) Given a list of words, count the frequency of each word and store it in a dictionary.

Q3) Merge two dictionaries into one.

Q4) Given a dictionary, invert it such that keys become values and values become keys. Assume values are unique.
"""

# a = {'name':"vishal",'age':18,'dob':"10-08-2005"}
# b = {'name':"himanshu",'age':20,'dob':"10-06-2003"}
# c = {'name':"harsh",'age':19,'dob':"11-12-2004"}
# dt = {"st1" : a,"st2":b,"st3":c}
# print(dt)

n = eval(input("enter total students : "))
dt = {}
st = {}

for k in range(1,n+1):
    keys = eval(input(f"enter keys for student {k} : "))
    values = eval(input(f"enter values for student {k} : "))
    st[k] = {}
    for i,j in zip(keys,values):
        (st[k])[i] = j  
    dt.update(st[k])
print("Total data of students => ",dt,end="\n\n")


# for i in range(1,n):
#     for j in range(term):
#         if i != lst[j] or i != lst[] :  
#             print(i,")",sep="",end=" ")
#             print(dt[f"st{i}"]["name"],dt[f"st{i}"]["age"],dt[f"st{i}"]["city"],sep=" - ")
#         else :
#             check = 0    
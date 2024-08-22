#_______________________CODING-QUESTIONS-4-CBT_______________________________#

# list questions
# (1) 
"""a = input("enter word => ")
b = input("enter alphabet => ")
print(a.count(b))"""
# (2)
"""a = input("enter word => ")
for i in range(len(a)):
    if a[i].isnumeric():
        print("true")
        break
else :
    print("false")  """ 
# (3)
"""a = eval(input("enter list of integers => "))
max_ = -1
for i in range(len(a)):
    if max_ < a[i]:
        max_ = a[i]
se_max = -1
for i in range(len(a)) :
    if se_max < a[i] and a[i] < max_:
        se_max = a[i]
print(se_max)              """
# (4)
"""a = eval(input("enter ur list => "))
for i in range(1,a[len(a)-1]):
    if i not in a:
        print(i)"""
# (5)
"""a = input("enter ur list => ")
lst = []
for i in range(len(a)//2):
    lst.append(int(a[i]))
print(lst)       """  

# string questions

# (1)
a = input()
if a == 1:
    raise ValueError   
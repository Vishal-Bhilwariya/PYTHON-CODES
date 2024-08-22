# pattern printing

# 1)
# ****
# ****
# ****
# ****

a = int(input("enter number:"))
for i in range(a):
    for j in range(a):
        print("*",end="")
    print("\n")

# 2)
# *
# **
# ***
# ****


a = int(input("enter number:"))
for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    print("\n")

# 3)
# ****
# ***
# **
# *

a = int(input("enter number:"))
for i in range(1,a+1):
    for j in range(a+1,i,-1):
        print("*",end="")
    print("\n")

# 4)
# 1111
# 2222
# 3333
# 4444

a = int(input("enter number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        print(i,end="")
    print("\n")

# 5)
# 1
# 22
# 333
# 4444

a = int(input("enter number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end="")
    print("\n")

# 6)
# 1111
# 222
# 33
# 4

a = int(input("enter number:"))
for i in range(1,a+1):
    for j in range(a+1,i,-1):
        print(i,end="")
    print("\n")

# 7)
# 1
# 1 2 
# 1 2 3
# 1 2 3 4

a = int(input("enter number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")
    
# 8)
# 1
    

#type conversion

old_age = input("your age = "  )

# new_age = old_age + 2  
# this is syntax error as old_age is consider as string by compiler and 2 is as number . So, we cant add them 

# to overcome this problem we do "TYPE CONVERSION OR TYPECASTING"

new_age = int(old_age) + 2

print(new_age)

''' 
Type conversion can be of four types :
   1) int()
   2) float()
   3) str()
   4) bool()
'''

num = 34
print(float(num))
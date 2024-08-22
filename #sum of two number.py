#sum of two number
num = input("a = ")
num2 = input("b = ")

# sum = num + num2  # this will not add ( if num =1 & num2 = 4 then output according to this line is 14)
# print(sum)
# print("sum of a and b = " + sum) # this will also give error bcoz can only add string not intger to an string
#to overcome this problem we use type conversion

sum = int(num) + int(num2)
print(sum)
print("sum of a and b = " + str(sum))

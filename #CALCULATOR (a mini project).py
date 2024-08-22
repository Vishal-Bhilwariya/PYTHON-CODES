#CALCULATOR (a mini project)

sign = input("symbol (+,-,/,*,%) =" )
a = int(input("a = ") )
b = int(input("b = ") )

if sign == '+' :
    print("a+b = ",a+b)
elif sign == '-' :
    print("a-b = ",a-b)
elif sign == '/' :
    print("a/b = ",a/b)
    print("a//b = ",a//b)
elif sign == '*':
    print("a*b = ",a*b)
elif sign == '%' :
    print("a%b = ",a%b)    
else:
    print("WRONG CHOICE")                
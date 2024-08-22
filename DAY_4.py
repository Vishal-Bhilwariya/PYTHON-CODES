
#calculator using if elif
print("ENTER SYMBOL (+,-,*,/) = ")
sym = input()

if(sym=='+' or sym=='-' or sym=='*' or sym=='/' ):
    print("ENTER a = ")
    a = int(input())
    print("ENTER b = ")
    b = int(input())
    if(sym == '+'):
        print("a+b = ",a+b)
    elif(sym == '-'):
        print("a-b = ",a-b)    
    elif(sym == '*'):
        print("a*b = ",a*b)
    elif(sym == '/'):
        print("a/b = ",a/b)
else:
    print("PLZ SELECT CORRECT OPERATION U WANT TO DO")  

print("THANK YOU")


# ANOTHER CODE OF CALCULATOR in which each operation will takes place
a = 500
b = 10
print("SUM OF ",a,"&",b,a+b)
print("PRODUCT OF ",a,"&",b,a*b)
print("SUBTRACTION OF ",a,"&",b,"(a-b)",a-b)
print("DIVIDE  ",a,"&",b,"(a/b)",a/b)
print(a,"power",b,"is = ",a**b)

























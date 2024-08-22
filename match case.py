a  = int(input("enter your number : "))

match a:
    case 1 :
        print("ONE")
    case 2 :
        print("TWO")
    case 3 :
        print("THREE")
    case _ :
        print("THANK YOU")


''' EXAMPLE - > MAKE A PROGRAM TO MAKE A CALCULATOR USING MATCH CASE '''

a = int(input("Enter a = "))
b = int(input("Enter b = "))
s = input("Enter opertion u want to do = ")

match s:
    case '+':
        print(a+b,"is sum of ",a,"and",b)
    case '-':
        print(a-b,"is subtraction from ",a,"to ",b)
    case '*':
        print(a*b,"is multipication of ",a,"and",b)
    case '/':
        print(a/b,"is division by ",b,"to",a)
    case '//':
        print(a//b)
    case '%':
        print(a%b,"is remeindar when divide by",b,"to",a)
    case _ :
        print("WRONG CHOICE OF OPERATION")                        
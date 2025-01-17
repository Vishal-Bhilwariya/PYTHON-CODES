# PYTHON 
print("\n\n_______________________________PYTHON NOTES BY VISHAL R-R BHILWARIYA__________________________________")

# TOPICS THAT IS DONE : 1) ALL ABOUT NUMBERS IN PYTHON
#                       2) ALL ABOUT COMMENTS IN PYTHON
#                       3) SOME KEYWORDS IN PYTHON
#                       4) ALL ABOUT " BOOL " DATA TYPE
#                       5) ASSIGNING THE VALUE INTO VARIABLES
#                       6) OCTAL AND HEXADECIMAL REPRESENTATION IN PYTHON
#                       7) LOGICAL OPERATORS
#                       8) ALL ABOUT PRECEDENCE AND ASSOCITIVITY (Not complete by me)
#                       9) ALL ABOUT PRINT FUNCTION
#                      10) ALL ABOUT IF , ELIF AND ELSE
#                      11) ALL ABOUT THE STRING
#                      12) ALL ABOUT INPUT FUNCTION
#                      13) ALL ABOUT STRING SLICING AND STRIDING
#                      14) ALL ABOUT MUTABILITY AND IMUTABILITY (Not complete by me)
#                      15) ALL ABOUT STRING FUNCTIONS (NOT COMPLETE YET)
#                      16) ALL ABOUT LOOPS
#                      17) DIFFERENCE BETWEEN LISTS , SETS , TUPLES
#                      18) ALL ABOUT LISTS
#                   


print("\n................................................")
#Note -> " ; " is used after a statement to type multiple statement in a single line

a = 4
print(a) ; print(type(a)) ; print(a/2)
print("\n................................................")

# 1) ALL ABOUT NUMBERS IN PYTHON
print("ALL ABOUT NUMBERS IN PYTHON")

# TYPES OF NUMBER -> 1) int : anything that is not float and complex and string
#                    2) float : anything that contains decimal values and any number in python containing E or e
#                               ex - 23.4 , 23e2 , 23E2 etc 
#                                    23e2 -> means 23 * 10 ^ 2 = 2300.0
#                    3) complex : a + bj : a) here a is real & b is imaginary part
#                                          b) a and b are of float type bocz of iota
#                                          c) in python we use j as iota . it is predefined

print("\n................................................")

a = 5
b = 3.4
c = 23e2
d = 3 + 4j

print(type(a))  
print(type(b))
print(type(c))
print(type(d))
print(d.real)    # real part of complex number (d)
print(type(d.real))  
print(d.imag)    # imaginary part of complex number (d)
print(type(d.imag))  

print(".................................................\n")

# 2) ALL ABOUT COMMENTS IN PYTHON
print("ALL ABOUT COMMENTS IN PYTHON")

# -> Properties : a) It is non excutable part ( ignored by compiler or intpreter )  in code.
#                 b) Used to make understandable the code for future or for our team members whom with we working  
#                 c) basically a additional information about the program

# Types comment ->  a) SINGLE LINE COMMENT : is done by '#'
#                   b) MULTIPLE LINE COMMENT : is done by multiple #

# Note ->  Sometime we use triple quotes ( like this ''' body ''' ) for comment the line but it is not correct method of commenting
#          it works for us as comments bcoz it is not assigned to any variable ( space ) in right side . If assigned then it is a string.
# example 

''' HI i am Vishal 
    I love music
    i LOve GLA
'''

# the above three lines will work as a comments bcoz it lost in memeory as it is not assigned to any boxes and can not print it
# we will do one change in above three lines and lets see what happened

a = ''' HI i am Vishal 
    I love music
    i LOve GLA
    '''
print(a)   
# in above code we assigned the same lines in a variable named as "a" and the it print
print(".................................................\n")

# 3) SOME KEYWORDS IN PYTHON
print("SOME KEYWORDS IN PYTHON")
import keyword
print("Total keyword = ",len(keyword.kwlist))
print(keyword.kwlist)

# Note -> when u print the keyword u will see that only True , False & None are starting with upper case and rest all with lower

print(".................................................\n")

# 4) ALL ABOUT " BOOL " DATA TYPE
print("ALL ABOUT \" BOOL \" DATA TYPE")
# types : a) False is when 0
#         b) Except 0 all will gives true

a = 7
b = 0.0
c = 0.003
d = 0
print(bool(a))
print(bool(b))
print(bool(c))  
print(bool(d)) 
print(".................................................\n")

# 5) ASSIGNING THE VALUE INTO VARIABLES
print("ASSIGNING THE VALUE INTO VARIABLES")
a  = 4
b,c,d = 23,45.0,27 + 4j
e = 4 ; f = 4 ; g = 45.4
print(a,b,c,d,e,f,g)
print(".................................................\n")

# 6) OCTAL AND HEXADECIMAL REPRESENTATION IN PYTHON
print("OCTAL AND HEXADECIMAL REPRESENTATION IN PYTHON")
# -> Python usually(default) takes decimal value
# -> a) In Python octal number(0 t0 7) is repersent by " 0o " in stating
#    b) In Python hexadecimal number (0 t0 15 -> express as 0-9 and then A to F , A = 10 and so on F = 15) 
#       is represented by " 0x " in starting.

a = 0o56      # -> converting octal into decimal : 8^1 * 5 + 8^0 *6 = 46 (in decimal)
b = 0x78      # -> converting hexadecimal into decimal : 16^1 * 7 + 16^0 * 8 =  120 (in decimal)
print(a) ; print(b)
print(type(a)) ; print(type(b))
print(0x9F)   # -> 16^1 * 9 + 16^0 + 15(F) = 159
print(".................................................\n")

# 7) LOGICAL OPERATORS
print("LOGICAL OPERATORS")
# Three types : 
#    a) and -> means both condition should be give true to get true in output.If any one condition is false then output is false
#    b) or  -> if any one condition is true then output will be true 
#    c) not -> if condition is true then output will be false and vice versa

print(10>20 and 20>10) 
print(10>20 or 20>10)
print(not 10>20)

# some good quetions , guess the output before run
# a) and :
print("\n")
print(23 and 1087)  
print(-89 and -872)
print(-27 and 90.98)
print(23 and -72.8) 
print(0 and 20)

# -> in above codes :a) intrepeter will check the first value , is it true or false , if true then check second value and print
#                       value that value when there is no other condition is present further.
#                    b) if first value is false , then the intrepeter will stop and will print false condition value
#   NOTE -> Condition is true when non-zero value is present and false when value is zero(0) 
                      

# b) or :
print("\n")
print( 2 or 6)
print( 0 or 6)
print( 0 or-67)
print (-65 or -34)
print(34 or 0)

# -> in above codes :a) intrepeter will check the first value , is it true or false , if false then check second value and print
#                       value that value when there is no other condition is present further.
#                    b) if first value is true , then the intrepeter will stop and will print true condition value
#   NOTE -> Condition is true when non-zero value is present and false when value is zero(0) 

# -> MULTIPLE and & or
print(23 and 0 or 342) # (23 and 0 ) -> 0 : now (0 or 342 ) -> 342
print(2 and 0 or 50)  # (2 and 0 ) -> 0 : now (0 or 50 ) -> 50
print(2 and 455 or 0)   # (2 and 455 ) -> 455 : now (455 or 0 ) -> 435 
print(2 and 455 or 45)  # (2 and 455 ) -> 455 : now (455 or 45 ) -> 435 

# c) not :
print(not(0)) # -> 0 is false then output is true bcoz of not

# -> MULTIPLE and & or & not
print(not(34) and 76 ) #-> 76 will be output
print(not(0 or 34) and not(34 and 0))
#      false and true -> false in output
print(not(0 or 34) or not(34 and 0))
#      false or true ->true in output


print(".................................................\n")

# 8) ALL ABOUT PRECEDENCE AND ASSOCITIVITY
print("ALL ABOUT PRECEDENCE AND ASSOCITIVITY")


print(".................................................\n")

# 9) ALL ABOUT PRINT FUNCTION
print("ALL ABOUT PRINT FUNCTION")
# print() -> is used to display anything on output screen

# Print function can take two types of arguments :
#         a) POSITIONAL arguments : Based on position (first come first serve)
#         b) Keywords argumnet : Based on two types :
#                   1) sep -> used to add any character or number in between two or more strings
#                   2) end -> used to add any character or number at the end of string
# note -> 1) By default the sep takes blank space ( like this : sep = " ")
#         2) By default the end takes new line ( like this : end = "\n")
# Note -> Positional arguments should be provide before the keywords arguments otherwise it will through an error

print("HI","VISHAL","SIR") # -> In this : "HI" is on first postion
                           #              "VISHAL" is on second position
                           #              "SIR" is on third position
                           # they will show there output according to their positions . These all are called "POSITIONAL ARGUMNETS"


print("HI","VISHAL","SIR") # -> 1) in this when it will print on screen we can see blank space between different strings by default
                           # -> 2) in this when it will print on screen we can see a new line  by default ( * doubt * )
print("HI","VISHAL","SIR",sep="@") # -> 1) in this when it will print on screen we can see '@' between different strings as sep is defined by coder

print("HI","VISHAL","SIR",end = "90") # -> 1) in this when it will print on screen we can see 90 at the end of string as end is defined by coder

# *
# note -> when we use end function in print function (like this : end = "34") then the new line automaticallly terminated .so for next line should use "\n"
# so here for new line :
print("\n") 
print("HI","VISHAL","SIR",end = "90",sep = "_")
                          
# some notables points : 1) do not use keywords argumnet before or between positional argumnets .they will through error
#                        2) can use end before sep or vice-versa

# to see what is wrong in below two lines , uncomment and then see
#  print("HI","VISHAL",end = "90","SIR",sep = "_")
#  print("HI","VISHAL",sep = "_","SIR",end = "90")

print("\n................................................")

# 10) ALL ABOUT IF , ELIF AND ELSE

#Note -> SOME RULES : 
#    a) else is not mandatory for if but if is mandatory for else (else present without previous if throws an syntax error)
# Types :- 1) if
#          2) Nested if
#          3) if else
#          4) if elif else


if 10>23 :
    print("NAMSTE")
elif 23<1 :
    print("HELLO WORLD")    
else :
    print("BYE")   

# Write a python script to check the number is 3 digit or not .
#  sample test : input -> a) 324 -< true
#                         b) -231 -< true
#                         c) 000 -< true
#                         d) 008 -< true

num = input("Enter Your Number = ")

length = len(num)  # will count lenght of input string
negative = num.count("-") # if there is negative number present then 1 is stored in negative variable(using count function)
                          # if not present negative number then 0  stored in negative variable 

if negative == 1 :               # for negative number
    if length == 4:
        print(num,"is a three digit number")
    else :
        print(num,"is not a three digit number")

else :                       # for non - negative number
    if length == 3:
        print(num,"is a three digit number")
    else :
        print(num,"is not a three digit number")

print("\n................................................")

# 11) ALL ABOUT THE STRING

# -> Anything that is present in between single , double or triple quotes is called "STRING"
# -> In python there is no character data type , so anything between single quotes is consider as string
# -> In python , for multiple line we use triple quotes 

n1 = 'VISHAL BHILWARIYA'
n2=  "VISHAL BHILWARIYA"
n3 = """VISHAL
      BHILWARIYA"""
n4 = '''VISHAL
      BHILWARIYA'''
print(n1)
print(n2)
print(n3)
print(n4)

# note -> n1 and n2 , n3 and n4 will produce same output

# -> String is consider as array or lists :
#        1) whose index is started from 0 and end with n-1
#        2) negative index (-1) is started from last character of string and move backword
# :-> negative index is used bcoz 0 is reserved already

# SLICING OF STRING
# SYNTAX -> variable_name[start : end-1 : step]
#      -> Default value for : a) start is 0
#                             b) end is last index
#                             c) step is -> 1) +1 for start index 0
#                                           2) -1 for start index -1 

name = "VISHAL BHILWARIYA SIR"
print(name)

print(name[0:5])
print(name[4:14])
print(name[-1:-4:-1])
print(name[-15:-4])
print(name[2:14:2])

# some tricky questions

print("\n................................................")
# 12) ALL ABOUT INPUT FUNCTION

# -> 'input' function is used to take input from user .
# -> input function always return "str" data
# -> can give statement inside input function which will shown at user screen

a = input()
    # or
b = input("enter :")

print(a)
print(b)

# Write a python program to add :
# a) two string (concatation)
a = input("a = ")
b = input("b = ")
print(a+b)

#note-> # :-> As we know input function only return string data so we have to do typecasting to perform int or float value problems
# b) two int 

a = int(input("a = "))
b = int(input("b = "))
print(a+b)

# c) two float 
a = float(input("a = "))
b = float(input("b = "))
print(a+b)

# d) one int and one float
a = int(input("a = "))
b = float(input("b = "))
print(a+b)

# -> we can see while performing the addition of two different - different data type values , we have to do typecasting for there use,
#    like -> for int typecast to int , for float typecast to float.
# So there is a function called 'eval' which is auto-sense the data type entered by user 

a = eval(input("enter any type  = "))
b = eval(input("enter any type = "))
print(a+b)

# note -> while taking any string from user , make sure that is enetered within quotes otherwise it throws an { name error-> not define}


print("\n................................................")

# 13) ALL ABOUT STRING SLICING AND STRIDING

# SYNTAX -> name[start : end : step] 
#          Default values of : a) start = 0
#                              b) end = len - 1
#                              c) step = +1 or -1  < - > +1 for forward direction and -1 for backward direction
# meaning of step is that suppose there is a string "HELLO SIR" if step is 2 and start and end is default then , output will be "HLOSR"               

name = "VISHAL BHILWARIYA SIR JI"
print(name[::]) # -> will work according to default value and will print same string
print(name[2:5:]) # -> starting index is 2 and ending index is (5 - 1 = 4) and step is default(1)
print(name[2:10:2]) # -> starting index is 2 and ending index is (10 - 1 = 9) and step is 2 
# print(name[12:20:-1]) # thows an error bcoz stating from 12 and going towards right but negative step wants to go left so it will throw an error
print(name[-2:-20:-1]) # will start from right and then move towards left and step is -1 
  # NOTE -> When moving from right to left we have to provide step as -1
print(name[1:18963487])   # end index provided by user is not define so program will works until the string ends
print(name[2345553:]) # does not print anything as starting index does not index and will print a blank space
# print(name[3.4:2.6:2.3]) 
# print(name["v":"j"])

# note -> line 10 and 11 will throws an error bcoz slicing works only with integer , none or index only
print(name[2:34:24325]) # will print start index only bcoz after that no index is awailable as provided by user in step
print(name[2:2:1])
print(name[-2:-2:-1])

# note -> line 15 and 16 will print blank space bcoz starting and ending is same

print(name[-2334:-43:-2]) # will print blank space as stating index does not exist
print(name[-1:-118963487:-1])   # end index provided by user is not define so program will works until the string ends

print(name[::2]) # default -> starting and ending index from left to right
print(name[::-2]) # default -> starting and ending index from right to left

print("\n................................................")
# 14) ALL ABOUT MUTABILITY AND IMUTABILITY


print("\n................................................")
# 15) ALL ABOUT STRING FUNCTIONS

# 1) append()

# 2) split() -> use to break  string into a list
  #  syntax -> name.split(sep = "", max_split = int) where default values are : a) sep -> blankspace , b) max_split is -1
  # always returns " lists "
name = "VISHAL BHILWARIYA IS A GOOD PERSON"
print(name.split())
print(name.split(" ",))
print(name.split(" ",-1)) 
# note -> line 7,8,9 will give same output 
# print(name.split( ,-1)) -> throws an error bcoz ep is not provided and max split is given.
print(name.split(" ")) # -> will not throws an error bcoz sep is given  
 # note -> if max split is given then u must provide sep but reverse is not mandatory

print(name.split(" ",2)) # -> will break first two words in two elements and all remaining in one element
print(name.split(" ",4)) # -> will break first 4 words in 4 elements and all remaining in one element

print(name.split("A")) # -> for first element it will check till A comes , when it comes then it break and search for second element formation
print(name.split(" ",0))

print(name.split(" ",23533540)) #-> will make elements of list from string until the last index of string
print(name.split(" ",-2353420)) # same as above line


# 3) islower() -> checks that all character in string is in lower case or not . It retuns in bool form
name = "VISHAL BHILWARIYA IS A GOOD PERSON"
print(name.islower()) # -> will print false

# 4) isupper() ->  checks that all character in string is in upper case or not . It retuns in bool form
name = "VISHAL BHILWARIYA IS A GOOD PERSON"
print(name.isupper()) # -> will print true

# 5) isidentifier -> used to check the identifier
name = "break"
name2 = "2break"
print(name.isidentifier()) # -> returns true bcoz valid identifier
print(name2.isidentifier()) # -> returns false bcoz un-valid identifier as stating with number

# 6) capitalize() -> used to convert first letter of string into uppercase if present in lower case and rest of string in lower case
name = "vISHAL BHILWARIYA IS A GOOD PERSON"
print(name.capitalize()) 

# 7) isalnum() -> used to check A-Z , a-z, 0-9 . if present these only then will return true
name = "Vsf444SFA@@"
print(name.isalnum()) # -> will print false bcoz of @@

# 8) isalpha() -> used to check A-Z , a-z only . if present these only then will return true
name = "VsfdsvfbgSDD"
print(name.isalpha()) # -> will print true

# 9) count -> used to count the entered character inside this function in any string
name = "vISHAL BHILWARIYA IS A GOOD PERSON"
print(name.count("A"))

# 10) casefold -> used to convert upper case into lower case
name = "vISHAL BHILWARIYA IS A GOOD PERSON"
print(name.casefold())

# 11) swapcase() -> used to convert upper case into lower case or vice-versa
name = "vISHAL BHILWAriya IS A GOOD PERSON"
print(name.swapcase())

# 12) endswith() -> used to check the last charcter 
name = "vISHAL BHILWARIYA IS A GOOD PERSON"
print(name.endswith("N"))

# 13) join() -> converts the element of an iterable into string
name = "_"
print(name.join("vishal")) 

# 14) isascii() -> used to check that any character has there own ascii value or not
name = "s"
name2 = "$%2"
print(name.isascii())
print(name2.isascii())

# 15) strip() -> used to remove the leading and trailing whitespaces from any string bcoz whitespaces does not show anything and which consumed memory for no logic
name = "    VISHAL BHILWARIYA IS A GOOD PERSON     "
print(name.strip()) # -> will print string without trailing and leading whitespaces

# 16) lstrip() -> used to remove leading whitespace
name = "       VISHAL SIR     "
print(name.lstrip())

# 17) rstrip() -> used to remove trailing whitespace
name = "       VISHAL SIR     "
print(name.rstrip())

# 18) center() -> a)returns centered string
name = "VISHAL SIR"
print(name.center(20)) # need to give one argument

# 19) find() -> a) returns the value position(index) which is user wants
#               b) if not found then returns -1
name = "VISHAL SIR"
print(name.find("S"))
print(name.find("s"))

# 20) rfind() -> start finding required value from right side and returns the index if found and if not found then returns -1
name = "vishal@ bhilwariya"
print(name.rfind("@"))
print(name.rfind("_"))

# 21) isdigit() -> returns true when all charcters are digits

# 22) isdecimal -> will return true if only consist 0-9
num = "1239092"
num2 = "1239092e"
print(num.isdecimal()) # -> true
print(num2.isdecimal()) # -> false bcoz ' e' comes in hexadecimal

# 23) isnumeric() -> returns true when all charcters are digits

#Note -> isdecimal is subset of isdigit and isdigit is subset of isnumeric

# 24) lower() -> converts upper case into lower case
# 25) upper() -> converts lower case into upper 
name = "VISHAL R-R bhilwariya"
print(name.lower())
print(name.upper())

# 26) -> replace() -> retunrs the the string where specified value is replaced with any particular value
#                  -> it takes at least two string argumnet : first to be replaced by second
name = "vishal r-r bhilwariya  "
print(name.replace("vishal","himanshu"))

# 27) startswith() -> used to check that specified value is started with required value or not
name = "@_vishal sir"
print(name.startswith("@"))
print(name.startswith("_"))

# 28) index() -> returns the  position(index) of searched argumnet
name = "VISHAL SIR"
print(name.index("S"))
# print(name.index("s")) -> throw an error bcoz small s is not found

# 29) rindex() ->

# 30) split() -> used to break the string in the form of list
name = "my name is vishal bhilwariya"
print(name.split())


# 31) rsplit() ->
# 32) zfill() ->
# 33) format() ->




print("\n................................................")

# 16) ALL ABOUT LOOPS

# function that can useful to use : in , range() , break() , continue() , pass()

for i in range(1,10):
    print(i)
# <> code for even or odd
for i in range(2,100,2):
    print(i,end=" ")
print("\n")
for i in range(1,100,2):
    print(i,end=" ")
# <> code to print table
num = eval(input("Enter number : "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

print("\n")        
# -> use of break  : use to terminate the loop when the required condition matched

for i in range(1,10):
   if i % 5 == 0:
    break
   else :
    print(i)

print("\n")        

# -> use of continue : use to skip that condition which is satisfied
for i in range(1,10):
   if i % 5 == 0:
    continue
   else :
    print(i)

# use of pass : if we want to excuete loop without providing any statement inside it then we use pass function to excuete that loop
for i in range(1,10):
    pass
print(i)

print("\n................................................")

# 17) DIFFERENCE BETWEEN LISTS , SETS , TUPLES
# a) Lists -> a) It is mutable
#             b) It is ordered collection of items or elements
#             c) Items can be changed or replaced
# b) Set ->   a) It is mutable 
#             b) It is un-ordered collection of items or elements
#             c) Items can not be changed or replaced but you can add or delete new items
# c) Tuples ->a) It is immutable
#             b) It is ordered collection of items or elements
#             c) Items can not be changed or replaced

# 18) ALL ABOUT LISTS

num = int(input())
lst = []
for i in range(num):
    b = 0 
    b = int(input())
    lst.append(b)
 
rev = lst[::-1]
print(rev)  

  
lst = [34,445,3,321,2,]
print(lst[::-1])
print(lst[-2])
print(lst[3])
print(lst[1:3])

lst.clear()
print(lst)

lst.append(5)
print(lst)


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = "")
    print("")
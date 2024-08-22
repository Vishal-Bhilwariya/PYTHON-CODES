name = "VISHAL" # OR 'VISHAL'
print(name)

chat = """
       MY NAME IS VISHAL
       I'M FROM AGRA
       I LOVE MUSIC
       """
print(chat)

print("HELL0 " +name)
print("HELLO",name)

print("He said,\"I am hungry\"")

print("""
       MY NAME IS VISHAL
       I'M FROM AGRA
       I LOVE MUSIC
       """
    )

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6]) #throws an error

#for loop in string
print("for loop\n")
for character in name:
    print(character)

a = len(name)
print(a)    

print(len(name))

# < STRING SLICING AND OPERATION > #
print("\"< STRING SLICING AND OPERATION >\"")
names = "VISHAL_BHILWARIYA"
print(names[0:5]) #in between means 0 includes and 5 not (means 5 - 1)

print(names[:5]) 
"""" for understanding some points 
     -> a) python automatically takes 0 as starting index if not mentioned
        b) index 0 is included but index 5 is not 
        c) code will run from 0 to 4 only
"""  

print(names[:]) # -> this is also correct,Python will take 0 index as start and will consider till end of string automatically

print(names[-7:-2]) 
'''
    -> a) this is correct syntax
       b) python will read like this : A) starting index = len(names) - 7 -> 17 - 7 = 10
                                       B) ending index = len(names) - 2 -> 17 - 2 = 15
'''   

print(names[-5:-1])

print(names[-4:0]) # no output for this bcoz ending index can't be 0 here as it is starting index is more than 0

names = "VISHAL_BHILWARIYA"
print(names[0:10:3]) 
print(names[4:15:2])

# # << STRINGS METHODS >> #

name = "visHAl BhiLWAriya sIR JI!!"
print(len(name))
print(name.upper()) 
print(name.lower())
print(name.rstrip("!"))  # will remove '!' present at end
print(name.replace("VisHAl","HImaNShu")) #will replace the string
print(name.replace("l",'h')) #will repalace character also
print(name.split()) # split into lists
print(name.capitalize()) # first letter will convert into upper case and rest will int0 lower case
print(name.center(len(name)+25))   #will give the blank space in starting of 25
print(name.center(len(name)+25,"_")) #will fill the blank space with _
print(name.ljust(50,'_')) #will fill the left side blank spaces with _
print(name.rjust(50,'_')) #will fill the right side blank spaces with _
print(name.count("A"))  #will count the number of time the character present 
print(name.startswith("visHAl"))
print(name.endswith("!")) #will check that string is ending with ! this or not and returns in boolean form(true or false)
print(name.endswith("SIR",0,21)) #can check in betweeen value by giving stat and end index
print(name.find("A")) #will return the index of first occurance if true if false then return -1
print(name.rfind("A"))  #will return the index of last occurance if true if false then return -1
print(name.index("sIR")) #will return the index of "S" bcoz it is first occurance
#NOTe -> find() & index() are quit similar but when condition is false then find() returns -1 & index returns error
print(name.swapcase())
print(name.title())

names = "  visHAl bhilWAriYa  !! "
print(names.strip()) #removes blank space from start and ending of string

names = "WelcomeToTheConsole45"
print(names.isalnum()) #only consist of A-Z,a-z,0-9 then true otherwise false
print(names.isalpha()) #only consist of A-Z,a-z then true otherwise false
print(names.istitle())

nam = "VISHAL SIR JI\n"
print(nam.islower()) #checking that string is in lower case or not if yes then returns true 
print(nam.isupper()) #checking that string is in upper case or not if yes then returns true

nam = "VISHAL SIR JI"
print(nam.isprintable()) #will return true
nam = "VISHAL SIR JI\n"
print(nam.isprintable()) #will return false bcoz '\n' can not print bocz it used to give new line

n = "                  "
print(n.isspace())  

s1 = "VISHALBHILWARIYA"
s2 = "_"
print(s2.join(s1))
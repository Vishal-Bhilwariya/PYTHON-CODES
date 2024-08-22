""" There are two python list representing marks of two subjects for 5 students. You have to identify
    those students who has more than 60 marks in both subjects """
# py = []
# ma = []
# print("enter python marks ")
# for i in range(5):
#     py.append(int(input()))
# print("enter maths marks ")
# for i in range(5):
#     ma.append(int(input()))

# for i in range(5):
#     if py[i] > 60 :
#         if ma[i] > 60 :
#             print("st :",i+1,"python :",py[i],"maths :",ma[i])

""" You have a list of tuples having students name followed by marks of python , maths ,english,physics
    Find those students who get more than 75% """

# a = int(input("enter total students : "))
# b = int(input("enter total subjects : "))
# data = []

# for i in range(a):
#     for j in range(b+1):



""" Write a python script to find initial prefix string within list elements .
note -> if no common prefix found display empty sting """

# # List of strings
# list_of_strings = ["apple", "appetizer", "application"]

# # Initialize prefix with the first element
# prefix = list_of_strings[0]

# # Iterate through the remaining elements
# for string in list_of_strings[1:]:
#     # Reduce prefix until it's a prefix of the current string
#     while not string.startswith(prefix):
#         prefix = prefix[:-1]
#         if not prefix:
#             break    

# # Print the initial prefix
# print("Initial prefix within list elements:", prefix)


a = "vishal bhilwariya"
print(a["v":"i"])

#lists

marks = [23,45,6,78,'maths']  #marks are lists here containing number as well as character

print(marks)  #it will print whole list
print(marks[0])   #it will only print value at index o (marks[0] = 23)
print(marks[-1])  #it will print value start from last index {last index will consider as -1 and then decreasing to left }

#if we want between index value then
print(marks[1:4]) #it will include index from 1 to 3 (4 is not included)

#FOR loops in LISTS

for score in marks:
    print(score)   #score starts from 0 , end with last index of marks and print their respective value

#to add any data to lists at end 
marks.append('air')    
print(marks)

#to add any data in between any index
marks.insert(3,'vishal')
print(marks)

#to check any data which is present in lists or not
print(6 in marks)   #here "in" function is working for check

#to find lenght of lists
print(len(marks))

#WHILE loops in LISTS
i=0
while i<len(marks):
    print(marks[i])
    i=i+1

#to clear (delete) the lists
marks.clear()
print(marks)    


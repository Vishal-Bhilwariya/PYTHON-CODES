# WAP TO TAKE TOTAL NUMBER OF MEMBERS AND THIER RESPECTIVE AGE FROM USER AND CHECK WHAETHER THEY ARE ELIGIBLE TO VOTE OR NOT

a = int(input("Enter total memebers in your family :"))
count = 0
i=1
while i<=a:
    print(i,")")
    b = input("     NAME :- ")
    c = int(input("     AGE :-"))
    # print("NAME :- ",b,"->","AGE :-",c)
    if c>=18:
        print("    ",b,"(",c,"year old",")","is eligible to vote")
        count+=1
    else :
        print("    ",b,"(",c,"year old",")","is not eligible to vote")    
    i +=1

if a == count:  
    print("\nNOTE -> 1)ALL MEMBERS OF THIS FAMILY ARE ELIGIBLE TO VOTE")
else :
    print("\nNOTE -> 1)",count,"PERSONS ARE ELIGIBLE TO VOTE") 

cost_per_head = 100
print("        2)Total amount to be pay by user is :",count*cost_per_head,"for",count,"persons")

print("\nTHANK YOU FOR INFORMATION")    
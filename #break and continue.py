#break and continue 

#use of break { to stop printing after that match }
name = ['VISHAL','HIMANSHU','ROHIT','SANDEEP','HARSH','SIR']
for name in name:
    if name == "HARSH" :
        break          #it will break the loop when if condition satsified
    print(name)

#use of continue { to skip that match part and continue }
name = ['VISHAL','HIMANSHU','ROHIT','SANDEEP','HARSH','SIR']
for name in name:
    if name == "HARSH":
        continue
    print(name)    
s2 = 0 
d = [{"per":70,"cat":"one"},{"per":50,"cat":"two"},{"per":25,"cat":"three"}]   
for i in reversed(range(11)):
    s=" "
    s2+=1
    if i != 10:
        ln = len(str((i+s2)*10))
        print(f"{s*(ln-len(str(i*10)))}{i*10}|",end=" ")
    else:
        print(f"{i*10}|",end=" ")
    s3=0
    for j in d:
        s3+=1
        if (j["per"] <i*10):
            if s3 == len(d):
                print("")
            else:    
                print("",end="")
        else:
            if s3 == len(d):
                print("o  ")
            else:    
                print("o  ",end=" ")
print("    -"+"-"*len(d)*3)  
print('    ',end="")    
##########
sp4 = 0  
li=[]
ln = 0
for i in d:
    if ln<len(i["cat"]):
        ln=len(i["cat"])   
while sp4<ln:
    for l in d:
        if sp4<len(l["cat"]):
            li.append(l["cat"][sp4])
        else:
            continue
    sp4+=1
li3=[]    
for i in d:
    li3.append(len(i["cat"]))
li2=[]    
sp5=1 
sp6=0
print(" ",end="")
for i in li:
    li2.append(sp5)
    if sp5%(len(d))==0:
        print(i,end="   ")
        print("\n    ",end=" ")
        sp5=1
    else:
        print(i,end="   ")
        sp5+=1 
    for i in li3:
        if i == li2.count(sp5):
            print("  ",end="")
            sp5+=1
            
            
            
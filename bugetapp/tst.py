"""
working perfectly

hello = {"name":"Sanchit Gupta", "age": 21, "city": "Delhi","Description": "I am a student of B.Tech CSE 3rd year at IIT Roorkee. "}
print("*"*50)
ch = 0
sp = 0
for i in hello:
    if type(hello[i])!=int:
        if len(i)+len(hello[i])+3>50:
            exp=None
            for j in hello[i]:
                ch+=1
                if j ==" ":
                    sp+=1
                    if len(hello[i][:ch])<(50-len(i)-3):
                        continue
                    else:
                    exp = True
                        print(f"{i} : {hello[i][:ch]}")
                        print(" "*len(i)," ",hello[i][ch:])
                        break
            if exp!=True:
                print(f"{i} : {hello[i][:ch]}")                                
        else:
            print(f"{i} : {hello[i]}")
    else:
        print(f"{i} : {hello[i]}")
"""

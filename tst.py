hello = {"name":"Sanchit Gupta", "age": 21, "city": "Delhi","Description": "I am a student of B.Tech CSE 3rd year at IIT Roorkee. "}
print("*"*50)
ch = 0
sp = 0
for i in hello:
    if type(hello[i])!=int:
        if len(i)+len(hello[i])+3>50:
            for j in hello[i]:
                ch+=1
                if j ==" ":
                    sp+=1
                    if len(hello[i][:ch])<(50-len(i)-3):
                        continue
                    else:
                        print(f"{i} : {hello[i][:ch]}")
                        print(" "*len(i)," ",hello[i][ch:])
                        break
                                                  
        else:
            print(f"{i} : {hello[i]}")
    else:
        print(f"{i} : {hello[i]}")


#print(hello["Description"][:45])

"""
for i in hello:
    if type(hello[i])!=int:
        if len(i)+len(hello[i])+1>48:
            print(f"{i} : {hello[i][:48-len(i)-1]}...")

    else:
        print(f"{i} : {hello[i]}")
print("About me".center(40, "*"),"\n","\n".join([f"{i}: {hello[i]}" for i,j in hello.items() if (len(i)+len(hello[i])+1)>48:]))
"""
hello = {"name":"Sanchit Gupta", "age": 21, "city": "Delhi","Description": "I am a student of B.Tech CSE 3rd year at IIT Roorkee. "}

for i in hello:
    if type(hello[i])!=int:
        for j in hello[i]

print(hello["Description"][:45])

"""
for i in hello:
    if type(hello[i])!=int:
        if len(i)+len(hello[i])+1>48:
            print(f"{i} : {hello[i][:48-len(i)-1]}...")

    else:
        print(f"{i} : {hello[i]}")
print("About me".center(40, "*"),"\n","\n".join([f"{i}: {hello[i]}" for i,j in hello.items() if (len(i)+len(hello[i])+1)>48:]))
"""
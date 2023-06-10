a= ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

oper=['+','-']
u_d = []
expr=[[],[],[]]
sol=[]
for i in a:
    u_d.append(i.split())

for j in u_d:
    l1=len(j[0])
    l2=len(j[2])
    if l1>l2:
        j.append([1,l1-l2,l1])
    elif l1<l2:
        j.append([-1,l2-l1,l2])    
    else:
        j.append([0,l1-l2,l1])

for k in u_d:
    if k[3][0]==-1:
        expr[0].append(f'  {" "*k[3][1]}{k[0]}')
        expr[1].append(f'{k[1]} {k[2]}')
        expr[2].append('--'+'-'*k[3][2])
    elif k[3][0]==1:
        expr[0].append(f'  {k[0]}')
        expr[1].append(f'{k[1]} {" "*k[3][1]}{k[2]}')
        expr[2].append('--'+'-'*k[3][2])
    else:
        expr[0].append(f'  {k[0]}')
        expr[1].append(f'{k[1]} {k[2]}')
        expr[2].append('--'+'-'*k[3][2])
print(expr)        
for l in expr[0]:
    print(l,end='    ')
print('\n',end='')    
for m in expr[1]:
    print(m,end='    ')    
print('\n',end='')
for n in expr[2]:
    print(n,end='    ')    
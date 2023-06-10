def arithmetic_arranger(problems:list,soln:bool=False):
    operators=['+','-']
    u_d = []
    expr=[[],[],[]]
    sol=[]
    num=[0,1,2,3,4,5,6,7,8,9]
    l_prob=len(problems)
    solve=True
    while solve ==True:
        if l_prob>5:
            print("Error: Too many problems.")
            solve=False
            break
        else:
            for i in problems:
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

                
        for val in u_d:
            if val[1] not in operators:
                print("Error: Operator must be '+' or '-'.")
                solve = False
                break
            for i in val[0]:
                if int(i) not in num:
                    print("Error: Numbers must only contain digits.")
                    solve = False
                break
            for i in val[2]:
                if int(i) not in num:
                    print("Error: Numbers must only contain digits.") 
                    solve = False
                break
            if (len(val[0]) or len(val[2]) ) >4:
                print("Error: Numbers cannot be more than four digits.")
                solve = False
                break
        if solve==False:
            break
        #arrangement
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
        for l in expr[0]:
            print(l,end='    ')
        print('\n',end='')    
        for m in expr[1]:
            print(m,end='    ')    
        print('\n',end='')
        for n in expr[2]:
            print(n,end='    ') 
        solve=False
        if soln==True:
            for o in u_d:
                if o[1]=="+":
                    sol.append(f'  {int(o[0])+int(o[2])}')
                if o[1]=="-":
                    if o[3][0]==-1:
                        sol.append(f' {int(o[0])-int(o[2])}')
                    elif o[3][0]==1:
                        sol.append(f'  {int(o[0])-int(o[2])}')  
                    else:      
                        sol.append(f'  {int(o[0])-int(o[2])}')  
            print('\n',end='')            
            for p in sol:
                print(p,end='    ')       
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","3801 - 2"], True)
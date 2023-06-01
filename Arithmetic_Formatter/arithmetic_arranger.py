def arithmetic_arranger(problems:list,soln:bool=False):
    operators=['+','-']
    exp = {}
    expup=[]
    expdown=[]
    num=[0,1,2,3,4,5,6,7,8,9]
    l_prob=len(problems)
    solve=True
    while solve ==True:
        if l_prob>5:
            print("Error: Too many problems.")
            break
        for i in range(l_prob):
            exp[i]=problems[i].split()
            if len(exp[i][0]) > len(exp[i][2]):
                exp[i].append(len(exp[i][0]))
            elif len(exp[i][0]) < len(exp[i][2]):
                exp[i].append(-len(exp[i][2]))
            else:
                exp[i].append(0)

                
        for val in exp.values():
            if val[1] not in operators:
                print("Error: Operator must be '+' or '-'.")
                solve = False
                break
            for i in val[0]:
                if int(i) not in num:
                    print("Error: Numbers must only contain digits.")
                    solve = False
                    break
                break
            for i in val[2]:
                if int(i) not in num:
                    print("Error: Numbers must only contain digits.") 
                    solve = False
                    break
                break
            if (len(val[0]) or len(val[2]) ) >4:
                print("Error: Numbers cannot be more than four digits.")
                solve = False
                break
        #arrangement
        for val in exp.items():
            if val[3]==0:
                expup.append(f"  {val[0]}    ")
            else:
                if val[3]



        solve=False

arithmetic_arranger(["32 + 698", "38021 - 2", "45 + 43", "13 + 49"])

    #return arranged_problems
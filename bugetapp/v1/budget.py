# imports
import numpy as np

# classes


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        return False

    def get_balance(self):
        return self.balance

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount: float, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, cat):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {cat.category}")
            cat.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def __str__(self):

        title = self.category.center(30, "*")
        li = []
        ch = 0
        sp = 0
        sp2 = " "
        for d in self.ledger:
            for i in d:
                if type(d[i]) != int and type(d[i]) != float:
                    if len(i)+len(d[i])+3 > (len(title)):
                        exp = None
                        for j in d[i]:
                            ch += 1
                            if j == " ":
                                sp += 1
                                if len(d[i][:ch]) <= ((len(title))-len(i)-3):
                                    continue
                                else:
                                    exp = True
                                    li.append(f"{i} : {d[i][:ch]}")
                                    li.append(f"{sp2*len(i)}   {d[i][ch:]}")
                                    break
                        if exp != True:
                            li.append(f"{i} : {d[i]}")

                    else:
                        li.append(f"{i} : {d[i]}")
                else:
                    li.append(f"{i} : {d[i]} ")
        return title + "\n"+"\n".join([f"{i}" for i in li]) + "\n" + f"Total: {format(self.balance, '.2f')}"


def create_spend_chart(lis: list):
    """
    This will create a bar chart of percentage spent by each category.
    """
    print("\nPercentage spent by category")
    a = []
    total = 0
    for i in lis:
        spent = 0
        for j in i.ledger:
            if "Transfer to" not in j["description"]:
                if np.sign(j["amount"]) == (-1 or -1.0):
                    spent += abs(j["amount"])
                    total += abs(j["amount"])

        a.append({"category": i.category, "spent": spent})
    s2 = 0
    for i in reversed(range(11)):
        s = " "
        s2 += 1
        if i != 10:
            ln = len(str((i+s2)*10))
            print(f"{s*(ln-len(str(i*10)))}{i*10}|", end=" ")
        else:
            print(f"{i*10}|", end=" ")
        s3 = 0
        for j in a:
            s3 += 1
            per = (j["spent"]/total)*100
            if (per < i*10):
                if s3 == len(a):
                    print("")
                else:
                    print("", end="")
            else:
                if s3 == len(a):
                    print("o ")
                else:
                    print("o ", end=" ")
    print("    -"+"-"*len(a)*3)
    print('    ', end="")
 
    def letter_sep(dic: dict, key: str):
        """

        Desc:If dictionary(or dictionaries) in a list has a key whose value is required to be sperated in letters.
            Then this functon will seperate letters of value of particular key of all disctionaries in a list.
        It will seperate value of that particular key of all dictionaries in a list.

        Order:It will start with zero index and go with it for all values of that particular key of all dictionaries in a list.
            Then it will go to first index and so on. 

        Returns: list of letters.    
        """
        sp4 = 0
        li = []  # list of letters
        ln = 0  # longest category name
        for i in dic:
            if ln < len(i[key]):
                ln = len(i[key])
        while sp4 < ln:
            for l in dic:
                if sp4 < len(l[key]):
                    li.append(l[key][sp4])
                else:
                    continue
            sp4 += 1
        return li
    li = letter_sep(a, "category")  # list of letters
    li3=[]   # list of letters count 
    for i in a:
        li3.append(len(i["category"]))    
    li2=[]
    sp5=1 
    sp6=0
    print(" ",end="")
    for i in range(len(li)):
        li2.append(sp5)
        if sp5==len(a):
            print(li[i],end="")
            print("\n    ",end=" ")
            sp5=1
            if li3[sp5-1]==li2.count(sp5):
                print("   ",end="")
            
            
        else:
            print(li[i],end="  ")
            sp5+=1
            if li3[sp5-1]==li2.count(sp5):
                print("   ",end="")
    return ""            
# imports


#classes

class Category:
    print("Welcome to the Budget App")
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
    def check_fund(self, amount):
        if self.balance >= amount:
            return True
        return False
    def get_balance(self):
        return self.balance
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount:float, description = ""):
        if self.check_fund(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False
    def transfer(self, amount, cat):
        if self.check_fund(amount):
            self.withdraw(amount, f"Transfer to {cat.category}")
            cat.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
    
    def __str__(self):

        title = self.category.center(30, "*") 
        li = []
        ch = 0
        sp = 0
        sp2 =" "
        for d in self.ledger:
            for i in d:
                if type(d[i])!=int and type(d[i])!=float:
                    if len(i)+len(d[i])+3>(len(title)):
                        for j in d[i]:
                            ch+=1
                            if j ==" ":
                                sp+=1
                                if len(d[i][:ch])<((len(title))-len(i)-3):
                                    continue
                                else:
                                    li.append(f"{i} : {d[i][:ch]}")
                                    li.append(f"{sp2*len(i)}   {d[i][ch:]}")
                                    break
                                                  
                    else:
                        li.append(f"{i} : {d[i]}")
                else:
                    li.append(f"{i} : {d[i]}")
        return title + "\n"+"\n".join([f"{i}" for i in li ]) + "\n" + f"Total: {format(self.balance, '.2f')}"
    
    
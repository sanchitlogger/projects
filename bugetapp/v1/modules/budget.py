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
        return title + "\n"+"\n".join([f"{i['description'].ljust(23)}{format(i['amount'], '.2f').rjust(7)}" for i in self.ledger]) + "\n" + f"Total: {format(self.balance, '.2f')}"
    
    
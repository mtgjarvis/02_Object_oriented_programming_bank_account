class BankAccount:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return (f'Your interest rate is {self.interest_rate} and you account balance is ${self.balance}')

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def gain_interest(self):
        rate = self.interest_rate / 100
        interest = self.balance * rate
        self.balance += interest
        return self.balance



account1 = BankAccount(1000, 3)
account1.deposit(400)
account1.gain_interest()
print(account1)
# account1 = BankAccount(1000, 1.03)
# print(account1)
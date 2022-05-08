class bank_account:
    def __init__(self, interest_rate, account_balance):
        if account_balance > 0:
            self.account_balance = account_balance
        else :
            self.account_balance = 0
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print(self.account_balance)
        return self

    def yield_interest(self):
        # account balance * interest_rate = interest
        interest = self.account_balance * self.interest_rate
        self.account_balance = interest + self.account_balance
        return self

    @classmethod
    def print_all_accounts(self):
        print(cls.bank_account)
        
logan = bank_account(.01,100)
doofus = bank_account(.04,400)

# logan.deposit(100).deposit(500).deposit(2300).withdrawal(190).yield_interest().display_account_info()
# doofus.deposit(3100).deposit(4500).deposit(21300).withdrawal(990).yield_interest().display_account_info()

print_all_accounts()
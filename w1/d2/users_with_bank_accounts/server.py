class bank_account:
    def __init__(self, interest_rate, account_balance):
        if account_balance > 0:
            self.account_balance = account_balance
        else :
            self.account_balance = 0
        self.interest_rate = interest_rate

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
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

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.checking = bank_account()

    # def make_deposit(self, amount):
    #     self.account_balance += amount
    #     return self

    # def make_withdrawal(self, amount):
    #     if self.account_balance >= amount:
    #         self.account_balance -= amount
    #     return self

    # def display_user_balance(self):
    #     print(self.account_balance)
    #     return self

logan = User("Logan", "Goonie", 16, "goons@goonie.com")
logan.checking(.01,100)
# jeff = User("Jeff", "Davison", 20, "crillan@goonies.com")
# chuck = User("Chuck", "Breter", 9000, "wtfchuck@goonie.com")
# ayden = User("Ayden", "Farrel", 13, "stankfoot@goonie.com")

logan.checking.make_deposit(15)checking.make_deposit(26)checking.make_deposit(28)checking.make_withdrawal(24)checking.display_account_info()
# jeff.make_deposit(22).make_deposit(39).make_withdrawal(40).make_withdrawal(15).display_user_balance()
# ayden.make_deposit(72).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).display_user_balance()




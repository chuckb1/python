class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

logan = User("Logan", "Goonie", 16, "goons@goonie.com")
jeff = User("Jeff", "Davison", 20, "crillan@goonies.com")
chuck = User("Chuck", "Breter", 9000, "wtfchuck@goonie.com")
ayden = User("Ayden", "Farrel", 13, "stankfoot@goonie.com")

logan.make_deposit(15).make_deposit(26).make_deposit(28).make_withdrawal(24).display_user_balance()
jeff.make_deposit(22).make_deposit(39).make_withdrawal(40).make_withdrawal(15).display_user_balance()
ayden.make_deposit(72).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).display_user_balance()




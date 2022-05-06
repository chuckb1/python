class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

logan = User("Logan", "Goonie", 16, "goons@goonie.com")
jeff = User("Jeff", "Davison", 20, "crillan@goonies.com")
chuck = User("Chuck", "Breter", 9000, "wtfchuck@goonie.com")
ayden = User("Ayden", "Farrel", 13, "stankfoot@goonie.com")

logan.make_deposit(15)
logan.make_deposit(26)
logan.make_deposit(28)
logan.make_withdrawal(24)
logan.display_user_balance()
jeff.make_deposit(22)
jeff.make_deposit(39)
jeff.make_withdrawal(40)
jeff.make_withdrawal(15)
jeff.display_user_balance()
ayden.make_deposit(72)
ayden.make_withdrawal(20)
ayden.make_withdrawal(20)
ayden.make_withdrawal(20)
ayden.display_user_balance()




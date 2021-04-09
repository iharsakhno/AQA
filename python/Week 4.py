
class Account:
    """
    Implement an ATM (Automatic Teller Machine)
    User should be able:
    1. Create account with pin and balance +
    2. Check account balance + 
    3. Deposit money to account
    4. Withdraw money
    5. Tell user that not enough money on balance in case if step 4 required more money than user had
    """

    def __init__(self, pin=1234, balance=0):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(self.balance)

    def add_money(self, value):
        print(self.balance + value)

    def withdraw_money(self, value):
        if value > self.balance:
            print("Please to find a new job")
        else:
            print(self.balance - value)

       

acc1 = Account(0000, 1400)

acc1.check_balance()

acc1.add_money(500)

acc1.withdraw_money(300)

class Person:
    
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def get_full_name(self):
        print(f"{self.first_name} {self.last_name}")

person1 = Person("Will", "Smith")

person1.get_full_name()
    

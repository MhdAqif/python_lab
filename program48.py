class BankAccount:
    def assign(self):
        self.name = input("Enter depositor name: ")
        self.accno = input("Enter account number: ")
        self.acctype = input("Enter account type: ")
        self.balance = float(input("Enter initial balance: "))

    def deposits(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self):
        amount = float(input("Enter withdraw amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("\n----Account Details----")
        print("Depositor Name:", self.name)
        print("Account Number:", self.accno)
        print("Account Type:", self.acctype)
        print("Balance:", self.balance)


b = BankAccount()
b.assign()
b.deposits()
b.withdraw()
b.display()


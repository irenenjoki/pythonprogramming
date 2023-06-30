import datetime
#create a class BankAccount
class BankAccount:
    def __init__(self, account_number, balance, customer_name):#init shld have two underscores on both sides,input the attributes provided
        #assign the parameter passed to the attribute of the current instance self
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.date.today()
        self.customer_name = customer_name

    def deposit(self, amount):#this method is used to deposit an amount into the bank
        self.balance += amount#here the balance of the account is increased by adding the deposited amount
        return amount#shows final amount

    def withdraw(self, amount):#this method is responsible for withdrawing an amount from the bank
        if self.balance < amount:#checks if balance is less than amount withdrawn and if so returns insufficient balance
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount#if balance is insufficient it returns ammount that has been withdrawn

    def check_balance(self):#method used to check current balance
        print("Current balance:", self.balance)

    def customer_details(self):#this method is responsible for printing the customer details
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Current balance:", self.balance)

# Creating an instance of the BankAccount class
#prompt use to input their bank details
account_number = input("Enter your account number:\n ")
customer_name = input("Enter your name: \n")
balance = float(input("Enter your bank balance: \n"))

account = BankAccount(account_number, balance, customer_name)
#use the instance 'account', to call the methods; deposit,withdraw,check_balance,customer_balance

# Depositing amount and printing the returned value
#prompt user to enter amount to be deposited
deposited_amount = float(input("Enter the amount to deposit:\n "))
print("Amount Deposited:", account.deposit(deposited_amount))

# Withdrawing amount and printing the returned value
#prompt user to input amount they wish to withdraw
withdrawn_amount = float(input("Enter the amount to withdraw:\n "))
print("Amount Withdrawn:", account.withdraw(withdrawn_amount))

# Checking the balance
account.check_balance()

# Printing customer details
account.customer_details()
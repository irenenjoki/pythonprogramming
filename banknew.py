import datetime
#create a class BankAccount
class BankAccount:
    def _init_(self,account_number,balance,customer_name):#init shld have two underscores on both sides,input the attributes provided
        #assign the parameter passed to the attribute of the current instance self
        self.account_number=account_number
        self.balance=balance
        self.openingdate=datetime.date.today()
        self.customer_name=customer_name
        
    def deposit(self,amount):#this method is used to deposit an amount into the bank
        self.amount=amount#here the balance of the account is increased by adding the deposited amount
        return amount
    def withdraw(self,amount):#this method is responsible for withdrawing an amount from the bank
        self.amount=amount
        if self.balance < amount:#checks if balance is less than amount withdrawn and if so returns insufficient balance
         return "insufficient"
        else:
         self.balance==amount
         return "sufficient funds"
    def check_balance(self):#method used to check current balance
        self.amount=balance+depositedamount
        return self.amount
        
    def customer_details(self):#this method is responsible for printing the customer details
        #self.details=details
        #prompt use to input their bank details
        print("customer_name",self.customer_name)
        print("account_number",self.account_number)
        print("balance",self.balance)
        print("total",self.amount)
        print("openingdate",self.openingdate)
customer_name=input("input your name\n")
account_number=input("input your account number\n")
balance=float(input("input your balance\n"))
    
    # Creating an instance of the BankAccount class
account = BankAccount(account_number, balance, customer_name)
#use the instance 'account', to call the methods; deposit,withdraw,check_balance,customer_balance

depositedamount=float(input("input amount to deposit"))
print("amount deposited",account.deposit(depositedamount))
withdrawamount=float(input("input amount to withdraw"))
print("amount withdrawn",account.withdraw(withdrawamount))
# Checking the balance
account.check_balance()
# Printing customer details
account.customer_details()
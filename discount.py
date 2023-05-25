# user inputs an amount:
amount = float(input("enter amount in shillings"))
if amount > 1000:
    amount+=amount * 0.05
    # user gets a 5% discount if they purchase a good worth over 1000shillings:
    print("updated amount:",amount)
else:

 print("no discount")
 # if good purchased is less than 1000shillings no discount is offered:
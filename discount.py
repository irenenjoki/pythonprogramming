amount = float(input("enter amount in shillings"))
if amount > 1000:
    amount+=amount * 0.05
    print("updated amount:",amount)
else:

 print("no discount")
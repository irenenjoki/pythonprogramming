#user is prompted to input age:
age = int(input("enter age:"))
income = float(input("enter income:"))
if age >= 21 and income >= 21000:
    print("congratulations! you qualify for the loan.")
    #in order to get a loan from the bank, one has to be 21 yrs and above and request more or 21000shillings:
else:
    print("unfortunately, we are unable to offer you a loan at this time.")
    #user is denied a loan if one or none of the conditions are met:
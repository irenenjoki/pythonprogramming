#prompts user to input their citizenship:

kenyan=input("enter nationality:")
age=int(input("enter age:"))
if age>=18 and kenyan.lower()=="kenyan":
    print("eligible to vote")
            #when conditions required are met, the user is allowed voting:

else:
    print("not eligible to vote")
                #if one or none of the requirements are met, the use is denied voting:
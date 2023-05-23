kenyan=input("enter nationality")
age=int(input("enter age:"))
if age>=18 and kenyan.lower()=="kenyan":
    print("eligible to vote")
else:
    print("not eligible to vote")
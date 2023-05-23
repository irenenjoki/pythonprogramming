citizenship=input("enter citizenship:")
citizenship_options=["kenyan", "ugandan", "tanzanian"]
if citizenship.lower() in citizenship_options:
    age=int(input("enter your age:"))
    if age>=18:
        print("you are eligible to vote.")
    else:
        print("you are not eligible to vote.")
else:
    print("you are not eligble to vote or a citizen.")
            
income=int(input("Enter the income:"))
if income<=250000:
    print("tax=",0)
elif income>250000 and income<=500000:
    print("tax=",0.05*income)
elif income>500000 and income<=1000000:
    print("tax=",0.1*income)
else:
    print("tax=",0.3*income)

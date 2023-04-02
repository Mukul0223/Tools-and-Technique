age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to cast vote")
else:
    a=18-age
    print("Not eligible to cast vote.")
    print(a,"years left to be eligible")
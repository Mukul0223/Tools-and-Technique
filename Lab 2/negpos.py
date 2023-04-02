x=0
while x!=-1:
    n=int(input("Enter a number:"))
    x=n
    if n<0:
        print("Negative")
    elif n>-1:
        print("Positive")
    else:
        print("Invalid input")
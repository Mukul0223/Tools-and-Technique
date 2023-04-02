def fact(num):
    if  num < 0:
        print("Factorial does not exist.")
    elif num > 0:
        factorial=1
        for i in range(1,num+1):
            factorial = factorial*i
        print("Factorial of ",num,"=",factorial)
num=int(input("Enter a number:"))
fact(num)
        
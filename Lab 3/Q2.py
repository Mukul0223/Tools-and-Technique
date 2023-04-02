def sumdigit(num):
    sum = 0
    while num > 0:
        digit=num%10
        num=num//10
        sum=sum+digit
    print(sum)

num=int(input("Enter a number:"))
sumdigit(num)
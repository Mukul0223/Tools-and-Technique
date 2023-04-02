def reverse(num):
    n=""
    while num>0:
        digit=num%10
        num=num//10
        n=n+str(digit)
    print(n)
num=input("Enter a number:")
reverse(int(num))
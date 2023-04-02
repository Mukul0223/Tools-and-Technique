# Write a program to find square root of a number using Newtons method.
def squareroot(n,l):
    x=n
    count=0
    while (1):
        count+=1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < l):
            break
        x = root
    return root

n=float(input("Enter a number:"))
l=float(input("Enter the tolerance rate:"))
print(squareroot(n,l))

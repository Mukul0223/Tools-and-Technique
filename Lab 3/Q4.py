def HCF(a,b):
    if b==0:
        return a
    else:
        return HCF(b, a % b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("HCF of",a,"and",b,"is",HCF(a,b))

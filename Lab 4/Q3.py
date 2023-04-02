# Write a program to find exponentiation(power) of a number.
def exponentiation(n,b):
    result=(n**b)
    return result
n=int(input("Enter a number: "))
b=int(input("Enter the power:"))
print(exponentiation(n,b))
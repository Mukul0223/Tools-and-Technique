#Write a function that accept three integers and return TRUE if they are sorted otherwise return FALSE.
def check(a,b,c):
    if a<=b<=c:
        return True
    else:
        return False
    
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
print(check(a,b,c))

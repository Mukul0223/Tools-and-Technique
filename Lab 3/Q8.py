#n = 5
def pattern(n):
 for i in range(n):
    for j in range(i + 1):
        x=65+i-j
        print(chr(x), end=" ")
    print()

n=int(input("Enter a number: "))
pattern(n)
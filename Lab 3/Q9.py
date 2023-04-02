def pattern(n):
 for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,i+1):
            print(j,end=" ")
    else:
       for j in range(1,i + 1):
        x=i-j+1
        print(x,end=" ")  
    print()

n=int(input("Enter a number: "))
pattern(n)
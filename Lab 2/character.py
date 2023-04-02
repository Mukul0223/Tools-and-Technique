string=input("Enter a character:")
if string.isupper():
        print(string.lower())
elif string.islower():
        print(string.upper())
else:
        print("Invalid input")
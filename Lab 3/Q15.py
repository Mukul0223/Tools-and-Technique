is_palindrome = lambda s: s == s[::-1]
s=input("Enter a string:")
print(f"{s} is a palindrome: {is_palindrome(s)}")
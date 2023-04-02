# Write a program that counts the amount of lowercase. Uppercase and digit entered by user.
def count_chars(string):
    """Counts the number of lowercase, uppercase, and digit characters in a string."""
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    for c in string:
        if c.islower():
            lowercase_count += 1
        elif c.isupper():
            uppercase_count += 1
        elif c.isdigit():
            digit_count += 1
    return lowercase_count, uppercase_count, digit_count

string = input("Enter a string: ")
lowercase_count, uppercase_count, digit_count = count_chars(string)
print("Lowercase characters: ", lowercase_count)
print("Uppercase characters: ", uppercase_count)
print("Digit characters: ", digit_count)

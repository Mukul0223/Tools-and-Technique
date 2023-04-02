# Write a program to find whether a given character is present in a string or not.
def is_character_present(string, character):
    for c in string:
        if c == character:
            return True
    return False
string = input("Enter a string:")
character = input("Enter a character:")
result = is_character_present(string, character)
print(result)


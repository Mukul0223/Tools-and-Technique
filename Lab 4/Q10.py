#Write a program that encrypts a message by adding a key value to every character (CaesarCipher)
def caesar_cipher(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted

message = input("Enter a message:")
key = int(input("Enter a key value:"))
encrypted = caesar_cipher(message, key)
print(encrypted)
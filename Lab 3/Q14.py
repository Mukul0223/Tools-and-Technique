def count_letter(s):
    upper_count=0
    lower_count=0
    for char in s:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    return upper_count,lower_count
s=input("Enter a string:")
print("Upper count and lower count in string is", count_letter(s))
#Write a program to find maximum of a list of a number.
numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = float(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)

max_num = max(numbers)

print("The maximum number in the list is:", max_num)

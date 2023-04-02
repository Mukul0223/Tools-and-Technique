def largest(numbers):
 max_value = numbers[0]
 for number in numbers:
    if number > max_value:
        max_value = number
 print("The largest number is:", max_value)

numbers = [int(num) for num in input("Enter a list of numbers separated by space: ").split()]
largest(numbers)
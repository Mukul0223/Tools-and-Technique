def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    if sum(divisors) == number:
        return True
    return False
number=int(input("Enter a number:"))
print(is_perfect(number))

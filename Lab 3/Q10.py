def decimal_to_base_b(decimal_num, b):
    base_b_num = ""
    while decimal_num > 0:
        digit = decimal_num % b
        base_b_num = str(digit) + base_b_num
        decimal_num = decimal_num // b
    return base_b_num

decimal_num = int(input("Enter the decimal number: "))
b = int(input("Enter the base: "))
base_b_num = decimal_to_base_b(decimal_num, b)
print("The equivalent number with base {} is: {}".format(b, base_b_num))

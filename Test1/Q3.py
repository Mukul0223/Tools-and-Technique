# To that creates a list of 20 random integers. Then create two list, even and odd list that has all the even and odd numbers in sorted form.
import random
random_list=[random.randint(1,100) for i in range(20)]
odd_list=[]
even_list=[]
for num in random_list:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Odd list is ",odd_list)
print("Even list is",even_list)
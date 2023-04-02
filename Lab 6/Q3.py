# WAP to enter a number, find the factorial of a number, check, whether the number is prime or not, find the square of that number, through object and class concept
class number:
    def __init__(self,num):
        self.num=num

    def factorial(self):
        fact=1
        for i in range(1,self.num+1):
            fact=fact*i
        print("Factorial of number:",fact)
    
    def is_prime(self):
        if self.num<2:
            print("Not prime")
            return
        for i in range(2,int(self.num**0.5)+1):
            if self.num%i==0:
                print("Not prime")
                return
        print("Is Prime")

    def square(self):
        self.num=self.num**2
        print("Square of number:",self.num)

num=number(3)
num.factorial()
num.is_prime()
num.square()
    



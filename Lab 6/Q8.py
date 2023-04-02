# WAP to program to calculate simple interest and compound interest with appreciate input given to the program e.g p, r, t input.
class Interest:
    def __init__(self,p,r,t,n):
        self.p = p
        self.r = r
        self.t = t
        self.n=n
    def calculate_si(self):
        return self.p*(1+self.r*self.t)
    def calculate_ci(self):
        return self.p*(1+self.r/self.n)/self.n*self.t

interest1=Interest(10000,5,7,3)
print("Simple Interest is",interest1.calculate_si())
print("Compound Interest is",interest1.calculate_ci())
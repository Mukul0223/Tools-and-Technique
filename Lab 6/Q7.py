# WAP to enter sides of different geometric figure, find the area of any 5 geometric figure
class Area:
    PI=3.14
    def __init__(self,l,b,r):
        self.l = l
        self.b = b
        self.r=r
    def rectangle(self):
        return self.l * self.b
    def circle(self):
        return Area.PI*self.r**2
    def rhombus(self):
        return 0.5*self.l*self.b
    def trapezium(self):
        return ((self.b+self.l)*self.r)/2
    def triangle(self):
        return (self.l*self.r)/2
area1=Area(12,7,25)
print("Area of rectangle is ",area1.rectangle())
print("Area of circle is ",area1.circle())
print("Area of rhombus is ",area1.rhombus())
print("Area of trapezium is ",area1.trapezium())
print("Area of triangle is ",area1.triangle())

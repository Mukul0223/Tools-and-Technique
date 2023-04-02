# WAP that has a class circle. Use class variable to define the values of constant circle.PI. Use class variable to calculate area and circumference with specified radius.
class circle:
    PI = 3.14
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.PI*self.r**2
    def circumference(self):
        return 2*circle.PI*self.r
    
r=circle(7)
print("Area of circle is ",r.area())
print("Circumference of circle is ",r.circumference())

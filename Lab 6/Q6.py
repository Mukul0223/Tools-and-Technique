# Write a class rectangle that has attribute length, Breadth and a method area which returns area of the rectangle.
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
rectangle1=rectangle(23,34)
rectangle2=rectangle(45,67)
print("Area of rectangle is ",rectangle1.area())
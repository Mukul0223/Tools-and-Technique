# Wap to count the number of object created.
class student:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
    def showinfo(self):
        print("Name:",self.name,"Age:",self.age)
student1=student('Max',34)
student2=student('Sam',35)
student3=student('Toby',33)
print("Total number of object created",student.count)


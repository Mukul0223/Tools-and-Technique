# WAP that has a class Student that stores roll number, name, and marks (in three subjects). Display information roll number, total marks stored about a student.
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def total_marks(self):
        return sum(self.marks)
    def display_info(self):
        print("Roll no: {0}".format(self.roll_no))
        print("Name: {0}".format(self.name))
        print("Total marks: {0}".format(self.total_marks()))

student1=Student(1,'Max',[80,89,77])
student1.display_info()
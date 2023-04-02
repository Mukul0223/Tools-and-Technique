# Write a program that has a class Student storing student information including DOB. The program should subtract DOB from present date to find out whether you are eligible to cast vote or not.
import datetime
class student:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    def cast_vote(self):
        today=datetime.date.today()
        age=today.year - self.dob.year-((today.month,today.day)<(self.dob.month,self.dob.day))
        if age >=18:
            print("You are eligible to cast vote")
        else:
            print("You are not eligible to cast vote")
s=student("John",datetime.date(2002,2,2))
s.cast_vote()
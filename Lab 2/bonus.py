gender=input("Enter the gender of employee:")
salary=int(input("enter the salary of employee:"))
bonus_F=10/100*salary
bonus_M=5/100*salary
bonus_E=5/100*salary
if gender =="Male" and salary <= 20000:
   print("t_salary=",salary+bonus_E+bonus_M)
elif gender =="Female" and salary <= 20000:
    print("t_salary=",salary+bonus_F+bonus_E)
elif gender =="Female" and salary > 20000:
     print("t_salary=",salary+bonus_F)
elif gender =="Male" and salary > 20000:
    print("t_salary=",salary+bonus_M)

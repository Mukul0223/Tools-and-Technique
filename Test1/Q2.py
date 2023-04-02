#Program to calculate net salary, gross salary of an employ, Considering, Basic pay,HRA, DA and other deduction.Determine whether the employ will pay the tax or not
basic_pay=float(input("Enter th basic pay:"))
hra=float(input("Enter hra:"))
da=float(input("Enter da:"))
deduction=float(input("Enter deduction:"))
gross_salary=basic_pay+hra+da
net_salary=gross_salary-deduction
print("Gross salary is ",gross_salary)
print("Net salary is ",net_salary)

if net_salary>500000:
    print("Tax needs to be paid.")
else:
    print("Tax not to be paid")

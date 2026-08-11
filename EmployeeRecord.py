employee = ("Arjun", "Developer", 45000, 3)
Employee_Name,Designation,Monthly_Salary,Years_of_Experience=employee
anual_salary=Monthly_Salary*12
b=0
total=0
if Years_of_Experience<2:
    b=anual_salary*0.05
elif 2<=Years_of_Experience<=5:
    b=anual_salary*0.1
else:
    b=anual_salary*0.15
total=anual_salary+b
print(f"Employee Name: {Employee_Name}")
print(f"Designation: {Designation}")
print(f"Experience: {Years_of_Experience}")
print(f"Monthly Salary: {Monthly_Salary}")
print(f"Anual Salary: {anual_salary}")
print(f"Bonus: {b}")
print(f"Total: {total}")
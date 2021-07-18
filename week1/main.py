#!/usr/bin/python3
from andy_packages.company import Developer, Employee, Manager
import andy_packages as ap
import datetime

# create instance, Employ is the class
emp1 = ap.Employee('andy','lee','30000')
emp2 = ap.Employee('jasmine','yeah','40000')

Employee.set_rasie_amt(1.05)

# print(Employee.raise_amt)
# print(emp1.raise_amt)


# Tutorial 1
# It is the same, you can call "self = emp1 or emp1" 
# print(emp1.fullname())
# print(Employee.fullname(self = emp1))



# Tutorial3
# How we use classmethod to create andy from string
# emp_str_1 = 'Andy-Lee-9000'
# emp3 = Employee.from_string(emp_str_1)

# print(emp3.fullname())

# my_date = datetime.date(2021,7,18)
# print(Employee.is_workday(my_date))


# Tutorial 4 , change the variable without changing the original class 
dev_1 = Developer("Jasmine","Yeah",100000,"python")
dev_2 = Developer("James","Lebron",300000,"c++")

dev_1.apply_raise()
# print(dev_1.prog_lang)

mgr_1 = Manager("Andy","Lee",1000000,[dev_1,dev_2])

print(issubclass(Manager,Employee))
print(isinstance(mgr_1,Manager))
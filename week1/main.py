#!/usr/bin/python3
from andy_packages.tool import Employee
import andy_packages as ap


emp1 = ap.Employee('andy','lee','30000')
emp2 = ap.Employee('jasmine','yeah','40000')


# It is the same, you can call "self = emp1 or emp1" 
print(emp1.fullname())
print(Employee.fullname(self = emp1))
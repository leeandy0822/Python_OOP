import math


class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        # if somebody call this init function, the employee will add 1
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amt)
        # Tutorial2
        # Employee.raise_amount = the entire class raise_amount will change
        # emp1.raise_amount = only change the class emp1
    
    @classmethod
    def set_rasie_amt(cls,amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls,emp_str):
        first, last , pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        

# Tutorial3
# regular method take self as first argument
# cls = class


class Developer(Employee):
    raise_amt = 1.2
    
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        
        
        
class Manager(Employee):
    
    def __init__(self, first, last, pay,employees = None):
        super().__init__(first, last, pay)
        if employees is None :
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
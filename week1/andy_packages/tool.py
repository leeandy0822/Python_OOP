import math




class Employee():
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

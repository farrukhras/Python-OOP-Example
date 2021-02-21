class Employee:

  def __init__(self, first, last, pay): # sort of a constructor
    self.first = first 
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@comapny.com"

  def fullname(self): # class method
    return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Farrukh", "Rasool", "75000")
emp_2 = Employee("Zack", "Snyder", "60000")

print(emp_1.fullname())
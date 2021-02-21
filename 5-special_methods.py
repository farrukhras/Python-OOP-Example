class Employee:

  # class variables
  raise_amount = 1.04

  def __init__(self, first, last, pay): # sort of a constructor
    self.first = first 
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@comapny.com"

  def fullname(self): # class method
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  def __repr__(self): # used for debugging or for developers (if there is no __str__ method than python fallbacks to the __repr__ method)
    return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

  def __str__(self): # used for displaying to the end user (python uses this special method by default, if it is present, otherwise uses the __repr__ method)
    return '{} - {}'.format(self.fullname(), self.email)

  def __add__(self, other): # return the sum of the pays of the specified employees
    return self.pay + other.pay

  def __len__(self):
    return len(self.fullname())

emp_1 = Employee("Farrukh", "Rasool", 75000)
emp_2 = Employee("Zoraiz", "Qureshi", 60000)

print(emp_1 + emp_2) # returns the sum of the pays of the specified employees

print(len(emp_1))
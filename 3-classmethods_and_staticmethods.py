class Employee:
  # class variables
  raise_amount = 1.04
  num_of_employees = 0

  def __init__(self, first, last, pay): # sort of a constructor
    self.first = first 
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@comapny.com"
    Employee.num_of_employees += 1

  def fullname(self): # class method
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)
  
  @staticmethod
  def is_work_day(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

emp_1 = Employee("Farrukh", "Rasool", 75000)
emp_2 = Employee("Zoraiz", "Qureshi", 60000)

# ******************************
# class methods tests start here

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# make an employee object from a string input
# emp_str_1 = "Ahmed-Farhan-90000"
# emp_str_3 = "Ramez-Salman-85000"
# emp_str_2 = "Hamza-Farooq-80000"

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# class methods tests ends here
# ******************************

# ******************************
# static methods tests start here

import datetime

my_date = datetime.date(2021, 2, 20)
print(Employee.is_work_day(my_date))

# static methods tests ends here 
# ******************************

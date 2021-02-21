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

print("Number of Employees: ", Employee.num_of_employees)

emp_1 = Employee("Farrukh", "Rasool", 75000)
emp_2 = Employee("Zack", "Snyder", 60000)

print("Standard Raise Amount for Employee 1: ", emp_1.raise_amount) # raise amount for emp_1 before locally assigning new value of raise_amount to Employee instance emp_1

emp_1.apply_raise()
print("Employee 1 new pay with standard raise: ", emp_1.pay) # raise amount with the standard raise value

emp_1.raise_amount = 1.05

print("Standard Raise Amount for all Employees: ", Employee.raise_amount)
print("Standard Raise Amount for Employee 1: ", emp_1.raise_amount) # raise amount for emp_1 after locally assigning new value of raise_amount to Employee instance emp_1
print("Standard Raise Amount Employee 2: ", emp_2.raise_amount)

emp_1.pay = 75000
emp_1.apply_raise()
print("Standard Raise Amount Employee 1 with new raise: ", emp_1.pay) # raise amount after setting new raise value

print("Number of Employees: ", Employee.num_of_employees)
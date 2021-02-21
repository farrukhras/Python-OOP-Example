class Employee:

  # class variables
  raise_amount = 1.04

  def __init__(self, first, last): # sort of a constructor
    self.first = first 
    self.last = last

  @property
  def email(self):
    return "{}.{}@email.com".format(self.first, self.last)

  @property
  def fullname(self): # class method
    return '{} {}'.format(self.first, self.last)

  @fullname.setter
  def fullname(self, name):
    first, last = name.split(" ")
    self.first = first
    self.last = last 

  @fullname.deleter
  def fullname(self):
    print("Delete Name!")
    self.first = None
    self.last = None

emp_1 = Employee("Farrukh", "Rasool")

emp_1.fullname = "Zoraiz Qureshi"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
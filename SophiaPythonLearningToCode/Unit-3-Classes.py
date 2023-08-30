#Unit 3: Classes


class Dog:
  def __init__(self,name,breed,age,color):
    self.name = name
    self.breed = breed
    self.age = age
    self.color = color

  def bark(self):
    print("Woof")

  def fetch(self):
    print(self.name," went to fetch.")

# an instance of theSnipping Dog class
my_dog = Dog("Fluffy","Beagle",2,"Brown")
my_dog1 = Dog("Fluffy","Beagle",2,"Brown")
my_dog2 = Dog("Mochi","Mutt",5,"White")
my_dog3 = Dog("Wolfie","Maltese",10,"Black")

print(my_dog1.name, my_dog1.breed, my_dog1.age, my_dog1.color)
print(my_dog2.name, my_dog2.breed, my_dog2.age, my_dog2.color)
print(my_dog3.name, my_dog3.breed, my_dog3.age, my_dog3.color)
#print(my_dog.breed)
#print(my_dog.age)
#print(my_dog.color)


my_string = "Sophia"
print(my_string.upper())
print(my_string.lower())


class PeopleCounter:
   x = 0
 
   def anotherOne(self) :
     self.x = self.x + 1
     print("So far",self.x)

people = PeopleCounter() # creation of an instance of the class PeopleCounter
people.anotherOne()
people.anotherOne()
people.anotherOne()
people.anotherOne()


def __init__(self, <otherParameters>):


class User: 
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword

account = User('blue', 'mypass')

print(account)
print(account.username)
print(account.password)
account.username = 'whybye'
print(account.username)
print(account.password)
print(type(account))


import datetime

class User: 
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
    self.activeUser = True #new variable with True as default value
    self.numOfLogins = 0 #new variable with 0 as default value 
    self.dateJoined = datetime.date.today() #new variable using the datetime module

account = User('blue', 'mypass')

print(account)
print(account.username)
print(account.password)
print(account.activeUser)
print(account.numOfLogins)
print(account.dateJoined)
print(type(account))


import datetime 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
 
    self.activeUser = True
    self.numOfLogins = 0
    self.dateJoined = datetime.date.today()
  
  #display number of logins
  def show_num_logins(self):
    return self.username + " logged in " + str(self.numOfLogins) + " times."
 
  #increase number of logins
  def logged_in(self):
    self.numOfLogins = self.numOfLogins + 1
 
  #logging into the user account
  def login(self, uname, pword):
    if (self.username == uname and self.password == pword):
      print("Login successful")
      self.logged_in()
    else:
      print("Incorrect username and password combination.")
 
account = User('blue','mypass')
account.logged_in()
account.logged_in()
print(account.show_num_logins())
account.logged_in()
print(account.show_num_logins())


import datetime 
class Employee:
  def __init__(self, fname, lname, empid, title, sal):
    self.firstname = fname
    self.lastname = lname
    self.employeeid = empid
    self.jobtitle = title
    self.salary = sal
 
    self.hiredate = datetime.date.today()
  
  #returns first name
  def get_firstname(self):
    return self.firstname
  
  #sets firstname if fname isn't an empty string
  def set_firstname(self,fname):
    if len(fname) > 0:
      self.firstname = fname
 
  #returns last name
  def get_lastname(self):
    return self.lastname
  
  #sets lastname if lname isn't an empty string
  def set_lastname(self,lname):
    if len(lname) > 0:
      self.lastname = lname
 
  #returns job title
  def get_jobtitle(self):
    return self.jobtitle
  
  #sets job title if job title isn't an empty string
  def set_jobtitle(self,title):
    if len(title) > 0:
      self.jobtitle = title
 
  #return employee id
  def get_employeeid(self):
    return "Employee ID: " + str(self.employeeid)
 
  #returns salary
  def get_salary(self):
    return "${:,.2f}".format(self.salary)
  
  #sets salary if salary isn't an empty string
  def set_salary(self,sal):
    if sal > 0:
      self.salary = sal
 
  #increase salary
  def increase_salary(self,percent):
    if percent > 0:
      self.set_salary(self.salary + self.salary * percent)
    else:
      print("Increase of salary must be greater than 0.")

blue = Employee("Jack","Black",10001,"Account Manager",50000)
print(blue.get_firstname())
print(blue.get_lastname())
print(blue.get_employeeid())
print(blue.get_jobtitle())
print(blue.get_salary())

#increase salary
blue.increase_salary(0.05)
print("After COL increase: " + blue.get_salary())



import datetime
class Member:
  expiry_days = 365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
    
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)

#Subclass for us to use for administrators
class Admin(Member):
  pass

#Subclass for us to use for normal users
class User(Member):
  pass

TestMember = Member('blue', 'python')
print(TestMember.first_name)
print(TestMember.last_name)
print(TestMember.expiry_date)

TestAdmin = Admin('root','admin')
print(TestAdmin.first_name)
print(TestAdmin.last_name)
print(TestAdmin.expiry_date)
 
TestUser = User('Artic','Smith')
print(TestUser.first_name)
print(TestUser.last_name)
print(TestUser.expiry_date)


import datetime 
 
class Member:
  expiry_days = 365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
 
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)
 
#Subclass for us to use for administrators
class Admin(Member):
  expiry_days = 365 * 50
  
  def __init__(self, first, last, secret):
    super().__init__(first,last)
    self.secret_code = secret
 
#Subclass for us to use for normal users
class User(Member):
  pass
 
TestMember = Member('blue','python')
print(TestMember.first_name)
print(TestMember.last_name)
print(TestMember.expiry_date)
 
TestAdmin = Admin('root','admin','ABRACADABRA')
print(TestAdmin.first_name)
print(TestAdmin.last_name)
print(TestAdmin.secret_code)
print(TestAdmin.expiry_date)
 
print("--------")
 
TestUser = User('Artic','Smith')
print(TestUser.first_name)
print(TestUser.last_name)
print(TestUser.expiry_date)



import datetime 
 
class Member:
  expiry_days = 365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
 
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)
 
  def show_expiry(self):
    return f'{self.first_name} {self.last_name} expires on {self.expiry_date}'
    
  def show_status(self):
    return f'{self.first_name} {self.last_name} is a member'
 
#Subclass for us to use for administrators
class Admin(Member):
  expiry_days = 365 * 50
  
  def __init__(self, first, last, secret):
    super().__init__(first,last)
    self.secret_code = secret
  def show_status(self):
    return f'{self.first_name} {self.last_name} is an Admin'
 
#Subclass for us to use for normal users
class User(Member):
  def show_status(self):
    return f'{self.first_name} {self.last_name} is a User'
 
TestMember = Member('blue','python')
print(TestMember.show_status())
#print(TestMember.first_name)
#print(TestMember.last_name)
#print(TestMember.show_expiry)

print("--------")
 
TestAdmin = Admin('root','admin','ABRACADABRA')
print(TestAdmin.show_status())
#print(TestAdmin.first_name)
#print(TestAdmin.last_name)
#print(TestAdmin.secret_code)
#print(TestAdmin.show_expiry)
 
print("--------")
 
TestUser = User('Artic','Smith')
print(TestUser.show_status())
#print(TestUser.first_name)
#print(TestUser.last_name)
#print(TestUser.secret_code)
#print(TestUser.show_expiry)



total = 0; 
 
def sum(arg1,arg2):
   total = arg1 + arg2; 
   print ("Local total: ",total)
   return total;
 
sum(10,20);
print ("Global total : ", total)



#global scope
first_name = 'Global'

def display_name():
  #local scope
  last_name = 'local'
  return f'{first_name} is a global variable, while {last_name} is a local variable'

print(display_name())


#global scope
first_name = 'Global'

def display_name():
  #local scope
  last_name = 'local'
  
  #changing global name
  global first_name 
  first_name = 'changeMe'
  return f'{first_name} is a global variable, while {last_name} is a local variable'

print(display_name())
print(first_name)



import datetime 
 
class Member:
  expiry_days = 365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
 
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)
 
  def show_expiry(self):
    return f'{self.first_name} {self.last_name} expires on {self.expiry_date}'
 
  def show_status(self):
    return f'{self.first_name} {self.last_name} is a Member'
 
#Subclass for us to use for administrators
class Admin(Member):
  expiry_days = 365 * 100
 
  def __init__(self, first, last, secret):
    super().__init__(first,last)
    self.secret_code = secret
  def show_status(self):
    return f'{self.first_name} {self.last_name} is an Admin'
 
#Subclass for us to use for normal users
class User(Member):
  def show_status(self):
    return f'{self.first_name} {self.last_name} is a User'
 
print(Admin.__dict__)
help(User)



import datetime 
class Person:
  def __init__(self, fname, lname, title):
    self.firstname = fname
    self.lastname = lname
    self.jobtitle = title
 
    self.hiredate = datetime.date.today()
  
  #returns first name
  def get_firstname(self):
    return self.firstname
  
  #sets firstname if fname isn't null
  def set_firstname(self,fname):
    if len(fname) > 0:
      self.firstname = fname
 
  #returns last name
  def get_lastname(self):
    return self.lastname
  
  #sets lastname if lname isn't null
  def set_lastname(self,lname):
    if len(lname) > 0:
      self.lastname = lname
 
  #returns job title
  def get_jobtitle(self):
    return self.jobtitle
  
  #sets job title if job title isn't null
  def set_jobtitle(self,title):
    if len(title) > 0:
      self.jobtitle = title

class Employee(Person):
  def __init__(self,fname,lname,title,sal,empid):
    super().__init__(fname,lname,title)
    self.employeeid = empid
    self.salary = sal
    self.vacationdaysperyear = 14
    self.vacationdays = self.vacationdaysperyear
    
  #return employee id
  def get_employeeid(self):
    return "Employee ID: " + str(self.employeeid)
 
  #returns salary
  def get_salary(self):
    return "${:,.2f}".format(self.salary)
  
  #sets salary if salary isn't null
  def set_salary(self,sal):
    if sal > 0:
      self.salary = sal
 
  #increase salary
  def increase_salary(self,percent):
    if percent > 0:
      self.set_salary(self.salary + self.salary * percent)
    else:
      print("Increase of salary must be greater than 0.")
      
  #increase vacation days per year
  def increase_vacation_days_per_year(self,days):
    if days > 0:
      self.vacationdaysperyear = self.vacationdaysperyear + days
      
  #increase vacation days
  def increase_vacation_days(self,days):
    if days > 0:
      self.vacationdays = self.vacationdays + days
      
  #increase vacation days by year
  def increase_vacation_days_yearly(self):
    self.vacationdays = self.vacationdays + self.vacationdaysperyear
    
  #take spme vacation days
  def take_vacation_days(self,days):
    if days > 0 and self.vacationdays - days >= 0:
      self.vacationdays = self.vacationdays - days
    elif days <= 0:
      print("Vacation days taken must be greater than 0")
    elif self.vacationdays - days < 0:
      print("Employee does not have enough vacation time available")
      
  #return vacation days
  def get_vacation_days(self):
    return "Vacation days: " + str(self.vacationdays)

class Contractor(Person):
  def __init__(self,fname,lname,title,wage,contractorid):
    super().__init__(fname,lname,title)
    self.contractorid = contractorid
    self.hourlywage = wage
    
  #return contractor id
  def get_contractorid(self):
    return "Contractor ID: " + str(self.contractorid)
    
  #set hourly wage
  def set_hourlywage(self,wage):
    if wage > 0:
      self.hourlywage = wage
      
  #returns wage
  def get_hourlywage(self):
    return "${:,.2f}".format(self.hourlywage)

  #sets job wage if wage greater than 0
  def set_get_hourlywage(self,get_hourlywage):
    if get_hourlywage > 0:
      self.wage = get_hourlywage

emp1 = Employee('Jack','Black','Store Manager',50000,10001)
 
print(emp1.get_firstname())
print(emp1.get_lastname())
print(emp1.get_employeeid())
print(emp1.get_jobtitle())
print(emp1.get_salary())
 
print(emp1.get_vacation_days())
emp1.take_vacation_days(10)
print(emp1.get_vacation_days())
emp1.take_vacation_days(10)
emp1.take_vacation_days(-1)
 
emp1.increase_vacation_days_yearly()
print(emp1.get_vacation_days())

con = Contractor('Temp','Emp','Developer',60,20001)
print(con.get_firstname())
print(con.get_lastname())
print(con.get_contractorid())
print(con.get_jobtitle())
print(con.get_hourlywage())
print(con.set_hourlywage(50))
print(con.get_hourlywage())



import math
print(dir(math))


import math
help(math)


from math import pi


from math import pi
print(pi)


#to use a function, put modulename.functionname
import math
print(math.pi)


import math as m
print("The value of pi is", m.pi)


from math import pi, sqrt
print(pi)
print(sqrt)


#import everything from module and use names directly
#be careful with this. more than one function may have the same name in diff modules
from math import *
print(pi)


from statistics import median
print(median([1, 3, 5, 7, 9, 9]))


import statistics 
print(statistics.median([1, 33, 14, 25, 3]))



import random

number1 = random.random()
print(number1)
number2 = random.random() * 100
print(number2)

number3 = random.randint(1, 100) # an int from 1 to 100
print(number3)
number4 = random.randint(101, 200) # an int from 101 to 200 
print(number4)
number5 = random.randint(0, 7) # an int from 0 to 7
print(number5)

number6 = random.randrange(1, 100) # an int from 1 to 99
print(number6)
number7 = random.randrange(100, 200, 2) # an even int from 100 to 198
print(number7)
number8 = random.randrange(11, 250, 2) # an odd int from 11 to 249
print(number8)


temperature.py:
def to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def to_fahrenheit(celsius):
  fahrenheit = celsius * 9/5 + 32
  return fahrenheit


import temperature

temp = 20
print(temp, "Celsius = ", round(temperature.to_fahrenheit(temp)), "Fahrenheit")
print(temp, "Fahrenheit = ", round(temperature.to_celsius(temp)), "Celsius")



#when creating a module for import it is important to document for other people:
temperature.py:
"""
This module contains functions for converting temperature between degrees Fahrenheit
and degrees Celsius 
"""

def to_celsius(fahrenheit):
  """
  Accepts degrees Fahrenheit (fahrenheit argument)
  Returns degrees Celsius 
  """
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def to_fahrenheit(celsius):
  """
  Accepts degrees Celsius (celsius argument)
  Returns degrees Fahrenheit 
  """
  fahrenheit = celsius * 9/5 + 32
  return fahrenheit



#poem.txt:
Roses Are Red, 
Violets are blue, 
Sugar is sweet, 
And so are you.


fhandler = open('poem.txt')
count = 0
for line in fhandler:
  count = count + 1
print('Line count: ', count)


fhandler = open('poem.txt')
text = fhandler.read()
print(text)


fout = open('output.txt', 'w')
line1 = "putting in a line of text,\n"
fout.write(line1)
fout.close()


fout = open('firstexample.txt', 'w')
fout.write('Putting in a line of text\n')
fout.close()
fout = open('firstexample.txt', 'w')
fout.write('Putting in a line of text\n')
fout.close()
fout = open('firstexample.txt', 'w')
fout.write('Putting in a line of text\n')
fout.close()


fout = open('firstexample.txt', 'a')
fout.write('Putting in a line of text\n')
fout.close()
fout = open('firstexample.txt', 'a')
fout.write('Putting in a line of text\n')
fout.close()
fout = open('firstexample.txt', 'a')
fout.write('Putting in a line of text\n')
fout.close()


fout = open('myfile.txt', 'w')
fout.write('My first line of text\n')
fout.write('My second line of text\n')
fout.write('My third line of text\n')
fout.write('My fourth line of text\n')
fout.close()


fin = open('myfile.txt', 'r')

for line in fin:
  print(line)
print()

fin.close()


fin = open('myfile.txt', 'r')

for line in fin:
  print(line, end="")
print()

fin.close()


fin = open('myfile.txt', 'r')

contents = fin.read()
print(contents)

fin.close()


fin = open('myfile.txt', 'r')
#the following statement will read all the lines from the fin file handler and return the lines as a list.
lines = fin.readlines()
print(lines[0], end="")
print(lines[1])

fin.close()


fin = open('myfile.txt', 'r')
#the following statement will read all the lines from the fin file handler and return the lines.
lines = fin.readlines()
for line in lines:
  print(line, end="")

fin.close()


fin = open('myfile.txt', 'r')

line1 = fin.readline();
print(line1, end="")
line2 = fin.readline();
print(line2, end="")
fin = open('myfile.txt', 'r')


names = ["Blue", "Python"]
fout = open('names.txt', 'w')
for m in names:
  fout.write(m + "\n")
fout.close()


names = []
fin = open('names.txt', 'r')
for line in fin:
  line = line.replace("\n", "")
  names.append(line)
print(names)


years = [1975, 1979, 1983]
fout = open('years.txt', 'w')
for year in years:
  fout.write(str(year) + "\n")
fout.close()


years = []
fin = open('years.txt', 'r')
for line in fin:
  line = line.replace("\n", "")
  years.append(int(line))
print(years)


import os
os.remove("years.txt")


fout = open('myfile.txt', 'w')
numchars = fout.write('My second line of text\n')
fout.close()
X = 23
Y = 'not enough chars were written'
Z = 'the right amount of chars were written'
if numchars < X:
  print(Y)
elif numchars >= X:
  print(Z)


fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
  count = count + 1
print("There were", count, "lines in", fname)


fname = input("Enter the file name: ")
try:
  fhand = open(fname)
except:
  print("File cannot be opened:", fname)
  exit()
count = 0
for line in fhand:
  count = count + 1
print("There were", count, "lines in", fname)


s = '1 2\t 3\n 4'
print(s)


s = '1 2\t 3\n 4'
print(repr(s))


#full salary program:
import csv
import sys

FILENAME = "employees.csv"

#exiting the program
def exit_program():
  print("Ending program")
  sys.exit()

#read the employees from the file
def read_employees():
  try:
    employees = []
    with open(FILENAME, newline="") as file:
      reader = csv.reader(file)
      for row in reader:
        employees.append(row)
    return employees
  except FileNotFoundError as error:
    print(f"Could not find {FILENAME} file")
    exit_program()
  except Exception as e:
    print(type(e), e)
    exit_program()
    
#write employees to file
def write_employees(employees):
  try:
    with open(FILENAME, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(employees)
  except Exception as e:
    print(type(e), e)
    exit_program()
    
#add employee to the list
def add_employee(employees):
  empid = input("Enter the employee ID: ")
  sal = input("Enter the employee's salary: ")
  employee = [empid,sal]
  employees.append(employee)
  write_employees(employees)
  print(f"Employee {empid}: {sal} was added\n")
  
#display list of employees
def list_employees(employees):
  for i, employee in enumerate(employees, start=1):
    print(f"{i} Employee ID: {employee[0]} (${employee[1]})")
  print()

#delete an employee based on ID
def delete_employee(employees):
    found = False
    number = input("Enter in the employee ID: ")
    for i, employee in enumerate(employees, start=0):
      if (employee[0] == number):
        print(f"Employee was deleted.\n")
        employee = employees.pop(i)
        found = True

    if (found == False):
      print("Employee was not found.\n")
    else:
      write_employees(employees)

def display_menu():
    print("The Employee Salary List program")
    print()
    print("LIST OF COMMANDS")
    print("list - List all employees")
    print("add -  Add an employee")
    print("del -  Delete an employee")
    print("exit - Exit program")
    print()    

display_menu()
employees = read_employees()
while True:    
    command = input("Command: ")
    if command.lower() == "list":
        list_employees(employees)
    elif command.lower() == "add":
        add_employee(employees)
    elif command.lower() == "del":
        delete_employee(employees)
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Salary Program")



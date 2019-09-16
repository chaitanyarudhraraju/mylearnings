#Module is set of data, def,class where things can be reused without calling functions
#   ex: libraries
#class a:
#    ..
# def A:
# ....
#var = <>

#Below lines are documentation for module.py
'''
this module contains following services
a) data : version,L
b) def : sayHello ,sayHi
c) class : Rectangle,Person,Employee
'''
version = 1.8
L = [10,20,30]
def sayHI():

    ''' this is documentation for sayHI...... '''
    return 'Hello.....'
def sayHello():
    return 'Hi.....'
class Rectangle:
    '''this is rectangle doc....'''
    count = 0
    def __init__(self, x, y):
        self.length = x
        self.breadth = y
        Rectangle.count = Rectangle.count+1
    def __str__(self):
        return 'Rectangle({0}, {1})'.format(self.length,self.breadth)
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length * self.breadth)
    def isSquare(self):
        return self.length == self.breadth
    def scale(self, a = 0 ,b = 0):
        if self.length + a > 0:
            self.length = self.length + a
        if self.breadth + b > 0:
            self.breadth = self.breadth + b

    def  __add__(self, other):
        t = Rectangle(self.length+other.length , self.breadth+other.breadth)
        print t

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth
    @classmethod
    def getcount(cls): #Every function should have one argument
        return Rectangle.count

class Person:
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return 'Person({0} , {1}, {2})'.format(self.fname,self.lname,self.email)

    def fullname(self):
        return self.fname + ' ' + self.lname

    def getemail(self):
        return self.email

class Employee(Person): #inherting Person class <base class> into Employee class
    def __init__(self,fname,lname,email,eid,salary):
        Person.__init__(self,fname,lname,email)
        self.eid = eid
        self.salary = salary

    def __str__(self):
        return 'Employee({0},{1},{2},{3})'.format(self.fname,self.lname,self.email,self.eid)

    def getsalary(self):
        return self.salary

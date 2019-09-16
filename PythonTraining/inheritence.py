
#__init__ is a class level instance ,which basically creates an object
#
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

p = Person('abc', 'xyz', 'abc@xyz.com')
print p #Person(abc , xyz, abc@xyz.com)
fn = p.fullname()
print 'my fullname is ',fn
emp = Employee('xyz', 'abc' , 'abc@abc.com', 12345, 10000)
print emp #  Person(xyz , abc, abc@abc.com) emp uses str in Person if not available in EMployee
fn = emp.fullname() #if function doesn't exist in child class  will be inherited from parent
print fn
sal = emp.getsalary()
print sal


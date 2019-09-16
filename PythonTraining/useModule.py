import module
print module.version
R = module.Rectangle(2,3)
print R
from module import version, Rectangle

print  version
R = Rectangle(2,4)
s = set([1,2,3])
print R
print s
print module.__doc__
print module.sayHI().__doc__
print module.Rectangle.__doc__
print dir(int)

#
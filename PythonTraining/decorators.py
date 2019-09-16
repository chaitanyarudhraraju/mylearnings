#decorators

def outer():
    state = 10
    def inner():
        return state
    return inner
inn = outer()
s = inn()
print s

def add10(f):
    def decor(*args):
        return f(*args) + 10
    return decor
@add10   #decorator name
def add(a,b):
    return a+b
s= add(2, 3)
print 'sum = ',s
print add.__name__

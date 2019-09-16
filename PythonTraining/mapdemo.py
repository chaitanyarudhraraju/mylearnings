#map map(fun, seq, se2)
add = lambda a,b: a+b
l1 = [1,2,3,8]
l2 = [2,3,4,5]
print map(add, l1, l2)

#reduce

r = reduce(add, l2)
print r

L = [1,2,3,4,5,6,7,8,9,10]
m = map(add, L[::2], L[1::2])
print m

#question
lst = [1,2,3,4,5]
i = [0,1,2,3]
addsq = lambda a: a**2
add = lambda a,b: a+b
print lst[-1::]
m = map(add, lst[0:-1], lst[1::])
print m
m1 = map(addsq, m)
print m1
r = reduce(add, m1)
print r
#print help(map)




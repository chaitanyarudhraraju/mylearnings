#lambda to represent any math expression as an object
add = lambda a,b : a + b
#add is a lambda obj
s = add(2,3)
print s
L = [10,20,14,34,24,50,60,70,40]
L1 = 'apple', 'hi' ,'orange'
length = lambda x: len(x)
l2 = sorted(L1, key=length)
L3 = [(1,2), (12,2), (10,5),(35,6)]
L4 = sorted(L3)

print L4
pos = lambda x: x[1]
L1 = sorted(L3,key=pos)
print L1
#sort list of tuples by sum of tuples

sumT = lambda x : x[0] + x[1]
print sorted(L3,key=sumT)


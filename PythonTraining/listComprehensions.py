#

l = [10,12,14,13,16,17,18,19,20]
l1 = [x for x in l if x%2 == 0]
print l1
ip = '10.20.30.40'
L = ip.split('.')
L  = [int(x)for x in L]

def testprime(m):
    if m < 2: return False
    i = 2
    while i < m:
        if m % i == 0: return False
        i = i +1
        return True
p = [x for x in range(1000) if testprime(x)]
print p

A = [[0 for x in range(5)] for j in range(5)] ###list of list comprehensions
print A
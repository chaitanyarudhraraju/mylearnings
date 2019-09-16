import time
def sequence(seed = 0):
    i = 0
    a = 1
    if seed == 1: i =-1;a= 2
    if seed == 2: i=0 ;a= 2
    while True:
        i = i + a
        yield i
seq = sequence()
#print type(seq)

for i in range(10):
    print next(seq)
    #time.sleep(1)

odd_gen = sequence(1)
for x in range(10):
    print next(odd_gen),
print '\n'
even_gen = sequence(2)
for x in range(10):
    print next(even_gen),

print
def prime_seq():
    i = 2
    while True:
        i= i+1
        flag = True
        for x in range(2, i):
            if (i % x) == 0:
                flag = False
                break
        if flag == True: yield i

pri_seq = prime_seq()
for x in range(10):
    print next(pri_seq),


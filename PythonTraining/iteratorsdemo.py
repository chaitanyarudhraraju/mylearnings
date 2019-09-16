#iterators
L = [10,20,30,40,50]
print type(L)
iL = iter(L)
print next(iL)
print next(iL)
for x in iL:
    print x
fin = open('temp2.txt', 'r')
print type(fin)
print next(fin) ,next(fin)
#next(fin)
fin.seek(0,0)
print "next: ",next(fin)
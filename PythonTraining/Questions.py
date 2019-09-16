#Script to compute a time it takes to fill square matrix of order n randomly with random values in the range 1 - 1000 with cli interface
import os
import sys
import random
import time
class timeCompute():
    def __init__(self, order):
        self.order = order
        self.matrix = [[0 for i in range(self.order)] for i in range(self.order)]
        self.lenMat = self.order * self.order
    def getTime(self):
        i = 0
        count = 0
        time1 = 0
        #tmp = open('temp6.txt','w')
        while True:
            self.row = random.randrange(0, self.order)
            self.col = random.randrange(0, self.order)
            x = random.randrange(1, 1000)
            if self.matrix[self.row][self.col] == 0:
                self.matrix[self.row][self.col] = x
                count+=1
                if count == self.lenMat:
                    time1 = time1 + time.time()
                    break
        return time1
        #os._exit(0)
if len(sys.argv) !=2:
    pass
    #print "Need only one integer"
num = int(sys.argv[1])
obj = timeCompute(num)
t1 = obj.getTime()
#print t1
os._exit(0)
fh = open('temp1.txt', 'w')
fh.write()
fh.close()



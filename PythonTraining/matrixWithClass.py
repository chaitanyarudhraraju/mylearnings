import sys
class Matrix:
    def __init__(self, myFile):
        self.myfile = myFile
        self.fh = open(self.myfile, 'r')
        self.rows = []
        self.cols = []
        self.lst = []
    def __str__(self):
        for line in self.fh.readlines():
            self.lst.append(line.split())
        self.fh.close()
        return str(self.lst)
    def __add__(self, other):
        self.fh1 = open(sys.argv[3], 'w')
        t = Matrix(self.fh1)
        self.lst = []
        [t.lst[x][y] for x in self.  ]


if len(sys.argv) != 4:
    print 'I need 3 files through CLI'
    sys.exit(1)
m1 = Matrix(sys.argv[1])
print m1
m2 = Matrix(sys.argv[2])
print m2

#m3 = m1 + m2
#m3.write(sys.argv[3])
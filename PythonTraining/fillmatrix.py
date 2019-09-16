import os, sys

if len(sys.argv)!= 2:
    print "I need one input"
    sys.exit(1)
pidList = []
child1 = os.fork()
#os.execvp('<application name>', ['<appliation name>', <arg1: file name>,<argus>])
if child1 == 0:
    pidList.append(os.getpid())
    print "Child1 started with pid:",os.getpid()
    os.execvp('python', ['python', 'fillmatrix.py', sys.argv[1]])

child2 = os.fork()
if child2 == 0:
    pidList.append(os.getpid())
    print "Child2 started with pid:",os.getpid()
    os.execvp('python', ['python', 'fillmatrix.py', sys.argv[1]])
child3 = os.fork()
if child3 == 0:
    pidList.append(os.getpid())
    print "Child3 started with pid:",os.getpid()
    os.execvp('python', ['python', 'fillmatrix.py', sys.argv[1]])
r = 1
while True:
    try:
        p = os.wait() #Return [pid,status]
        print 'Process',p[0],'complete',r
    except OSError:
        print "Game is over"
        #os._exit(0) #to exit main process
        break
    r= r+1
child4 = os.fork()
if child4 == 0:
    print "Child4 has started with pid {0}: ".format(os.getpid)
    tmp = 0
    pid = int()
    for child in pidList:
        fh = open('{0}.txt'.format(child), 'r')
        childMatrix = []
        for line in fh.readlines():
            line = line.strip('\n')
            childMatrix.extend(line.split(' '))
        fh.close()
        childLen = len(childMatrix)
        childUnique = len(set(childMatrix))
        dupPer = ((childLen - childUnique)/childLen)*100
        if dupPer > tmp:
            tmp = dupPer
            pid = child
        elif dupPer == tmp:
            pid = child
    print "Child with PID :{0} has more duplicates".format(pid)
os.wait()
os._exit(0)
















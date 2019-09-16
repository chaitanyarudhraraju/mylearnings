import threading
import time
import re,os,sys

class MyThread(threading.Thread):
    def __init__(self,tid, tname, ip):
        threading.Thread.__init__(self)
        self.tid = tid
        self.tname = tname
        self.ip = ip
    def run(self):
        ip = self.ip
        pat = re.compile(r'(\d) received')
        report = ("No Response","Partial Response","Alive")

        print "Started Thread --->",self.tname
        ip = '15.252.203.'+str(ip)
        channel= os.popen('ping -c 2 '+ip, 'r')
        print "Tesing...",ip,
        sys.stdout.flush()
        while True:
            line = channel.readline()
            if not line: break
            result = re.findall(pat,line)
            if result:
                print report[int(result[0])]

threadList = []
ipList = [x for x in range(25, 36)]
for x in range(10):
    tname = 'theard'+str(1)
    threadList.append(tname)

for thread in threadList:
    thread = MyThread(1, thread, ipList[threadList.index(thread)])

print time.ctime()
for t in threadList:
    t.start()

for t in threadList:
    t.join()
print time.ctime()


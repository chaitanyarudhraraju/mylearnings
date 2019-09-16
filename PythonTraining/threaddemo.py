import threading
import time

class MyThread(threading.Thread):
    def __init__(self,tid,tname):
        threading.Thread.__init__(self)
        self.tid = tid
        self.tname = tname
    def run(self):
        print "Started Thread --->",self.tname
        for i in range(10):
            print self.tname, " :: value of i:",i
            time.sleep(1)
t1=MyThread(1,'one')
t2=MyThread(2,'two')
t1.start()
t2.start()
t1.join()
t2.join()
print "Main thread existing"
import os,re,time,sys
pat = re.compile(r'(\d) received')
report = ("No Response","Partial Response","Alive")

print time.ctime()

for host in range(60,70):
    ip = '192.168.200.'+str(host)
    channel= os.popen('ping -n 2 '+ip,'r')
    print "Tesing...",ip,
    sys.stdout.flush()
    while True:
        line = channel.readline()
        if not line: break
        result = re.findall(pat,line)
        if result:
            print report[int(result[0])]
print time.ctime()





import socket
import os,sys


def testprime(m):
    if m<2: return False
    i = 2
    while i < m:
        if m%i == 0:
            return False
        i = i+1
    return True

def nextprime(m):
    while True:
        m = m+1
        if testprime(m):
            return m
lookup = {'1': testprime , '2': nextprime}
HOST = ''
PORT = 6000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
os.system("clear")
print "Server is up and ready...",
sys.stdout.flush()
while True:
    conn , addr = s.accept()
    print "\n connection established from",addr[0]
    sys.stdout.flush()
    child = os.fork()
    if child == 0:
        while True:
            data= conn.recv(1024)
            if data == 3: break
            li = data.split(':')
            result = lookup[li[0]](int(li[1]))
            conn.sendall(str(result))
        conn.close()
        print "\n connection closed by",addr[0],
        sys.stdout.flush()
        os._exit(0)
    conn.close()

import sys
import re
def ipFind(lines):
    result = []
    for line in lines:
        print re.findall(r'(?:\b(?:25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)', line)
    return result
fh = open(sys.argv[1], 'r')
lines = fh.readlines()
result = ipFind(lines)
fh.close()
print result
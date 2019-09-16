import re
s = 'hello 123 ok 17 and 654321 and 78654 done'
print re.findall(r'\b(?:\d{2})+\b',s)
ip = 'hi my ip address is 192.168.72.56 to no'
print re.findall(r'((?:25[0-5]\.|2[0-4]\d|\.|[1-9]\.|[1-9]\d\.|1\d{2}\.){3})', ip )
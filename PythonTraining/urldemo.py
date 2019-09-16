import urllib
import re
sock = urllib.urlopen("http://www.google.co.in/")
html = sock.read()
sock.close()
#print html
print type(html)
result = re.findall(r'https?://.*?/', html)
print result

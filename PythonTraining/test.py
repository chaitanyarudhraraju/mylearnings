import pdb
l = [0]*256
string = 'chaitanya'
for ch in list(string):
    l[ord(ch)] = l[ord(ch)]+1
string2 = 'chaitanyavarmachaitanyahaitcanyanyachaita'
i = 0
y = len(string)
count = 0
while i <= len(string2):
    l1 = [0]*256
    for j in list(string2)[i:y]:
        l1[ord(j)] = l1[ord(j)]+1
    if l1 == l: count += 1;# print string2[i:y]
    i += 1
    y += 1
    if y == len(string2): break

#Maximize the sum in Array
#cond1: delete number


#7.Given a string S, remove all the consecutive duplicates.
'''
#Input  : aaaaabbbbbb
#Output : ab

str1 = list('aabccba')
#print str1
i = 0
l2 = [str1[0]]
while i < len(str1):
    if str1[i] == l2[-1]: i += 1
    else:
        l2.append(str1[i])
        i = i+1
    if i == len(str1):
        break
print ''.join(l2)
'''
#Python code to print common characters of two Strings in alphabetical order
'''
Input :
string1 : geeks
string2 : forgeeks
Output : eegks
Explanation: The letters that are common between
the two strings are e(2 times), k(1 time) and
s(1 time).
Hence the lexicographical output is "eegks"


string1 = 'geeks'
string2 = 'forgeeks'


list1 = [0]*256
list2 = [0]*256
finalList = []
for val in list(string1):
    list1[ord(val)] = list1[ord(val)]+1
for val in list(string2):
    list2[ord(val)] = list2[ord(val)]+1
for x in range(len(list1)):
    if list1[x] and list2[x] > 0:
            if list1[x] > list2[x]: len1 = list2[x]
            elif list1[x] < list2[x]: len1 = list1[x]
            else: len1 = list1[x]
            finalList.extend([chr(x)]*len1)
print finalList

'''
#Leading zeros from the IP address
str1 = '0000000100.020.00.0000400'
str2 = []
for x in str1.split('.'):
    if len(x) == 1:
        str2.append(x)
    else:
        for i in list(x):
            if int(i) > 0:
                str2.append(x[list(x).index(i)::])
                break

print str2

print int('000200')
import re
#Regex in Python to put spaces between words starting with capital letters


str1 = 'BruceWayneIsBatman'
print re.findall(r'[A-Z][a-z]*',  str1)
str2 = 'A'
print str2.lower()

str = "geeks for geeks"
str = ' '*4 + str
print str


L = [1,2,3,4,5,6]
print  L[-2:] + L[0:-2]

import copy
L1 = copy.deepcopy(L)
#print L, L1
#L.append(7)
#print L, L1
L[2] = 9
print L, L1


L2 = L[:]
L2.append(10)
print L, L2



iter1 = iter(L2)
print next(iter1)

for i in L2:
    if next(iter1):
        print i,






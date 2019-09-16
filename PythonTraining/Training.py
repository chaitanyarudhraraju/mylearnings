import sys
import re



#Write a script to find whether a given no is even or odd
'''
num = input("Enter the number :")
if int(num) % 2 == 0:
    print('Entered number is even')
else:
    print("Entered number is odd")
'''
#write a script to find out the smallest integer out of 3 integers
'''
intList = [445, -1320, -154]
min = intList[0]
if intList[1] < min:
    min = intList[1]
    #print min
if intList[2] < min:
    min = intList[2]
    #print min
if intList[1] < intList[2]:
    min = intList[1]
print min

'''

#Write a script to count the number of even length words from a given string
'''
str1 = raw_input("Enter the string:")
strList = str1.split()
count = 0
for x in strList:
    if len(x)%2 == 0:
        count+=1
print "The number of even len words are :", count
'''

#Write a script to swap the first and last characters of each and every word from a given string
'''
myStr = 'hello world , my name is chaitanya'
print "Entered string is :", myStr
myStrList = myStr.split()
for word in myStrList:
    wordList = list(word)
    wordList[0], wordList[-1] = wordList[-1], wordList[0]
    print ''.join(wordList),
'''

#Write a script to remove all the duplicate words from a given string
'''
myStr = raw_input("Enter the string:")
myStrList = myStr.split()
print ' '.join(list(set(myStrList)))
'''

#Write a script to find the frequency occurence of each and every word in a string
'''
myStr = raw_input("Enter the string:")
myStrList = myStr.split()
myDict = {}
count = 0
for word in myStrList:
    if word in myDict.keys():
        myDict[word]+= 1
    else:
        myDict[word] = 1
print myDict
'''

#To test a give IP vaild is valid or not
'''
myIp = raw_input("Enter the IP:")
flag = True
myIpList = myIp.split('.')
if len(myIpList) == 4:
    for dig in myIpList:
        if dig.isdigit():
            if int(dig) > 0 and int(dig) < 256:
                flag = True
            else:
                flag = False
                break
        else:
            flag = False
            break

else:
    flag = False
if flag == True:
    print("Valid address")
else:
    print("Not a valid address")
'''

#Script to read n IP's from key board and classify them into classes valid and invalid.
'''
myIpListCount = input('Number of Ip to check:')
i = 0
myIpList = []
while i < int(myIpListCount):
    myIp = raw_input('Enter IP :')
    myIpList.append(myIp)
    i+=1
validAddress = 0
notvalidAddress = 0
for ip in myIpList:
    flag = True
    myIpList1 = ip.split('.')
    if len(myIpList1) == 4:
        for dig in myIpList1:
            if dig.isdigit():
                if int(dig) > 0 and int(dig) < 256:
                    flag = True
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    else:
        flag = False
    if flag == True:
        #print("Valid address")
        validAddress +=1
    else:
        #print("Not a valid address")
        notvalidAddress +=1
print "valid addresses : ", validAddress
print "not valid address : ",notvalidAddress
'''

#Write a script to read and display a matrix
'''
rows = input("Enter number of rows: ")
cols = input('Enter number of coloumns : ')
i = 0
matrixList = []
while i < int(rows):
    myList = raw_input("Enter {} elements  separated ".format(cols))
    matrixList.append(list(myList.split(',')))
    i+=1
for x in matrixList:
    for y in x:
        print y,
    print

'''

#Script to find sum of 2 matricies
''''
matrixDict = {}
matrixCount = input("Enter the matrix count : ")
for x in range(matrixCount):
    rows = input("Enter number of rows of matrix ->{}: ".format(x))
    cols = input('Enter number of coloumns of matrixc ->{} : '.format(x))
    list1 = []
    j = 0
    while j < int(rows):
        myList = raw_input("Enter {} elements  separated by ',' of matrix{} ".format(cols, x))
        list1.append(list(myList.split(',')))
        j+=1
    matrixDict[x] = list1
sumMatrix=list(matrixDict.items())
'''
#Write a function that should be able to take any no of IP's and classify
'''
1.valid
2.invalid
3.classA
3.classB
4.classC
5.classD

def getValidIp(myIpList):
    validAddress = 0
    notvalidAddress = 0
    validAddressList = []
    notvalidAddressList = []
    for ip in myIpList:
        flag = True
        myIpList1 = ip.split('.')
        if len(myIpList1) == 4:
            for dig in myIpList1:
                if dig.isdigit():
                    if int(dig) > 0 and int(dig) < 256:
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
        else:
            flag = False
        if flag == True:
            validAddressList.append(ip)
        else:
            notvalidAddressList.append(ip)
        return validAddressList
    print "valid ip list:",validAddressList

def getClass(myIpList1):
    classA = []
    classB = []
    classC = []
    classD = []
    for ip in myIpList1:
        if int(myIpList1[0]) >=1 and int(myIpList1[0]) < 127: classA.append(ip)
        elif int(myIpList1[0]) >=128 and int(myIpList1[0]) <196 : classB.append(ip)
        elif int(myIpList1[0]) >=196 and int(myIpList1[0]) <224 : classC.append(ip)
        elif int(myIpList1[0]) >=224 and int(myIpList1[0]) <240 : classD.append(ip)
        else:
            print "Ip is {} classE address".format(ip)
    print "classA : ",classA
    print "classB : ",classB
    print "classC : ",classC
    print "classD : ",classD
    return classA,classB,classC,classD

myIpListCount = input('Number of Ip to check:')
i=0
myIpList = []
while i < int(myIpListCount):
    myIp = raw_input('Enter IP :')
    myIpList.append(myIp)
    i+=1
validIp = getValidIp(myIpList)
classIp = getClass(validIp)

'''


#Script to find the sum of all the numbers available in a file with cli interface
'''
def sumOfList(l):
    mysum=0
    for x in l:
        mysum=mysum+int(x)
    return mysum

def sumOfNum(fh):
    resultList = []
    for line in fh.readlines():
        resultList.append(re.findall('\d+', line))
    mysum=0
    for lst in resultList:
       mysum = mysum + sumOfList(lst)
    return mysum
fh = open(sys.argv[1] , 'r')
mySum = sumOfNum(fh)
print mySum
fh.close()
'''
#Script  to extract all the words which contains atleast one vowel from a file with cli interface
'''
def vowelWord(fh):
    resultList = []
    for line in fh.readlines():
        resultList.extend(re.findall('\w*[aeiouAEIOU]\w*', line))
    return resultList
fh = open(sys.argv[1], 'r')
vowelList = vowelWord(fh)
print vowelList
fh.close()
'''

#Script to extract all capital letters words available in a file with cli interface
'''
def capWord(list1):
    resultList = []
    for line in list1:
        resultList.extend(re.findall(r'\b[A-Z]+\b', line))
    return resultList
fh = open(sys.argv[1] , 'r')
lines = fh.readlines()
result = capWord(lines)
print result
'''

#write a script to extract all even length numbers available in a file using cli interface
#Script to extract all the numbers between 1 and 255 inclusive from a file using cli interface
'''
def numbFind(lines):
    result = []
    for line in lines:
        result.extend(re.findall(r'\b[1-9]\b|\b[1-9]\d\b|\b1\d{2}\b|\b2[0-4]\d\b|\b25[0-5]\b', line))
    return result
fh = open(sys.argv[1], 'r')
lines = fh.readlines()
result = numbFind(lines)
print result
'''


#script to extract all valid IP addresses from a file using cli interface
'''
def numbFind(lines):
    result = []
    for line in lines:
        result.extend(re.findall(r'\b[1-9]|\b[1-9]\d|1\d{2}|2[0-4]\d|25[0-5].[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5].'
                                 r'[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5].[1-9]|[1-9]\d|\b1\d{2}\b|\b2[0-4]\d\b|\b25[0-5]\b', line))
    return result
fh = open(sys.argv[1], 'r')
lines = fh.readlines()
result = numbFind(lines)
print result
'''



#Script to split given file into n parts with cli interface

#Script to find the addition of 2 matrices using files  to 3 file as output with cli interface
'''
class Rectangle:
    count = 0
    def __init__(self, x, y):
        self.length = x
        self.breadth = y
        Rectangle.count = Rectangle.count+1
    def __str__(self):
        return 'Rectangle({0}, {1})'.format(self.length,self.breadth)
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length * self.breadth)
    def isSquare(self):
        return self.length == self.breadth
    def scale(self, a = 0 ,b = 0):
        if self.length + a > 0:
            self.length = self.length + a
        if self.breadth + b > 0:
            self.breadth = self.breadth + b
        '''
'''
        if self.length < a and self.breadth < b:
             self.length = a
             self.breadth = b
        elif self.length < a and self.breadth > b:
            self.length,self.breadth = a,b
        elif self.length > a and self.breadth < b:
            self.length,self.breadth = a,b
        elif self.length > a and self.breadth > b:
            self.length,self.breadth = a, b
        else:
            self.length,self.breadth = a, b
'
    def  __add__(self, other):
        t = Rectangle(self.length+other.length , self.breadth+other.breadth)
        print t

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth
    @classmethod
    def getcount(cls): #Every function should have one argument
        return Rectangle.count

#main app starts here
R1 = Rectangle(2, 3)
print R1
a = R1.area()
R2 = Rectangle(4,5)
print 'area = ',a
p = R1.perimeter()
print 'Perimeter = ',p
if R1.isSquare():
    print 'square'
else:
    print "not a square"

R4 = R1.scale(1,2)
print R4

R3 = R1 + R2
print R3


if R1 == R2:
    print 'same'
else:
    print "not same"
c = Rectangle.getcount()
print 'count = ',c

'''
#class to find valid Ip and class
'''
#1.
class IpAddress:
    validAddressList = []
    def __init__(self, ip):
        self.ip = ip
    def __str__(self):
        return self.ip

    def valid(self):
        self.validAddressList = []
        flag = True
        myIpList = self.ip.split('.')
        if len(myIpList) == 4:
            for dig in myIpList:
                if dig.isdigit():
                    if int(dig) > 0 and int(dig) < 256:
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
        else:
            flag = False
        if flag == True:
            self.validAddressList.append(self.ip)
            return True
        else:
            return False

    def getclass(self):
        if self.validAddressList:
            myIpList1 = self.validAddressList[0]
            for ip in myIpList1:
                if int(myIpList1[0]) >=1 and int(myIpList1[0]) < 127:
                    return 'class A'
                elif int(myIpList1[0]) >=128 and int(myIpList1[0]) <196 :
                    return 'class B'
                elif int(myIpList1[0]) >=196 and int(myIpList1[0]) <224 :
                    return 'class C'
                elif int(myIpList1[0]) >=224 and int(myIpList1[0]) <240 :
                    return 'class D'
                else:
                    return 'Class E'
        else:
            return False
    def __eq__(self,other):
        return self.ip == other.ip

ip1 = IpAddress('142a.2.3.4')
print ip1
if ip1.valid():
    print 'ValidIp'
else:
    print 'Invalid Ip'
gc = ip1.getclass()
print gc

ip2 = IpAddress('1.2.3.5')
if ip1 == ip2:
    print 'same'
else:
    print 'Not same'

'''
#Martix using class
'''
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


if len(sys.argv) != 4:
    print 'I need 3 files through CLI'
    sys.exit(1)
m1 = Matrix(sys.argv[1])
print m1
m2 = Matrix(sys.argv[2])
print m2

#m3 = m1 + m2
#m3.write(sys.argv[3])
'''




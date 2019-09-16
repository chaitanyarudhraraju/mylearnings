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
mylist = matrixDict.values()
summatrix = []
for x in zip(*mylist):
    innermatrix = []
    for y in zip(*x):
        innermatrix.append(sum([int(z) for z in y]))
    summatrix.append(innermatrix)
print summatrix






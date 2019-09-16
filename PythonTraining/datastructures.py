class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        newNode = Node(node.data)
        newNode.setNextNode(self.head)
        self.head = newNode

    def push(self, prev_node, node):
        print prev_node.getNextNode()
        newNode = Node(node)
        newNode.setNextNode(prev_node.getNextNode())
        print prev_node.getNextNode()
        prev_node.setNextNode(newNode)

    def delete(self, node):
        node = Node(node)

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.getNextNode()
        return count

    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next_node

class Node:
    def __init__(self, data=None, next_node=None ):
        self.data= data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.next_node

    def setNextNode(self,next_node):
        self.next_node = next_node
first = Node(1)
LL = LinkedList(first)
second = Node(2)
third = Node(3)
first.setNextNode(second)
print(LL.size())
print (LL.printList())
#print LL
LL.insert(third)
print (LL.printList())
four = Node(4)
LL.insert(four)
print (LL.printList())
LL.push(third, 5)
print (LL.printList())

L5 = [1,2,3]
L5.append(None)
print L5

i = '2'
in1 = '2'
if int(i) == int(in1):
    print True












'''
Singly Linked list and operations 
@auther : Saurabh P Sabnis 
'''

class sllNode:
    "single node of a Singly Liked List"
    def __init__(self,data=None, nextNode = None):
        self.data = data
        self.next = nextNode
        
    def setData(self,data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self,nextNode):
        self.next = nextNode
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return (self.next != None)
   
def printSll(node):
    while node:
        print node.getData(), " ",
        node = node.getNext()
    print

def reverseSll(node):
    if(not node):
        return None
    t1 = None
    t2 = node
    t3 = node.getNext()
    while (t2):
        t3 = t2.getNext()
        t2.setNext(t1)
        t1 = t2
        t2 = t3
    return t1

def insertByIndex(node,data,index):
    i =0 
    while i!= index-1:
        if(node.getNext == None):
            print "index out of range"
            return
        else:
            node = node.getNext()
        i +=1
    nextNode = node.getNext()
    tempNode = sllNode(data)
    tempNode.setNext(nextNode)
    node.setNext(tempNode)
    

ll = [45,78,11,23,61,89,32,6,112]
#Creating the SLL from the list
head = sllNode(ll[0])
t1 = head
for i in ll[1:]:
    sll = sllNode(i)
    t1.setNext(sll)
    t1 = sll
printSll(head)
# reversing the SLL
head = reverseSll(head)
printSll(head)

#reversing it back to original 
head = reverseSll(head)
    
#inserting an element in the middle 
insertByIndex(head, 34, 4)
printSll(head)
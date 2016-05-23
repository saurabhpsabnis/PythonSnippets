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
        print node.getData()
        node = node.getNext()
       
ll = [45,78,11,23,61,89,32,6,112]
#Creating the SLL from the list
head = sllNode(ll[0])
t1 = head
for i in ll[1:]:
    sll = sllNode(i)
    t1.setNext(sll)
    t1 = sll
printSll(head)

    
    

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data=None, next=None, prev=None): 
    self.data = data
    self.next = next
    self.prev = prev

# A Linked List class with a single head node and tail node
class LinkedList:
  def __init__(self):  
    self.head = None
    self.tail = None 
# insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
      current.next.prev = current
      self.tail = newNode
    else:
      self.head = newNode
#print method for the linked list
  def printLLReverse(self):
    current = self.tail
    while(current):
      print(current.data)
      current = current.prev
  def printLLForward(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
#LL.printLL()
#LL.reverse_LL()
#LL.printLL()
#LL.deletion(3)
LL.printLLForward()
LL.printLLReverse()

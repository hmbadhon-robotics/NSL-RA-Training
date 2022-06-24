# A deque implemented with 2way linkedlist

class Node:
#constructor
  def __init__(self, data=None, next=None, prev=None): 
    self.data = data
    self.next = next
    self.prev = prev

#A Linked List class with a single head node and tail node
class Deque:
  def __init__(self):  
    self.head = None
    self.tail = None 


#rear insert in Deque
  def rear_insert(self, data):
    newNode = Node(data)
    if(self.tail):
        current = self.tail
        current.next = newNode
        current.next.prev = current
        self.tail = newNode
    else:
        self.insert(data)
#front insert in Deque
  def front_insert(self, data):
    newNode = Node(data)
    if(self.head):
        current = self.head
        current.prev = newNode
        current.prev.next = current
        self.head = newNode
    else:
        self.insert(data)

##insert
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

  def rear_delete(self):
    if(self.tail):
        current = self.tail
        current.prev.next = None
        self.tail = current.prev
    else:
        print("create first node")
  def front_delete(self):
    if(self.head):
        current = self.head
        current.next.prev = None
        self.head = current.next
    else:
        print("create first node")

#print method for Deque
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


# Deque Operations
LL = Deque()
#LL.front_insert(200)
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.rear_insert(5)
LL.front_insert(6)
#LL.printLL()
#LL.reverse_LL()
#LL.printLL()
#LL.deletion(3)
LL.printLLForward()

LL.rear_delete()
LL.front_delete()
LL.printLLForward()

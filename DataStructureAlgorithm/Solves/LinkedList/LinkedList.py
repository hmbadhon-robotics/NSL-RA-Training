# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

  def reverse_LL(self):
    current = self.head
    prev = None 

    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev

  def deletion(self, val):
    current = self.head
    prev = None
    curr = None
    while(current.data! = val):
        prev = current
        curr = current.next
        current = current.next
    prev.next = current.next











# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
#LL.printLL()
#LL.reverse_LL()
#LL.printLL()
LL.deletion(3)
LL.printLL()




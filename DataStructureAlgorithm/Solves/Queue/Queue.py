class Queue:
    def __init__(self, Size):
        self.size = Size
        self.head = 0
        self.tail = -1
        self.queue = [None for i in range(self.size)]
    def push(self, value):
        self.tail = self.tail +1
        self.queue[self.tail] = value
    def pop(self):
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = self.head +1
        if(self.head > self.tail and self.head!=0 and self.tail!=-1):
            self.head=0
            self.tail=-1
        return value
    def show_queue(self):
        print(self.queue)
    def print_pointer(self):
        print("HEAD:",self.head)
        print("TAIL:",self.tail)

my_queue = Queue(10)


my_queue.print_pointer()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.push(4)
my_queue.push(5)
print(my_queue.show_queue())
my_queue.pop()
my_queue.pop()
my_queue.pop()
my_queue.pop()
my_queue.pop()
print(my_queue.show_queue())
my_queue.print_pointer()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
print(my_queue.show_queue())
my_queue.print_pointer()
my_queue.pop()
my_queue.pop()
print(my_queue.show_queue())
my_queue.print_pointer()




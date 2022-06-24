# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:
    def __init__(self,Size):
        self.top = -1
        self.stack = [None]*Size
    def push(self,value):
        self.top = self.top + 1
        #print("Push Pointer",self.top)
        self.stack[self.top] = value


    def pop(self):
        pop_value = self.stack[self.top]
        self.stack[self.top] = None
        self.top = self.top - 1
        if(self.top<-1):
           self.top = -1

        #print("pop pointer",self.top)
        return pop_value
    
    def peek(self):
        peek_value = self.stack[self.top]
        return peek_value


    def empty(self):
        if(self.top == -1):
            return False
        else:
            return True
    def print_Stack(self):
        print(self.stack)


class Queue():
    def __init__(self,size):
        self.size = size
        self.stack_1 = Stack(size)
        self.stack_2 = Stack(size)
        
        
    def push_queue(self,value):
        while(self.stack_1.empty()):
            self.stack_2.push(self.stack_1.pop())
            #print("hello")                
        self.stack_1.push(value)
        #self.stack_1.print_Stack()
        #self.stack_1.print_Stack()
        while(self.stack_2.empty()):
            self.stack_1.push(self.stack_2.pop())
        # print("in push queue")
        # self.stack_1.print_Stack()
        # self.stack_1.print_Stack()
    def pop_queue(self):
        x = self.stack_1.pop()
        # print("in pop queue")
        # self.stack_1.print_Stack()
        # self.stack_1.print_Stack()
        #return x
        
    def print_front(self):
        x = self.stack_1.peek()
        # print("in print front queue")
        # self.stack_1.print_Stack()
        # self.stack_1.print_Stack()
        return x    
# Driver code
if __name__ == '__main__':       
    n = int(input())
    my_queue = Queue(n)


    for i in range(n):
        val = input().split()
        #print(val[0],val[1])
        if(int(val[0])==1):
            my_queue.push_queue(int(val[1]))
        elif(int(val[0])==2):
            my_queue.pop_queue()
        elif(int(val[0])==3):
            print(my_queue.print_front())
        
    
class Stack:
    def __init__(self,Size):
        self.top = -1
        self.stack = [None for i in range(Size)]



    def push(self,value):
        self.top = self.top + 1
        print("Push Pointer",self.top)
        self.stack[self.top] = value


    def pop(self):
        pop_value = self.stack[self.top]
        self.top = self.top - 1
        if(self.top<-1):
           self.top = -1

        print("pop pointer",self.top)
        return pop_value


    def peek(self):
        peek_value = self.stack[self.top]
        return peek_value


    def empty(self):
        if(self.top == -1):
            return True
        else:
            return False
    def print_Stack(self):
        print(self.stack)

stack_1 = Stack(5)
stack_1.push(1)
stack_1.pop()
stack_1.pop()
stack_1.pop()

print(stack_1.peek())

stack_1.push(2)



print(stack_1.peek())

stack_1.push(3)
print(stack_1.peek())
stack_1.push(4)
print(stack_1.peek())
stack_1.push(5)
print(stack_1.peek())
stack_1.pop()
print(stack_1.peek())

stack_1.print_Stack()
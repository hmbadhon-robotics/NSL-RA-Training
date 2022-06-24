#!/bin/python3

import math
import os
import random
import re
import sys

class Stack:
    def __init__(self,Size):
        self.top = -1
        self.stack = [None for i in range(Size)]
        
    def push(self,value):
        self.top = self.top + 1
        #print("Push Pointer",self.top)
        self.stack[self.top] = value


    def pop(self):
        pop_value = self.stack[self.top]
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
            return True
        else:
            return False
    def print_Stack(self):
        print(self.stack)


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING expression as parameter.
#

def isBalanced(expression):
    # Write your code here
    #print(type(expression))
    list_of_string = list(expression)
    print(list_of_string)
    my_stack = Stack(len(expression))

    for bracket in list_of_string:
        if(bracket =='{' or bracket =="(" or bracket=="["):
            my_stack.push(bracket)
        else:
            if(bracket == ")" and my_stack.peek() == "(" ):
                x = my_stack.pop()
            elif(bracket == "}" and my_stack.peek() == "{" ):
                x = my_stack.pop()
            elif(bracket == "]" and my_stack.peek() == "[" ):
                x = my_stack.pop()
            else:
                my_stack.push(bracket)
    if(my_stack.empty()):
        return "YES"
    else:
        return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        expression = input()

        res = isBalanced(expression)

        fptr.write(res + '\n')

    fptr.close()

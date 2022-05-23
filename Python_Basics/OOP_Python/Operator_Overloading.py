#Overloading with MAGIC METHODS
import re


class MyNum:
    def __init__(self,value) -> None:
        self.value = value

##ADDING
    def __add__(self,other):
        return (self.value)+(other.value)
## INPLACE ADDING
    def __iadd__(self,other):
        self.value = (self.value) + (other.value)
        return self.value


a = MyNum(2)

b = MyNum(3)

c = a + b

print(c)

a += b

print(a)
        
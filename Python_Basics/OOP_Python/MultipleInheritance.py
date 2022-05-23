#Base classes
class A:
    def spam(self):
        print(1)
class B:
    def spam(self):
        print(2)

##multiple inheritance
class C(A,B):
    def spam(self):
        print(3)

c_object = C()

A().spam()
B().spam()
C().spam()


c_object.spam()


def my_decorator(func):
    def decorate():
        print("Startind Decorator")
        func()
        print("End Decorator")
    return decorate



def show():
    print("Hello_Inside_Main_Function")

    
@my_decorator
def show1():
    print("Hello_Inside_Main_Function1")

decorated_func = my_decorator(show)
decorated_func()

show1()
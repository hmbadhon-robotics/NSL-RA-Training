##Multiple Parameter Handling


def make_sum(*args):

    ##*args take parameter as tuple
    sum = 0
    for num in args:
        sum += num
    return sum

print(make_sum(10,20,30,40))


## Named Multiple Parameter Handling
def print_dict(**kwargs):
    ##** takes parameter as dictionary
    sum = 0
    for i in kwargs:
        print("{0} : {1}".format( i , kwargs[i]))
        sum += kwargs[i]
    return sum
print_dict(a = 11,b = 23)


##Mixed Parameter 
def print_all(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

print_all(10, 20, 30, 50, b=5, c=10)
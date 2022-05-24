def my_function(func, arg):
    return func(arg)
print(my_function(lambda x: 2 * x, 5))

##difference between lambda and function
def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
 
# using the normally
# defined function
print(cube(5))
 
# using the lambda function
print(lambda_cube(5))


##lambda with if-else

max = lambda a, b : a if (a>b) else b
print(max(12,42))



##Lambda with list comprehension

def mul_ten(x):
    return x*10

mul_ten_lambda = lambda x : x*10

tables = [ lambda x=x: x*10 for x in range(1, 11)]

print(tables)
 
for table in tables:
    print(table())



##Mixed lambda with list comprehension and if-else
def mul_ten(x):
    return x*10

mul_ten_lambda = lambda x : x*10

tables = [ lambda x=x, y=x: x*10 if(x*10<50) else x+y for x in range(1, 11)]

print(tables)
 
for table in tables:
    print(table())



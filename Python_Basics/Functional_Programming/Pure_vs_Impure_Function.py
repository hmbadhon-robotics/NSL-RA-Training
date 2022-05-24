
##pure function that takes inpput,process it and gives an output
def pure(a,b):
    return a+b


#impure function holds the values inside the function
listo = []
def impure(val):
    listo.append(val)


print(pure(1,2))

impure(2)

print(listo)


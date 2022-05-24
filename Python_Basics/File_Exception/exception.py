try:
    variable = 10
    #print(variable+"hello")
    print(variable/10)
##handling ZeroDivision error
except ZeroDivisionError:
    print("Divided By Zero Error.")
## handl;ing value/typerror
except(ValueError,TypeError):
    print("Type or Value error occurred.")
##Other error
except:
    print("Othher Error occurred.")
##finally runs code though the exceptions occured.
finally:
    print("Solve the error but the code is running")



## raise keyword use

try:
    num = 5 / 5
except:
    print("custom message about error!")
    raise




## ASSERTION
##used to handle data sanity or it is valid or not
def Summing(val):
    assert (val<0),"Value Less Than 0"
    val = (val*val)
    #
    assert (val>=100),"Value Greater Than 100"
    return val

print(Summing(-2))
print(Summing(5))
print(Summing(10))
import numpy as np

a = np.array([1, 2, 3 ,4])
print(type(a))
print(a.dtype)
print(a)
a = np.array([1, 2, 3, 4, 5],dtype = 'float32')
print(a.dtype)

#access numpy array
print(a[0],a[1],a[-1])
print(a)

#2d array

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
print(b.shape)
print(b.shape[0])
print(b.shape[1])
#print(b[1,1])
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        print(b[i,j])

c= np.ones((3,4))
d = np.ones(10)


print(c)
print(d)

#Indentity matrix,random matrix
d = np.eye(4)
print(d)
e = np.random.random((2,2))
print(e)


#Array Indexing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
b = a[:2, 1:3]
print(b)

#numpy masking
a = np.array([[1, 2], [3, 4], [5, 6]])

bool_idx = (a > 2)

print(bool_idx)
print ('using bool index:', a[bool_idx])
print ('direct:', a[a > 2])


##numpy operations
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Element wise sum; both produce this array
# "[[6.0 8.0]
#  [10.0 12.0]]"
print(x + y)
print(np.add(x, y))

# Element wise subtraction
# "[[-4.0 -4.0]
#  [-4.0 -4.0]]"
print(x - y)
print(np.subtract(x, y))

# Element wise multiplication
# "[[  5.  12.]
#  [ 21.  32.]]"
print(x * y)
print (np.multiply(x, y))

# Element wise division
# "[[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]"
print (x / y)
print (np.divide(x, y))

# Element wise Square root 
# "[[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]"
print(np.sqrt(x))

# numpy reshape
import numpy as np

a = np.arange(12)

b = a.reshape(3, 4)

print(b)
out = np.array([[[1., 2.],
        [3., 4.],
        [5., 6.]],

       [[7., 8.],
        [9., 10.],
        [11., 12.]],

       [[13., 14.],
        [15., 16.],
        [17., 18.]],

       [[19., 20.],
        [21., 22.],
        [23., 24.]]])


print(out)
print(out.shape)
print("3d print i,j,k")
for i in range(out.shape[0]):
    for j in range(out.shape[1]):
        for k in range(out.shape[2]):
            print(out[i,j,k])


print("3d print i,j")
for i in range(out.shape[0]):
    for j in range(out.shape[1]):
        print(out[i,j])
        print("fin")


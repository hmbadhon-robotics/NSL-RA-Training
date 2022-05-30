"""
numpy stanford course
"""
import numpy as np

if __name__ == "__main__":

    v = np.array([1, 2, 3])
    w = np.array([4, 5])
    print(np.reshape(v, (3, 1)) * w)
    x = np.array([[1, 2, 3], [4, 5, 6]])
    print(x+v)
    print((x.T +w).T)
    print(x + np.reshape(w, (2, 1)))
    print(x*2)
    ##Scipy

    a_3d_array = np.zeros((2, 3, 4))
    print(a_3d_array)

    ar = np.zeros((12, 12, 3))
    print(ar)
    print(ar)
    for i in range(ar.shape[0]):
        for j in range(ar.shape[1]):
            print(ar[i, j])
    




    ####Array Indexing
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    print(a)
    print(a.shape)
    ##Access index with slicing

    print(a[:2, 1:3])
    print(a[0, 1])   # Prints "2"
    a[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
    print(a[0, 1])   # Prints "77"

    print(np.arange(4))

    a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

    print(a) 

    # Create an array of indices
    b = np.array([0, 2, 0, 1])

    # Select one element from each row of a using the indices in b
    print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"
    ##accessing index (0, 0), (1, 2), (2, 0) ,(3, 1)
    # Mutate one element from each row of a using the indices in b
    




    ##Boolean Indexing
    a[np.arange(4), b] += 10
    print(a)
    limit = (a>2) & (a<10)
    print(a[limit])



    ####Datatypes

    x = np.array([1, 2])   # Let numpy choose the datatype
    print(x.dtype)         # Prints "int64"

    x = np.array([1.0, 2.0])   # Let numpy choose the datatype
    print(x.dtype)             # Prints "float64"

    x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
    print(x.dtype) 


    ###Numpy Math
    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print(x + y)
    print(np.add(x, y))

    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print(x - y)
    print(np.subtract(x, y))

    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print(x * y)
    print(np.multiply(x, y))

    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print(x / y)
    print(np.divide(x, y))

    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print(np.sqrt(x))


    import numpy as np

    x = np.array([[1, 2],[3, 4]])
    y = np.array([[5, 6],[7, 8]])

    v = np.array([1, 2])
    w = np.array([3, 4])

    print("Inner product of vectors; Element wise multiplication and sum")
    print(v.dot(w))
    print(np.dot(v, w))

    print("Matrix / vector product; both produce the rank 1 array")
    print(x.dot(v))
    print(np.dot(x, v))

    print(x.dot(y))
    print(np.dot(x, y))

    #print matrix multiplication
    print(np.matmul(x,y))
    print(np.cross(x, y))


    # Vectors
    a = np.array([2, 6])
    b = np.array([3, 10])
    print("Vectors :")
    print("a = ", a)
    print("\nb = ", b)

    # Inner Product of Vectors
    print("\nInner product of vectors a and b =")
    print(np.inner(a, b))

    print("---------------------------------------")

    # Matrices
    x = np.random.rand(3,4)
    y = np.random.rand(2,4)
    print("\nMatrices :")
    print("x =", x)
    print("\ny =", y)

    # Inner product of matrices
    print("\nInner product of matrices x and y =")
    print(np.inner(x, y))
    # Vectors
    a = np.array([2, 6])
    b = np.array([3, 10])
    print("Vectors :")
    print("a = ", a)
    print("\nb = ", b)
    
    # Outer product of vectors 
    print("\nOuter product of vectors a and b =")
    print(np.outer(a, b))
    
    print("------------------------------------")
    
    # Matrices
    x = np.array([[3, 6, 4], [9, 4, 6]])
    y = np.array([[1, 15, 7], [3, 10, 8]])
    print("\nMatrices :")
    print("x =", x)
    print("\ny =", y)
    
    # Outer product of matrices
    print("\nOuter product of matrices x and y =")
    print(np.outer(x, y))


    ##BroadCasting
    import numpy as np

    # We will add the vector v to each row of the matrix x,
    # storing the result in the matrix y
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1 , 1])
    v= np.reshape(v, (4,1))
    y = x + v  # Add v to each row of x using broadcasting
    print(y)  # Prints "[[ 2  2  4]
            #          [ 5  5  7]
            #          [ 8  8 10]
            #          [11 11 13]]"



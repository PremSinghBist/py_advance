import numpy as np 

A  = np.array([ [1, 2, 3], [3, 4, 5] ])
B  = np.array([ [1, 2] , [4, 5] ,  [5, 6] ])
print(A.shape)
print(B.shape)
C = np.zeros((A.shape[0], B.shape[1])  )
print("Shape of C {}".format(C.shape))

#matri multiplication
for i in range(A.shape[0]):
    for k in range(B.shape[1]):
        for j in range(A.shape[1]):
            C[i][k]  += A[i][j] * B[j][k]
print("Shape of C: ", C.shape)
print(C)
            

import numpy as np 
A  = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B  = np.array([[1, 2 ], [4, 5], [7, 8]])
#A  = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def mat_mul_using_numpy():
    print(A.shape)
    mult = np.dot(A, A)
    print(mult.shape)
    print(mult)
    
def mat_mut_core_python():
    result = np.zeros( (A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(B.shape[1]):
            assert A.shape[1] == B.shape[0], "These matrices cannot be dot producted"
            for j in  range(A.shape[1]):
                result[i][k] += A[i][j] * B[j][k]  
    print(result)
            
print(np.einsum("ij,jk->ij",A,B)) 

    

mat_mul_using_numpy()
print("Multiplication using core logic")
mat_mut_core_python()
from numpy import *

'''
#Sqaure matrix multiplication

def matrixmult(n, mat1, mat2):
    temp_matrix = [[0 for i in range(n)] for j in range(n)]
    temp_matrix = array(temp_matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp_matrix[i][j] += mat1[i][k] * mat2[k][j]
    return temp_matrix

print("----- Square Matrix Multplication -----")
m1 = [[1,1],[2,2]]
m1 = array(m1)
m2 = [[2,2],[3,3]]
m2 = array(m2)
result = matrixmult(2, m1, m2)
print(f'Matrix 1: \n{m1}')
print(f'Matrix 2: \n{m2}')
print(f'After Multiplication: \n{result}\n')
'''

#Strassen Algorithm (Matrix multiplication)
def strassen (n, A, B, C):
    threshold = 2
    A11 = array([[A[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
    A12 = array([[A[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2))])
    A21 = array([[A[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), n)])
    A22 = array([[A[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2), n)])

    B11 = array([[B[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
    B12 = array([[B[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2))])
    B21 = array([[B[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), n)])
    B22 = array([[B[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2), n)])

    #print(A11, A12, A21, A22, B11, B12, B21, B22)
    if (n <= threshold):
        C = array(A) @ array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = array([])
        M1 = strassen(int(n/2), (A11 + A22), (B11 + B22), M1)
        M2 = strassen(int(n/2), (A21 + A22), B11, M2)
        M3 = strassen(int(n/2), A11, (B12 - B22), M3)
        M4 = strassen(int(n/2), A22, (B21 - B11), M4)
        M5 = strassen(int(n/2), (A11 + A12), B22, M5)
        M6 = strassen(int(n/2), (A21 - A11), (B11 + B12), M6)
        M7 = strassen(int(n/2), (A12 - A22), (B21 + B22), M7)

        C = vstack([hstack([M1 + M4 - M5 + M7, M3 + M5]), hstack([M2 + M4, M1 + M3 - M2 + M6])])
    return C
    


n = 4
#A = [[1 for cols in range(n)] for rows in range(n)]
#B = [[2 for cols in range(n)] for rows in range(n)]
A = [ [1,2,0,2], [3,1,0,0], [0,1,1,2], [2,0,2,0] ]
B = [ [0,3,0,2], [1,1,4,0], [1,1,0,2], [0,5,2,0] ]
C = array(A) @ array(B)
D = [[0 for cols in range(n)] for rows in range(n)]
print(f'Anticipated Result: \n{C}\n')
D = strassen(n, A, B, D)
print(f'After Strassen: \n{D}\n')












#Matrix
'''
1. 행렬의 합
2. 행렬의 곱
3. 전체 행렬
'''

A = [[1,2,3], [4,5,6]]       # 2 x 3
B = [[5,2,3], [1,3,1]]       # 2 x 3
C = [[1,2], [3,4], [5,6]]    # 3 x 2
hap = [[0,0,0], [0,0,0]]
mul = [[0,0], [0,0]]
transpose = [[0,0],[0,0],[0,0]]
#1.
for i in range(len(A)):
    for j in range(len(A[0])):
        hap[i][j] = A[i][j] + B[i][j]
print(hap)


#2.
for i in range(len(A)):
    for j in range(len(C[0])):
        for k in range(len(A[0])):
            mul[i][j] += A[i][k] * C[k][j]
print(mul)


#3.
for i in range(len(A[0])): # 0 1 2
    for j in range(len(A)): # 0 1
        transpose[i][j] = A[j][i]

print(transpose)
            
                   

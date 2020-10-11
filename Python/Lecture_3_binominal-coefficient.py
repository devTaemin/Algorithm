# 이항계수 알고리즘: 분할 정복식 접근 방법
from numpy import *

def bin(n,k):
    if (k == 0 or n == k):
        return 1
    else:
        return bin(n-1, k-1) + bin(n-1, k)

# 이항계수 알고리즘: 동적 계획법 접근 방법
def bin2(n,k):
    B = array([[0 for rows in range(k+1)] for cols in range(n+1)])
    for i in range(0, n+1):
        limit = min(i,k)
        for j in range(0, limit + 1):
            if (j == 0 or j == i):
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j] + B[i-1][j-1]
    return B[n][k]


        
    


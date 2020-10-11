#최소 연쇄 행렬 곱셈: 동적 계획 알고리즘
import Lecture_3_utility as utility #제출 전 수정요망

def order(p,i,j):
    if (i == j):
        print("A" + str(i), end = "")
    else:
        k = p[i][j]
        print("(", end = "")
        order(p,i,k)
        order(p,k+1,j)
        print(")", end = "")


d = [5,2,3,4,6,7,8]
n = len(d) - 1

m = [[0 for j in range(1, n+2)] for i in range(1, n+2)]
p = [[0 for j in range(1, n+2)] for i in range(1, n+2)]


for diagonal in range(1, n):   #대각선 1,2,3,4,5
    limit = (n - diagonal + 1) #i는 n-diagonal 까지
    for i in range(1, limit):
        j = i + diagonal       #j는 i + diagonal
        
        result = 0
        for k in range(i, j): #k는 i부터 j-1까지
            if (k == i):
                result = m[i][k] + m[k+1][j] + (d[i-1] * d[k] * d[j])
                p[i][j] = k
            else:
                temp = m[i][k] + m[k+1][j] + (d[i-1] * d[k] * d[j])
                if (temp < result):
                    result = temp
                    p[i][j] = k

        m[i][j] = result
            
        
    

utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6)

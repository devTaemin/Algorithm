#최단 경로 찾기 알고리즘: Floyd2
import numpy as np

def allShortestPath(g,n):
    #node number은 1부터 n까지
    P = np.array([[-1 for rows in range(n)] for cols in range(n)])
    W = g
    D = W[:]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (D[i][k] + D[k][j] < D[i][j]):
                    P[i][j] = k
                    D[i][j] = D[i][k] + D[k][j]
    return D, P


    
def printMatrix(Matrix):
    n = len(Matrix[0])
    for i in range(0,n):
        for j in range(0,n):
            print(Matrix[i][j], end = " ")
        print()


def printP(Matrix):
    n = len(Matrix[0])
    for i in range(0,n):
        for j in range(0,n):
            print(Matrix[i][j] + 1, end = " ")
        print()


def _path(q,r):
    if(p[q][r] != -1):
        _path(q, p[q][r])
        print("v", p[q][r] + 1)
        _path(p[q][r], r)


def path(q,r):
    print("v %d"% q)
    _path(q-1, r-1)
    print("v %d"% r)


inf = 1000
g = [[0,1,inf,1,5],
     [9,0,3,2,inf],
     [inf,inf,0,4,inf],
     [inf,inf,2,0,3],
     [3,inf,inf,inf,0]]

d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printP(p)
print()
path(5,3)

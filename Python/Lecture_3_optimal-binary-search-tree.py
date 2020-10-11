#최적 이진 검색 트리: 동적 계획 알고리즘
import Lecture_3_utility as utility

class Node:
    def __init__(self,data):
        self.l_child = None
        self.r_child = None
        self.data = data

def tree(key,r,i,j):
    k=r[i][j]
    if (k == 0):
        return
    else:
        p=Node(key[k])
        p.l_child = tree(key,r,i,k-1)
        p.r_child = tree(key,r,k+1,j)
        return p


key = [" ", "A", "B", "C", "D", "E"]
p = [0, 5/15, 4/15, 3/15, 2/15, 1/15]
#확인용
#key = [" ", "A", "B", "C", "D"]
#p = [0, 0.375, 0.375, 0.125, 0.125]
n = len(p) - 1 # n = 5

a = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]


for i in range(1, n+1):   #n=5 이므로, i = 1,2,3,4,5
    a[i][i-1] = 0
    a[i][i] = p[i]
    r[i][i] = i
    r[i][i-1] = 0
a[n+1][n] = 0   #a[6][5] = 0
r[n+1][n] = 0   #r[6][5] = 0



for diagonal in range(1, n):
    limit = (n - diagonal + 1)
    for i in range(1, limit):
        j = i + diagonal
        result = 0
        for k in range(i, j+1):
            if (k == i):
                result = a[i][k-1] + a[k+1][j]
                r[i][j] = k
            else:
                temp = a[i][k-1] + a[k+1][j]
                if (temp < result):
                    result = temp
                    r[i][j] = k
        for add_p in range(i,j+1):
            result = result + p[add_p]
        a[i][j] = result
                       



utility.printMatrixF(a)
print()
utility.printMatrix(r)

root = tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)

#--------------------------------UTILITY-----------------------------------
#print matrix
def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j], end=" ")
        print()


#print float matrix
def printMatrixF(d):
    n = len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print("%5.2f" % d[i][j], end=" ")
        print()


#print matrix inorder
def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)


#print matrix preorder
def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)


#print matrix postorder
def print_postOrder(root):
    if not root:
        return
    print_postOrder(root.l_child)
    print_postOrder(root.r_child)
    print(root.data)

#---------------------------Min-matrix-chain-multiplication-----------------------------------

def order(p,i,j):
    if (i == j):
        print("A" + str(i), end = "")
    else:
        k = p[i][j]
        print("(", end = "")
        order(p,i,k)
        order(p,k+1,j)
        print(")", end = "")


d_1 = [5,2,3,4,6,7,8]
n_1 = len(d_1) - 1

m_1 = [[0 for j in range(1, n_1+2)] for i in range(1, n_1+2)]
p_1 = [[0 for j in range(1, n_1+2)] for i in range(1, n_1+2)]


for diagonal in range(1, n_1):   #대각선 1,2,3,4,5
    limit = (n_1 - diagonal + 1) #i는 n-diagonal 까지
    for i in range(1, limit):
        j = i + diagonal       #j는 i + diagonal
        
        result = 0
        for k in range(i, j): #k는 i부터 j-1까지
            if (k == i):
                result = m_1[i][k] + m_1[k+1][j] + (d_1[i-1] * d_1[k] * d_1[j])
                p_1[i][j] = k
            else:
                temp = m_1[i][k] + m_1[k+1][j] + (d_1[i-1] * d_1[k] * d_1[j])
                if (temp < result):
                    result = temp
                    p_1[i][j] = k

        m_1[i][j] = result
            
        
    

#utility.printMatrix(m_1)
printMatrix(m_1)
print()
#utility.printMatrix(p_1)
printMatrix(p_1)
order(p_1,1,6)


#---------------------------Optimal-binary-search-tree-----------------------------------
print()

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
p_2 = [0, 5/15, 4/15, 3/15, 2/15, 1/15]
#확인용
#key = [" ", "A", "B", "C", "D"]
#p_2 = [0, 0.375, 0.375, 0.125, 0.125]
n_2 = len(p_2) - 1 # n = 5

a = [[0 for j in range(0, n_2+2)] for i in range(0, n_2+2)]
r = [[0 for j in range(0, n_2+2)] for i in range(0, n_2+2)]


for i in range(1, n_2+1):   #n=5 이므로, i = 1,2,3,4,5
    a[i][i-1] = 0
    a[i][i] = p_2[i]
    r[i][i] = i
    r[i][i-1] = 0
a[n_2+1][n_2] = 0   #a[6][5] = 0
r[n_2+1][n_2] = 0   #r[6][5] = 0



for diagonal in range(1, n_2):
    limit = (n_2 - diagonal + 1)
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
            result = result + p_2[add_p]
        a[i][j] = result
                       


print()
#utility.printMatrixF(a)
printMatrixF(a)
print()
#utility.printMatrix(r)
printMatrix(r)

root = tree(key,r,1,n_2)
#utility.print_inOrder(root)
print_inOrder(root)
print()
#utility.print_preOrder(root)
print_preOrder(root)












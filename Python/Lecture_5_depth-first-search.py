#print matrix
def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j], end=" ")
        print()

#깊이 우선 검색
e = {0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6], 4:[6,7]}
n = 8
a = [ [0 for j in range(0,n)] for i in range (0,n) ]
for i in range(0,n-1):
    for j in range(i+1, n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1

printMatrix(a)

visited = n * [0]

def DFS(a,v):
    #a에서 시작해서 방문 찍기
    #a에서 연결된 것 중 가장 작은 것부터 visited검사
    #visited가 아니면 작은 것 부터 해당 노드로 방문
    #모두 visted이면 backtracking해서

    visited[v] = 1 #방문 체크
    print(v)
    for i in range(v,n):
        if (a[v][i] == 1 and visited[i] == 0):
            DFS(a,i)
    for j in range(v,n):
        if (a[v][j] == 1 and visited[j] == 0):
            DFS(a,j)





        

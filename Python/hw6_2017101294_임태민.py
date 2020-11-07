#-----------------------------------------------------------------------------
#Q1.
import queue
#print matrix
def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j], end=" ")
        print()

#너비 우선 검색
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

def BFS(a,v):
    q = queue.Queue()
    q.put(v)
    visited[v] = 1

    #너비 우선으로 큐에 입력
    #출력하면서 자녀 노드를 추가
    while(visited.count(1) < n):
        node = q.get()
        print(node)
        #print("출력 큐 " + str(node))
        for j in range(node,n):
            if (a[node][j] == 1 and visited[j] == 0):
                q.put(j)
                #print("들어가는 큐 " + str(j))
                visited[j] = 1
                #print("체크된 위치 " + str(j))

    #큐에 남은 노드 출력
    while(q.qsize() > 0):
        node = q.get()
        print(node)
          
BFS(a,0)
#-----------------------------------------------------------------------------
#Q2.
def promising(i,col):
    switch = True
    k = 0
    while (k < i and switch):
        if (col[i] == col[k] or (abs(col[i] - col[k]) == (i-k))):
            switch = False
        k = k + 1
    return switch


def queens(n,i,col):
    if (promising(i,col)):
        if (i == n-1):
            print(col)
        else:
            for j in range(n):
                col[i+1] = j
                queens(n,i+1,col)
    

#최종 결과로는 n=7일 경우의 결과를 출력
n = 7
col = n * [0]
queens(n, -1, col)
#-----------------------------------------------------------------------------

        

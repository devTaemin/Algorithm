#Kruskal Algorithm

parent = dict()
rank = dict()

def make_singleton_set(v):
    parent[v] = v
    rank[v] = 1

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(r1,r2):
    if (r1 != r2):
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if (rank[r1] == rank[r2]):
                rank[r2] += rank[r1]

def kruskal(graph):
    #vertices의 수 저장, edge의 수 저장
    n = len(graph['vertices'])
    m = len(graph['edges'])
    
    #graph의 edge들을 비내림차순으로 정렬한다.
    sorted_edges = sorted(list(graph['edges']))
    
    #vertices들을 singleton_set으로 만든다.
    for node in range(n):
        make_singleton_set(graph['vertices'][node])
        
    #edge를 저장하는 F=set()을 만든다.
    result = set()
    
    #반복문
    for rep in range(m-1):
        (e, i, j) = sorted_edges[rep]
        p = find(i)
        q = find(j)
        if (p != q):
            union(p,q)
            result.add(sorted_edges[rep])

    return result

graph = {
        'vertices': ['A','B','C','D','E'],
        'edges': set([
            (1, 'A', 'B'),
            (3, 'A', 'C'),
            (3, 'B', 'C'),
            (6, 'B', 'D'),
            (4, 'C', 'D'),
            (2, 'C', 'E'),
            (5, 'D', 'E')])
        }

mst = kruskal(graph)
print(mst)
#-------------------------------------------------------------------------
#Dijkstra Algorithm

inf = 1000
w = [[0, 7, 4, 6, 1],
     [inf, 0, inf, inf, inf],
     [inf, 2, 0, 5, inf],
     [inf, 3, inf, 0, inf],
     [inf, inf, inf, 1, 0]]
n = 5 #node의 수
f = set() #경로 저장
touch = n * [0] #index까지 이동하는데 거리가 최소가 되는 이전 node
length = n * [0] #길이 저장
save_length = n * [0] #해당 경로까지의 최소 길이 저장


#length를 W로부터 초기화
for i in range(n):
    length[i] = w[0][i]

#(node-1)번 반복
for i in range(n-1):

    #distance가 최소가 되는 길이, 인덱스찾기
    min_distance = inf
    min_index = 0
    for i in range(1,n):
        if (length[i] >= 0 and length[i] < min_distance):
            min_index = i
            min_distance = length[i]

    #경로 저장, 거리 저장
    e = (touch[min_index], min_index)
    f.add(e)
    save_length[min_index] = min_distance

    #경로 업데이트
    for i in range(1,n):
        if (length[min_index] + w[min_index][i] < length[i]):
            length[i] = length[min_index] + w[min_index][i]
            touch[i] = min_index

    length[min_index] = -1 #해당 노드는 더이상 고려하지 않음.
    


print(f)
print(save_length)

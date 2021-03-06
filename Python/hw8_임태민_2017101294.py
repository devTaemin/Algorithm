
#Knapsack problem
#branch and bound, Breadth-First Search
import queue

class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level    #층수 --> bestset, include의 좌표..?
        self.weight = weight  #무게 --> 최대 무게 W와 비교
        self.profit = profit  #이익 --> 더해진 이익
        self.include = include #더해진 상황

    def printNode(self):
        print("level: ", self.level, "profit: ", self.profit, "weight: ", self.weight, "include:", self.include)


    def copyNode(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include


def kp_BFS():
    global maxProfit
    global bestset

    q = queue.Queue()
    temp = Node(0, 0, 0, include)
    q.put(temp)

    while(not q.empty()):
        u = Node(0, 0, 0, include)
        v = q.get()
        #print("\n----------------------")
        #Node.printNode(v)
        #print("----------------------\n")
        
        u.level = v.level + 1
        
        if (u.level <= n):
            
            u.weight = v.weight + w[u.level-1]
            u.profit = v.profit + p[u.level-1]
            u.include = v.include
            
            #print("\n----------------------")
            #print(u.level)
            #Node.printNode(v)
            #Node.printNode(u)
            #print("----------------------\n")
            
            if (u.weight <= W and u.profit >= maxProfit):
                maxProfit = u.profit
                
            if (compBound(u) > maxProfit):
                #print("1들어가는 u")
                temp_include = u.include[:]
                temp_include[u.level-1] = 1
                copy_u = Node(u.level,u.weight,u.profit,temp_include)
                #Node.printNode(copy_u)
                q.put(copy_u)
                

            u.weight = v.weight
            u.profit = v.profit
            u.include = v.include
            #print("\n----------------------")
            #print(u.level)
            #Node.printNode(v)
            #Node.printNode(u)
            #print("----------------------\n")

            
            if (compBound(u) > maxProfit):
                #print("2들어가는 u")
                temp_include = u.include[:]
                copy_u = Node(u.level,u.weight,u.profit,temp_include)
                #Node.printNode(copy_u)
                q.put(copy_u)

            if (u.profit == maxProfit):
                bestset = u.include
        
        
        
    

    

def compBound(u):
    if (u.weight >= W):
        return 0;
    else:
        total_profit = u.profit
        total_level = u.level + 1
        total_weight = u.weight
        while (total_level <= n and total_weight + w[total_level-1] <= W):
            total_weight = total_weight + w[total_level-1]
            total_profit = total_profit + p[total_level-1]
            total_level = total_level + 1

        if (total_level <= n):
            total_profit = total_profit + ((W - total_weight) * p[total_level-1]/w[total_level-1])
        return total_profit
        
        




n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]

include = [0] * n
maxProfit = 0
bestset = n * [0]
kp_BFS()
print(bestset)


#Knapsack problem
#branch and bound, Best-first search


class Node:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

    #def __cmp__(self, other):
    #    return self.bound <= other.bound

    def __lt__(self, other):
        return self.bound <= other.bound
    
    def printNode(self):
        print("level: ", self.level, "profit: ", self.profit, "weight: ", self.weight, "include:", self.include, "bound:", self.bound)


    def copyNode(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include
        self.bound = bound



def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n * [0]
    v = Node(0, 0, 0, 0.0, temp)
    #구현
    PQ = queue.PriorityQueue()
    v.bound = compBound(v)
    PQ.put(v)
    #Node.printNode(v)

    while(not PQ.empty()):
        u = Node(0, 0, 0, 0.0, temp)
        v = PQ.get()
        
        if (v.bound <= maxProfit):
            u.level = v.level + 1
            if (u.level <= n):
                u.weight = (v.weight + w[u.level-1])
                u.profit = (v.profit + p[u.level-1])
                u.include = v.include
                u.bound = compBound(u)

                #print("\n----------left------------")
                #print(u.level)
                #Node.printNode(v)
                #Node.printNode(u)
                #print("----------------------------\n")

                if (u.weight <= W and u.profit > maxProfit):       
                    maxProfit = u.profit * -1
                    #print(maxProfit)

                
                if (u.bound < maxProfit):
                    temp_include = u.include[:]
                    temp_include[u.level-1] = 1
                    copy_u = Node(u.level, u.weight, u.profit, u.bound, temp_include)
                    PQ.put(copy_u)

                u.weight = v.weight
                u.profit = v.profit
                u.include = v.include
                u.bound = compBound(u)

                #print("\n----------right-------------")
                #Node.printNode(v)
                #Node.printNode(u)
                #print("-----------------------------\n")
                
                if (u.bound < maxProfit):
                    temp_include = u.include[:]
                    copy_u = Node(u.level, u.weight, u.profit, u.bound, temp_include)
                    PQ.put(copy_u)

                if (u.profit == maxProfit*-1):
                    bestset = u.include    
                
        


def compBound(u):
    if (u.weight >= W):
        return 0;
    else:
        total_profit = u.profit
        total_level = u.level + 1
        total_weight = u.weight
        while (total_level <= n and total_weight + w[total_level-1] <= W):
            total_weight = total_weight + w[total_level-1]
            total_profit = total_profit + p[total_level-1]
            total_level = total_level + 1

        if (total_level <= n):
            total_profit = total_profit + ((W - total_weight) * p[total_level-1]/w[total_level-1])
        return total_profit * -1



# heap이 minheap이라 bound를 계산하여 -를 하여 리턴한다. 비교를 < maxProfit으로 수행한다.
n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
include = [0] * n
maxProfit = 0
bestset = [0] * n
kp_Best_FS()
print(bestset)
print(maxProfit)







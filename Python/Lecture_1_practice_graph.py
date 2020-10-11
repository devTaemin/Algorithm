#Graph

g1 = [[0,1,1,0,0,0],
     [1,0,1,1,1,0],
     [1,1,0,1,0,0],
     [0,1,1,0,1,1],
     [0,1,0,1,0,0],
     [0,0,0,0,1,0]]

print(g1)
print()
print(len(g1))
print(len(g1[0]))

edge1 = 0
for i in range(len(g1)):
    for j in range(len(g1[i])):
        if (g1[i][j] == 1):
            edge1 += 1

print(f"Total edge = {edge1 / 2}")
print(g1[0][2])

total1 = 0
num1 = int(input("Input the number of node: "))
if (0 > num1 and num1 > 5):
    print("Out of range..")
else:
    for i in range(len(g1[num1])):
        if (g1[num1][i] == 1):
            total1 += 1
    print(f"The number of nodes on node{num1} is {total1}.")
    
    
g2 = {'A' : {'B','C'},
      'B' : {'A','C','D','E'},
      'C' : {'A','B','D'},
      'D' : {'B','C','E','F'},
      'E' : {'B','D'},
      'F' : {'D'}}

print(g2)
print()
print(len(g2))
print(len(g2['A']))

edge2 = 0
keys = g2.keys()
for i in keys:
    edge2 += len(g2[i])

print(f"Total edge = {edge2 / 2}")
print('C' in g2['A'])

total2 = 0
key1 = input("Input the id of node: ")
if (key1 not in keys):
    print("Incorrect key")
else:
    total2 = len(g2[key1])
    print(f"The number of edges on {key1} is {total2}.")
    



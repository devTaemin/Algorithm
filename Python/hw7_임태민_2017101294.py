#Sum of subsets Problem

def promising(i, weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i+1] <= W)


def s_s(i, weight, total, include):
    sorted_w = w[:]
    sorted_w.sort()
    if (promising(i, weight, total)):
        if (weight == W):
            print("sol", include)
        else:
            include_o = include[:]
            include_o[i+1] = 1
            s_s(i+1, weight + sorted_w[i+1], total - sorted_w[i+1], include_o)

            include_x = include[:]
            include_x[i+1] = 0
            s_s(i+1, weight, total - sorted_w[i+1], include_x)
            
n = 4
w = [1,4,2,6]
W = 6

print("items =", w,  "W =", W)
include = n * [0]
total = 0

for k in w:
    total += k

s_s(-1, 0, total, include)


#m-coloring
def color(i, vcolor):
    if (promising(i, vcolor)):
        if (i == n-1):
            print(vcolor)
        else:
            for col in range(m):
                vcolor[i+1] = col + 1
                color(i+1, vcolor)
        


def promising(I, vcolor):
    switch = True
    j = 0
    while (j < I and switch):
        if (W[I][j] and vcolor[I] == vcolor[j]):
            switch = False
        j += 1
    return switch


n = 4
W = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
vcolor = n * [0]
m = 3
color(-1, vcolor)




























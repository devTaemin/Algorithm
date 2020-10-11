#Set
'''
#1.
s = {1,3,3,5,7}
print(s)
empty_s = set()
print(empty_s)
empty_s.add(9)
print(empty_s)
new_s = {1, 2.3, "ABC", (5, 6, "D")}
print(new_s)


#unhashable_s = {{"a":1,"b":2,"c":3}, [1,2,3]}    TypeError: unhashable type
s1 = set([1,2,3])
s2 = {}
s3 = set()
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))


f1 = {1,2,3}
print(f1)
f1.add(4)
print(f1)
#f1.add(5,6)  TypeError: add() takes exactly one argument (2 given)

f2 = {1,2,3}
f3 = {1,2,3}
f2.update([4,5])
f3.add(4)
f3.add(5)
print(f2)
print(f3)
f2.update((6,7))
f3.add((6,7))
print(f2)
print(f3)
f2.update(((8,9)))
print(f2)

f2.discard(1)
#f2.remove(1)
f3.remove(1)
f3.discard(1)
print(f2)
print(f3)


g1 = {1,2,3,4,5}
g2 = set()
for i in g1:
    if i not in {3,5}:
        g2.add(i)
print(g2)

g3 = {1,2,3,4,5}
g3 = {x for x in g3 if x not in {3,5}}
print(g3)
'''
k1 = {1,2,3}
k2 = {3,4,5}
k3 = k1|k2
print(k3)
print(k1.union(k2))

k4 = k1&k2
print(k4)
print(k1.intersection(k2))

k5 = k1-k2
print(k5)
print(k1.difference(k2))

k6 = k1^k2
print(k6)
print(k1.symmetric_difference(k2))

k7 = {1,2,3}
print(2 in k7)
print(5 in k7)



















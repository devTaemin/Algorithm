#dictionary
d1 = {}
print(d1, type(d1))

d1 = {1:'car', 2:'house'}
print(d1, type(d1))

d2 = {'kk':'car', 2:[5,7]}
print(d2, type(d2))

d3 = {'college':'kyunghee', 'major':'CS'}
print(d3)

d4 = dict({'college':'kyunghee', 'major':'CS'})
print(d4)

d5 = dict([('college','kyunghee'), ('major1', 'CS'), ('major2', 'IS'), ('id', 0)])
print(d5)
print(d5['college'])
print(d5['major1'])
print(d5.get('major2'))

d5['id'] = 2017101294
print(d5)

d5['grade'] = 'senior'
print(d5)

del d5['grade']
print(d5)

#d5.clear()
#print(d5)

print('college' in d5)
print('grade' in d5)


for idx, i in enumerate(d5):
    print(idx, i)























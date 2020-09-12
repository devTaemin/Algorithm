#print format
'''
a = 1.2
b = 345
print(f'A is {a}, B is {b}')

age = 27
name = 'Taemin'
print(f'My name is {name} and my age is {age}.')

c = 2
print(f'{c} {c*c} {c*c*c}')

print(f'A is {a:3.1f}, B is {b:3d}')
print(f'A is {a:7.3f}, B is {b:5d}')

d = 123.4567
print(f'{a:10.3e}')
print(f'{a:10.4e}')
print(f'{a:13.4e}')
print(f'{a:10.1f}')
print(f'{a:11.5f}')
'''

total_sum = 0
e = 1.5
while e < 3.5:
    print(f'{e:6.2f}')
    total_sum += e
    e += 0.1
print(f'Total = {total_sum:6.2f}')

name = 'Taemin'
print(f'My name is {name:^10}.')
print(f'My name is {name:<10}.')
print(f'My name is {name:>10}.')

number = 123
print(f'number = {number:10}')
print(f'number = {number:>10}')
print(f'number = {number:^10}')
print(f'number = {number:<10}')

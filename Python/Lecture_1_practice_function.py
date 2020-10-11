#Function
'''
def comp(x,y):
    result_sum = x + y
    result_mul = x * y
    return result_sum, result_mul

return_sum, return_mul = comp(4, 5)
print("Sum :", return_sum)
print("Multiplication :", return_mul)


def numComp(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return a*a + b*b + c*c

def numInput():
    x, y, z = input("X = "), input("Y = "), input("Z = ")
    print("The sum of square =", numComp(x, y, z))


numInput()

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(7))

def fact(n):
    if n == 0:
        return 1
    else:
        return  n * fact(n-1)

print(fact(4))
print(fact(0))
'''
def days(a):
    d = 0
    for i in range(0,12):
        if (i % 2 == 0):
            d += a[i]
    return d
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days(month_days))
            





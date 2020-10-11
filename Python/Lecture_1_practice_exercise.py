#Exercise

'''
def sequential_S(arr, x):
    for idx, i in enumerate(arr):
        if (i == x):
            print(f'The index of {x} is {idx}.')
            return
    print(f'{x} NOT FOUND')


temp1 = ['A','B','C','D','E']
sequential_S(temp1, "A")
sequential_S(temp1, "E")
sequential_S(temp1, "H")


def sequential_Sum(arr):
    length = len(arr)
    total = 0
    for i in range(length):
        total += arr[i]
    return total

temp2 = [1,2,3,4,5,6,7]
print(sequential_Sum(temp2))


def multiply_Matrix(Mat1, Mat2):

    row1 = len(Mat1)
    col1 = len(Mat1[0])
    row2 = len(Mat2)
    col2 = len(Mat2[0])

    if (col1 != row2):
        print('ERROR')
    else:
        Mat = [[0 for i in range(row1)] for j in range(col2)]

        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    Mat[i][j] += Mat1[i][k] * Mat2[k][j]
        return Mat
  

m1 = [[1,2,3], [4,5,6]]
m2 = [[3,6], [2,5], [1,4]]
m3 = multiply_Matrix(m1,m2)
print(m3)
m4 = multiply_Matrix(m1,m3)


def binary_S(arr, x):
    #pre-requisite: arr is sorted
    length = len(arr)
    front = 0
    rear = length - 1
    found = False
    
    while((front <= rear) and (not found)):
        mid = int((front + rear) / 2)
        if (arr[mid] == x):
            found = True
        elif (arr[mid] < x):
            front = mid + 1
        else:
            rear = mid - 1
        

    if (found):
        print(f'{x} is located in index {mid}')
    else:
        print("NOT FOUND")

a = [1, 3, 5, 6, 7, 8, 9, 13, 14, 19]
binary_S(a, 14)
'''

def fib1(num):
    #함수로 구현한 피보나치 수열
    #2진 계산을 수행하는 컴퓨터의 특성상 계산 과정에서 오차가 날 수 있다

    from math import sqrt

    func = (((1 + sqrt(5)) / 2) ** num - ((1 - sqrt(5)) / 2) ** num) / sqrt(5)
    return int(func)

def fib2(num):
    #반복문을 이용한 피보나치 수열

    fib_list = [0,1]
    if (num == 0):
        return fib_list[0]
    elif (num == 1):
        return fib_list[1]
    else:
        for i in range(1,num):
            v = fib_list[i - 1] + fib_list[i]
            fib_list.append(v)
        return fib_list[num]
            
def fib3(num):
    #재귀를 이용한 피보나치 수열
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fib3(num - 1) + fib3(num - 2)
    
print(fib3(0))
print(fib3(1))
print(fib3(4))
print(fib3(10))



    
    

















            
            

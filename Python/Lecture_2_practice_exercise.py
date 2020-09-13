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
'''

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

    

            
            

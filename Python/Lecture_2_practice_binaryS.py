#Binary Search: Recursive

def BinaryS(front, rear, x, arr):

    if (front > rear):
        return 0
    else:
        mid = int((front + rear) / 2)
        if (arr[mid] == x):
            return mid
        else:
            if (arr[mid] < x):
                return BinaryS(mid + 1, rear, x, arr)
            else:
                return BinaryS(front, mid - 1, x, arr)

# 중복되어 있는 해당 x의 모든 index를 출력하려면..?

#S = [0, 1, 1, 3, 5, 6, 8, 10]
#a = BinaryS(0, 7, 12, S)
#print(a)


# 5page
def bs(data, item, low, high):

    if(low > high):
        return 0
    else:
        mid = int((low + high) / 2)
        if(data[mid] == item):
            return mid
        else:
            if (data[mid] < item):
                return bs(data, item, mid + 1, high)
            else:
                return bs(data, item, low, mid - 1)

data = [1, 3, 5, 6, 7, 9, 10, 14, 17, 19]
n = 10
location = bs(data, 17, 0, n-1)
print(location)
    
    

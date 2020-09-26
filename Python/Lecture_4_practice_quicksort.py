#QuickSort (Partition exchange sort Algorithm)


def quickSort(s, low, high):
    if (low < high):
        pivot_index = partition(s,low,high)
        quickSort(s,low, pivot_index - 1)
        quickSort(s,pivot_index + 1, high)
        


def partition(s, low, high):
    pivot = low
    loc = low
    for i in range(low+1, high+1):
        if (s[pivot] > s[i]):
            loc+=1
            temp = s[loc]
            s[loc] = s[i]
            s[i] = temp

    temp_pivot = s[pivot]
    s[pivot] = s[loc]
    s[loc] = temp_pivot
    return loc

print("----- Quick Sort -----")
arr = [15,22,13,27,12,10,20,25]
print(f'Before QuickSort: {arr}')
quickSort(arr, 0, 7)
print(f'After QuickSrot: {arr}\n')


    
    




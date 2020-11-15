# MergeSort

memory1 = 0
memory1_record = list()
memory2 = 0
memory2_record = list()
def mergeSort(n, s):
    #n = 배열 s에 있는 데이터의 수
    #s = 배열
    global memory1
    global memory1_record
    half = int(n / 2) 
    remain = n - half 

    if (n > 1):
        U = s[:half]
        memory1 += half      #메모리 추가
        memory1_record.append(memory1)
        V = s[half:]
        memory1 += remain    #메모리 추가
        memory1_record.append(memory1)
        mergeSort(half, U)
        mergeSort(remain, V)
        return merge(half, remain, U, V, s)


def merge(h, m, u, v, s):
    global memory1
    global memory1_record
    i = 0 # u의 index역할, h가 u에 있는 데이터의 수 이므로 미만이어야 한다.
    j = 0 # v의 index역할, m이 v에 있는 데이터의 수 이므로 미만이어야 한다. 
    k = 0 # 합쳐질 배열 s의 index역할
    while (i < h) and (j < m):
        if (u[i] < v[j]):
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1

    if (i >= h):
        s[k:h+m] = v[j:m]
    else:
        s[k:h+m] = u[i:h]
    memory1 -= (h + m)    #메모리 해제
    memory1_record.append(memory1)
    return s


s = [3, 5, 2, 9, 10, 14, 4, 8]
print("MergeSort 1")
print(f'정렬 전 리스트: {s}')
print(f'정렬 후 리스트: {mergeSort(8, s)}')
print(f'추가 저장공간 : {max(memory1_record)}')


def mergeSort2(s, low, high):
    # low는 첫번째 data의 index
    # high은 마지막 data의 index
    if (low < high):
        mid = int((low + high) / 2)
        mergeSort2(s, low, mid) #left
        mergeSort2(s, mid+1, high) # right
        return merge2(s, low, mid, high)


def merge2(s, low, mid, high):
    global memory2
    global memory2_record
    i = low #left 시작점
    j = mid + 1 #right 시작점
    k = low #합쳐진 배열의 index
    U = [0 for i in range(0, (high - low + 1))] #합병하는데 필요한 메모리
    
    memory2 += (high - low + 1)      #메모리 
    memory2_record.append(memory2)   
   
    while (i <= mid and j <= high):
        if(s[i] < s[j]):
             U[k - low] = s[i]
             i += 1
        else:
             U[k - low] = s[j]
             j += 1
        k += 1

    if (i > mid):
         U[k - low:] = s[j:high+1]
    else:
         U[k - low:] = s[i:mid+1]

    s[low:high+1] = U[:]
    memory2 -= (high - low + 1)
    memory2_record.append(memory2)
    

    return s
    

s = [3, 5, 2, 9, 10, 14, 4, 8]
print("\nMergeSort 2")
print(f'정렬 전 리스트: {s}')
print(f'정렬 후 리스트: {mergeSort2(s, 0, 7)}')
print(f'추가 저장공간 : {max(memory2_record)}')




        
        
    
    

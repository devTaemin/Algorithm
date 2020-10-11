

def alg1(size):
    import time
    start_time = time.time()
    lst = list(range(1,size+1))                
    for idx, i in enumerate(lst):              
        total = 0
        for j in range(1, i+1):
            total += j
        print(f'avg{idx+1} = {total / (idx+1)}')
    end_time = time.time()
    print(f'alg1({size}) Runtime = {end_time - start_time}\n')
        


def alg2(size):
    import time
    start_time = time.time()
    lst = list(range(1,size+1))
    total = 0
    for idx, i in enumerate(lst):
        total += i
        print(f'avg{idx+1} = {total / (idx+1)}')
    end_time = time.time()
    print(f'alg2({size}) Runtime = {end_time - start_time}\n')



#alg1(10000)
#alg1(20000)
#alg1(30000)
#alg2(10000)
#alg2(20000)
alg2(30000)

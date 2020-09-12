import time
N = 50000000
d = []
a = range(N)

startTime = time.time()
for i in a:
    d.append(2*i)
endTime = time.time()

duration = endTime - startTime
print(duration)

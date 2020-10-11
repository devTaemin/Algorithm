#question
'''
#1.
scores = [0,0,0,0,0]
total_score = 0
for idx, score in enumerate(scores):
    scores[idx] = float(input(f"Input your score{idx}: "))
    total_score += scores[idx]

average_score = total_score / len(scores)
maximum_score = max(scores)
print(f'Average score = {average_score}')
print(f'Maximum score = {maximum_score}')
'''


#2.
def inputData():
    lst = []
    rep = 0
    while(True and (rep < 3)):
        datum = float(input("Input positive number: "))
        if (datum <= 0):
            print('fin\n')
            break
        else:
            lst.append(datum)
            rep += 1
    
    return lst

def dataProcess(listA):
    length = len(listA)
    if (length <= 1):
        print('dataProcess-fin\n')
    elif (length == 2):
        print(f'Area = {listA[0] * listA[1]}')
        print(f'Perimeter = {(listA[0] + listA[1]) * 2}')
    else:
        print(f'Volume = {listA[0] * listA[1] * listA[2]}')

temp = inputData()
temp2 = inputData()
dataProcess(temp)
dataProcess(temp2)

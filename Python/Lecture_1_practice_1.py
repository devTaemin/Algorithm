#1. Identifier

#2. Reserve words

#3. Input/Output
'''
print("Type any number: ")
a = input()
print("Result:", a)
print("Result type:", type(a))

b = input("Type any words: ")
print("Result:", b)
print("Result type:", type(b))

# input으로 받은 값들은 숫자를 입력하더라도 내부에서는 string으로 인식한다.
# 따라서 입력 받은 값을 특정 type으로 typecast를 해서 사용한다.
'''

#4. concatenation, typecast->add
'''
a = input("Type string1: ")
b = input("Type string2: ")
print(a + b)
print(a + "world!\n")

c = input("Type any float1: ")
d = input("Type any float2: ")
c = float(c)                    
d = float(d)
print("result = ", c + d)
'''

#5. string functions
# a.find(), a.count(), a.upper(), a.lower(), a.strip(), a.replace(), a.split()


#6. Precedence
# not > and > or


#7. Repetition
'''
sum = 0
for d in range(1,11,2):
    sum = sum + d
    print(d)
print("result =", sum)
'''

#Question 32page Solution
'''
a = float(input("Input the length of width of square: "))
b = float(input("Input the length of height of square: "))
side_sum = 2 * (a + b)
area = a * b
print("Total length of sqaure: ", side_sum)
print("Total area of square: ", area)
'''

#Question 33page Solution
'''
a = input("Type any word1: ")
b = input("Type any word2: ")
c = input("Type any word3: ")

for i in [a,b,c]:
    first = i
    for j in [a,b,c]:
        second = j
        if (first == second):
            continue
        else:
            for k in [a,b,c]:
                third = k
                if (third != first and third != second):
                    print(first + second + third)
                else:
                    continue
'''

#Question 37page Solution
'''
season = input("Choose summer or winter: ")
temperature = float(input("Input degree of teperature: "))

if (season == "summer"):
    if (temperature >= 30):
        print("hot")
    elif (temperature >= 20 and temperature <= 29):
        print("warm")
    else:
        print("cool")
elif (season == "winter"):
    if (temperature >= 10):
        print("warm")
    else:
        print("cold")
else:
    print("Error: You've typed wrong season!")
'''


#Question 38page Solution
'''
a = int(input("Input the integer value: "))
if (a == 0):
    print("zero")
else:
    if (a > 0):
        print("positive")
    else:
        print("negative")
'''


#Question 43page Solution
'''
a = int(input(("Input the natural number: ")))
if (a % 2 == 0):
    print("even\n")
else:
    print("odd\n")


b = int(input("Input the natural number: "))
if (b % 5 == 0):
    if (b % 4 == 0):
        print("multiplication of 20\n")
    else:
        print("multiplication of 5\n")
elif (b % 4 == 0):
    print("multiplication of 4\n")
else:
    print("none")
'''


#Question 52page Solution
'''
n = 2
while n < 1000:
    print(n)
    n = n *2

k = 1
sum1 = 0
while (sum1 + k <= 1000):
    sum1 = sum1 + k
    k = k + 1
print("n =", k-1)
'''


#Question 53page Solution
sum1 = 0
for i in range(1,101):
    if (i % 5 == 0):
        sum1 = sum1 + i

print(sum1)

sum2 = 0
for j in range(100, 201):
    if (j % 2 == 1):
        sum2 = sum2 + j
print(sum2)





















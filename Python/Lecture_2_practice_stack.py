#stack

class Stack(object):

    top = 0
    data = None
    length = None

    def __init__(self, length):
        self.length = length
        self.data = self.length*[0]

    def isFull(self):
        return (self.top == self.length)

    def isEmpty(self):
        if (self.top == 0):
            return True

    def push(self, name):
        if (self.isFull() == True):
            print("Stack is full")
            return
        else:
            self.data[self.top] = name
            self.top += 1

    def pop(self):
        if (self.isEmpty() == True):
            print("no data")
            return
        else:
            temp = self.data[self.top-1]
            self.top -= 1
            return temp

    def printStack(self):
        if (self.isEmpty() == True):
            return
        for i in range(0, self.top):
            print(self.data[i])
        print()


s = Stack(5)
if (s.isEmpty()):print("EMPTY")
else:print("NOT EMPTY")

s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
s.push("F")
s.printStack()
print(s.pop())
print()
s.printStack()

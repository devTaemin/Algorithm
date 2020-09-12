#queue (Circular)

class Queue(object):

    front = 0
    rear = 0
    data = None
    length = None

    def __init__(self,length):
        self.length = length
        self.data = self.length*[0]

    def isFull(self):
        return (self.rear + 1) % self.length == self.front

    def isEmpty(self):
        if (self.front == self.rear):
            return True

    def enqueue(self, name):
        if (self.isFull() == True):
            print("Queue is full")
            return
        else:
            self.data[self.rear] = name
            self.rear = (self.rear + 1) % self.length

    def dequeue(self):
        if (self.isEmpty() == True):
            print("no data")
        else:
            temp = self.data[self.front]
            self.front = (self.front + 1)
            return temp

    def printQ(self):
        if (self.isEmpty() == True):
            return
        if (self.rear < self.front):
            for i in range(self.front, self.length):
                print(self.data[i], end = " ")
            for j in range(0, self.rear):
                print(self.data[j], end = " ")
        else:
            for k in range(self.front, self.rear):
                print(self.data[k], end = " ")
        print()

q=Queue(5)
q.enqueue("A")
q.printQ()
q.enqueue("B")
q.printQ()
q.enqueue("C")
q.enqueue("D")
q.printQ()
q.dequeue()
q.printQ()
q.dequeue()
q.printQ()
q.enqueue("E")
q.printQ()
q.enqueue("F")
q.printQ()
q.dequeue()
q.printQ()














       

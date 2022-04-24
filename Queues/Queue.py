# Implementing Queue using Python List
class Queue: # using one list - ArrayQueue
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.__items = [0] * self.capacity
        self.__front = 0
        self.__rear = 0
        self.__count = 0

    def enqueue(self, item):
        if self.__count == self.capacity:
            raise Exception('Queue is full.')
        self.__items[self.__rear] = item
        self.__rear = (self.__rear + 1) % self.capacity
        self.__count += 1

    def dequeue(self):
        item = self.__items[self.__front]
        self.__items[self.__front] = 0
        self.__front = (self.__front + 1) % self.capacity
        self.__count -= 1
        return item

    def peek(self):
        return self.__items[self.__front]

    def isEmpty(self):
        return self.__front == self.__rear

    def isFull(self):
        return self.__count == self.capacity

    def __str__(self):
        # return str(self.__items[self.__front:self.__rear])
        return str(self.__items)

class Queue2: # using two lists - implement Queue with two stacks
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def enqueue(self, item): # O(1)
        self.__stack1.append(item)

    def dequeue(self): # O(n)
        if self.isEmpty():
            raise Exception('Queue is empty.')

        self.__moveStack1ToStack2()
        return self.__stack2.pop()

    def dequeue(self): # O(n)
        if self.isEmpty():
            raise Exception('Queue is empty.')

        self.__moveStack1ToStack2()
        return self.__stack2[-1]

    def isEmpty(self):
        return (not bool(self.__stack1)) and (not bool(self.__stack1))

    def __moveStack1ToStack2(self):
        if not bool(self.__stack2):
            while bool(self.__stack1):
                self.__stack2.append(self.__stack1.pop())

if __name__ == "__main__":
    print("Implement with one list - one array")
    queue = Queue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    var = queue.dequeue()
    print(var)
    print(queue)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    print(queue)
    queue.dequeue()
    print(queue)

    print("\nImplement with two lists - two stacks")
    queue2 = Queue2()
    queue2.enqueue(10)
    queue2.enqueue(20)
    queue2.enqueue(30)
    # print(queue2)
    var = queue2.dequeue()
    print(var)
    # print(queue2)
    var = queue2.dequeue()
    var = queue2.dequeue()
    var = queue2.dequeue()

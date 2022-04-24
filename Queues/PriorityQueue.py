# Priority Queues can be implemented using Array or Heap
# Here the implementation is using Array - actually Python List

class PriorityQueue: # Assume the Queue is in ascending order
    def __init__(self):
        self.__items = [0] * 5
        self.__count = 0

    def add(self, item):
        if self.__count == len(self.__items): # isFull()
            raise Exception("Queue is full.")

        i = self.__shiftItemsToInsert(item)
        self.__items[i] = item
        self.__count += 1

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue is empty/")
        self.__count -= 1
        return self.__items[self.__count]

    def isEmpty(self):
        return self.__count == 0

    def __shiftItemsToInsert(self, item):
        i = self.__count - 1
        while i >= 0:
            if self.__items[i] > item:
                self.__items[i+1] = self.__items[i]
            else:
                break
            i -=
        return i+1

    def __str__(self):
        return str(self.__items)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.add(5)
    pq.add(3)
    pq.add(6)
    pq.add(1)
    pq.add(4)
    print(pq)

    while not pq.isEmpty():
        print(pq.remove())

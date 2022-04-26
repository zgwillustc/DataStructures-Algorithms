# Implementing Heap using Python List
class Heap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        childIndex = len(self.values) - 1
        self.__bubbleUp(childIndex)

    def __bubbleUp(self, childIndex): # Can also use iteration besides recursion
        parentIndex = (childIndex - 1) // 2
        if parentIndex < 0:
            return
        if self.values[childIndex] > self.values[parentIndex]:
            self.__swap(childIndex, parentIndex)
            self.__bubbleUp(parentIndex)

    def remove(self):
        if self.isEmpty():
            raise Exception('Heap is empty.')
        removed_item = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.__bubbleDown(0)
        return removed_item

    def __bubbleDown(self, parentIndex):
        idx = self.__largerChildIndex(parentIndex)
        if not idx:
            return
        if self.values[idx] > self.values[parentIndex]:
            self.__swap(idx, parentIndex)
            self.__bubbleDown(idx)

    def __largerChildIndex(self, parentIndex):
        if not self.__hasLeftChild(parentIndex):
#            return parentIndex
            return None
        if not self.__hasRightChild(parentIndex):
            return self.__leftChildIndex(parentIndex)
        return self.__leftChildIndex(parentIndex) \
            if self.__leftChild(parentIndex) > self.__rightChild(parentIndex) \
            else self.__rightChildIndex(parentIndex)

#        leftChildIndex = parentIndex * 2 + 1
#        rightChildIndex = parentIndex * 2 + 2
#        if leftChildIndex > len(self.values) - 1:
#            return None
#        elif rightChildIndex > len(self.values) - 1:
#            return leftChildIndex
#        elif self.values[leftChildIndex] > self.values[rightChildIndex]:
#            return leftChildIndex
#        else:
#            return rightChildIndex

    def __leftChild(self, parentIndex):
        return self.values[self.__leftChildIndex(parentIndex)]

    def __rightChild(self, parentIndex):
        return self.values[self.__rightChildIndex(parentIndex)]

    def __leftChildIndex(self, parentIndex):
        return parentIndex * 2 + 1

    def __rightChildIndex(self, parentIndex):
        return parentIndex * 2 + 2

    def __hasLeftChild(self, parentIndex):
        return self.__leftChildIndex(parentIndex) < len(self.values)

    def __hasRightChild(self, parentIndex):
        return self.__rightChildIndex(parentIndex) < len(self.values)

    def __swap(self, idx1, idx2):
        self.values[idx1], self.values[idx2] = \
        self.values[idx2], self.values[idx1]

    def isEmpty(self):
        return len(self.values) == 0

    def max(self):
        if self.isEmpty():
            raise Exception('Heap is empty.')
        return self.values[0]

def main():
    heap = Heap()
    heap.insert(10)
    heap.insert(15)
    heap.insert(5)
    heap.insert(12)
    print(heap.values)
    print(heap.remove())
    print(heap.values)
    print(heap.remove())
    print(heap.values)
    print(heap.remove())
    print(heap.values)
    print(heap.remove())
    print(heap.values)
    #print(heap.remove())

    print('\nHeap2:')
    heap = Heap()
    heap.insert(15)
    heap.insert(10)
    heap.insert(3)
    heap.insert(8)
    heap.insert(12)
    heap.insert(9)
    heap.insert(4)
    heap.insert(1)
    heap.insert(24)
    print(heap.values)
    print(heap.remove())
    print(heap.values)

    print('HeapSort:')
    random_num = [5, 3, 10, 1, 4, 2]
    heap = Heap()
    for num in random_num:
        heap.insert(num)
    print(heap.values)
    numbers = []
    while not heap.isEmpty():
        numbers.append(heap.remove())
    print(numbers)

if __name__ == '__main__':
    main()

import Heap

class MaxHeap:
    def heapify(self, numbers):
        for i in range(len(numbers)):
            self.__heapify(numbers, i)

    def heapify1(self, numbers):
        for i in range(len(numbers)//2-1):
            self.__heapify(numbers, i)

    def heapify2(self, numbers):
        lastParentIndex = len(numbers)//2-1
        for i in range(lastParentIndex, -1, -1):
            self.__heapify(numbers, i)

    def __heapify(self, numbers, idx):
        largerIndex = idx
        leftIndex = idx * 2 + 1
        if leftIndex < len(numbers) and numbers[leftIndex] > numbers[largerIndex]:
            largerIndex = leftIndex

        rightIndex = idx * 2 + 2
        if rightIndex < len(numbers) and numbers[rightIndex] > numbers[largerIndex]:
            largerIndex = rightIndex

        if idx == largerIndex:
            return

        swap(numbers, idx, largerIndex)
        self.__heapify(numbers, largerIndex)

    def getKthLargest(self, numbers, k):
        if k < 1 or k > len(numbers):
            raise Exception('Out of index range.')
        heap = Heap.Heap()
        for num in numbers:
            heap.insert(num)
        for i in range(k-1):
            heap.remove()
        return heap.max()

def swap(numbers, first, second):
    numbers[first], numbers[second] = numbers[second], numbers[first]

def main():
    print('Heapify:')
    numbers = [5, 3, 8, 4, 1, 2]
    hp = MaxHeap()
    hp.heapify2(numbers)
    print(numbers)

    print('Kth largest:')
    numbers = [5, 3, 8, 4, 1, 2]
    hp = MaxHeap()
    print(hp.getKthLargest(numbers, 6))


if __name__ == '__main__':
    main()

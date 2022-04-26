# Implementing Priority Queue using Heap
# Compared to Priority Queue implemented using Array
#           PQ-Array        PQ-Heap
# insert    O(n)            O(log n)
# remove    O(1)            O(log n)
import Heap

class PriorityQueue:
    def __init__(self):
        self.heap = Heap.Heap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.remove()

    def isEmpty(self):
        return self.heap.isEmpty()

def main():
    pqueue = PriorityQueue()
    pqueue.enqueue(5)
    pqueue.enqueue(3)
    pqueue.enqueue(6)
    pqueue.enqueue(1)
    pqueue.enqueue(4)
    print(pqueue.heap.values)

    while not pqueue.isEmpty():
        print(pqueue.dequeue())

if __name__ == '__main__':
    main()

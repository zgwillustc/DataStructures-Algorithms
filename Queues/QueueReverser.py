class QueueReverser:
    def reverse(self, queue):
        stack = []
        while bool(queue):
            stack.append(queue.pop(0))
        while bool(stack):
            queue.append(stack.pop())

if __name__ == "__main__":
    reverser = QueueReverser()
    queue = [10, 20, 30]
    reverser.reverse(queue)
    print(queue)

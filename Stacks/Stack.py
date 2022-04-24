# Implementing Stack using Python List
class Stack:
    def __init__(self):
        self.__items = [0] * 5
        self.__count = 0

    def push(self, item):
        if self.__count == len(self.__items):
            raise OverflowError('Stack is full.')
        self.__items[self.__count] = item
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Empty stack.')
        self.__count -= 1
        return self.__items[self.__count]

    def peek(self):
        if self.isEmpty():
            raise Exception('Empty stack.')
        return self.__items[self.__count-1]

    def isEmpty(self):
        return self.__count == 0

    def __str__(self):
        return str(self.__items[:self.__count])

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(stack.pop())
    print(stack)
    stack.push(40)
    print(stack)
    print(stack.peek())
    print(stack)

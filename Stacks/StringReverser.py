class StringReverser:
    def reverse(self, string):
        if not isinstance(string, str):
            raise ValueError('Not a string!')
        stack = []
        for char in string:
            stack.append(char)
        reversed_buffer = []
        while stack:
            reversed_buffer.append(stack.pop())
        reversed = ''.join(reversed_buffer)
        return reversed

if __name__ == "__main__":
    reverser = StringReverser()
    print(reverser.reverse(None))

class Expression:
    def __init__(self):
        self.__leftBrackets = ['(', '<', '[', '{']
        self.__rightBrackets = [')', '>', ']', '}']

    def isBalanced(self, string):
        stack = []
        for char in string:
            if self.__isLeftBracket(char):
                stack.append(char)

            if self.__isRightBracket(char):
                if len(stack) == 0: return False

                top = stack.pop()
                if not self.__bracketsMatch(top, char): return False
        return not bool(stack)

    def __isLeftBracket(self, char):
        return char in self.__leftBrackets

    def __isRightBracket(self, char):
        return char in self.__rightBrackets

    def __bracketsMatch(self, left, right):
        return self.__leftBrackets.index(left) == \
               self.__rightBrackets.index(right)


if __name__ == "__main__":
    # Edge cases:
    # (
    # (()
    # ) (
    # ( ]
    expression = Expression()
    print(expression.isBalanced('((1+ 3)'))

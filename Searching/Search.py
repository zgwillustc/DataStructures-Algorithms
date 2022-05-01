class Search:
    def __init__(self, array, target):
        self.array = array
        self.target = target
        self.size = len(array)

    def linearSearch(self):
        for idx, num in enumerate(self.array):
            if self.target == num:
                return idx
        return -1

    # My implementaion
#    def binarySearch(self): # Recursion
#        return self.__binarySearch(0, self.size-1)

#    def __binarySearch(self, left, right):
#        if left == right:
#            return left if self.array[left] == self.target else -1
#        middle = (left + right) // 2
#        if self.array[middle] < self.target:
#            return self.__binarySearch(middle+1, right)
#        elif self.array[middle] > self.target:
#            return self.__binarySearch(left, middle) # ? middle-1
#        else:
#            return middle
#        #return -1

#    def binarySearchIter(self): # Iteration
#        left, right = 0, self.size-1
#        while left < right:
#            middle = (left + right) // 2
#            if self.array[middle] < self.target:
#                left = middle + 1
#            elif self.array[middle] > self.target:
#                right = middle
#            else:
#                return middle
#        return left if self.array[left] == self.target else -1

    def binarySearch(self): # Recursion
        return self.__binarySearch(0, self.size-1)

    def __binarySearch(self, left, right): # Recursion
        if right < left:
            return -1
        middle = (left + right) // 2
        if self.array[middle] < self.target:
            return self.__binarySearch(middle+1, right)
        elif self.array[middle] > self.target:
            return self.__binarySearch(left, middle-1)
        else:
            return middle

    def binarySearchIter(self): # Iteration
        left, right = 0, self.size-1
        while left <= right:
            middle = (left + right) // 2
            if self.array[middle] < self.target:
                left = middle + 1
            elif self.array[middle] > self.target:
                right = middle - 1
            else:
                return middle
        return -1

    def ternarySearch(self):
        return self.__ternarySearch(0, self.size-1)

    def __ternarySearch(self, left, right):
        if right < left:
            return -1
        partitionSize = (right - left) // 3
        mid1 = left + partitionSize
        mid2 = right - partitionSize
        if self.target == self.array[mid1]:
            return mid1
        elif self.target == self.array[mid2]:
            return mid2
        elif self.target < self.array[mid1]:
            return self.__ternarySearch(left, mid1-1)
        elif self.target > self.array[mid2]:
            return self.__ternarySearch(mid2+1, right)
        else:
            return self.__ternarySearch(mid1+1, mid2-1)

    # My solution
    def jumpSearch(self):
        blockSize = int(self.size**(1/2))
        start = 0
        while start < self.size:
            next = min(start + blockSize, self.size)
            if self.target == self.array[next-1]:
                return next-1
            elif self.target < self.array[next-1]:
                for i in range(start, next):
                    if self.target == self.array[i]:
                        return i
            start += blockSize
        return -1

    # Mosh's solution
    def jumpSearchMo(self):
        blockSize = int(pow(self.size, 0.5))
        start = 0
        next = blockSize

        while start < self.size and self.array[next-1] < self.target:
            start = next
            next += blockSize
            if next > self.size:
                next = self.size

        for i in range(start, next):
            if self.target == self.array[i]:
                return i
        return -1

    def exponentialSearch(self):
        bound = 1
        while bound < self.size and self.array[bound] < self.target:
            bound *= 2
        left = bound // 2
        right = min(bound, self.size-1)
        return self.__binarySearch(left, right)

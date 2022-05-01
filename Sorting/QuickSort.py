class QuickSort:
    def sort(self, array):
        self.__sort(array, 0, len(array)-1)

    def __sort(self, array, start, end):
        if start >= end:
            return
        # Partition
        boundary = self.partition(array, start, end)
        # Sort left
        self.__sort(array, start, boundary-1)
        # Sort right
        self.__sort(array, boundary+1, end)

    def partition(self, array, start, end):
        # return index of the pivot after it moves to the correct position
        pivot = array[end]
        boundary = start-1
        for i in range(start, end+1):
            if array[i] <= pivot:
                boundary += 1
                self.swap(array, boundary, i)
        #self.swap(array, boundary+1, i)
        return boundary

    def swap(self, array, idx1, idx2):
        array[idx1], array[idx2] = array[idx2], array[idx1]

def main():
    sorter = QuickSort()
    numbers = [7, 3, 1, 4, 6, 2, 3]
    sorter.sort(numbers)
    print(numbers)
    numbers2 = [6]
    sorter.sort(numbers2)
    print(numbers2)
    numbers3 = []
    sorter.sort(numbers3)
    print(numbers3)
    numbers4 = [7, 3]
    sorter.sort(numbers4)
    print(numbers4)

if __name__ == '__main__':
    main()

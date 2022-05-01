class SelectionSort:
#    def sort(self, array):
#        for i in range(len(array)):
#            min_idx = i
#            for j in range(i, len(array)):
#                if array[min_idx] > array[j]:
#                    min_idx = j
#            self.swap(array, i, min_idx)

    def sort(self, array):
        for i in range(len(array)):
            min_idx = self.findMinIdx(array, i)
            self.swap(array, i, min_idx)

    def findMinIdx(self, array, i):
        min_idx = i
        for j in range(i, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        return min_idx

    def swap(self, array, idx1, idx2):
        array[idx1], array[idx2] = array[idx2], array[idx1]

def main():
    sorter = SelectionSort()
    numbers = [7, 3, 1, 4, 6, 2, 3]
    sorter.sort(numbers)
    print(numbers)
    numbers2 = [6]
    sorter.sort(numbers2)
    print(numbers2)
    numbers3 = []
    sorter.sort(numbers3)
    print(numbers3)

if __name__ == '__main__':
    main()

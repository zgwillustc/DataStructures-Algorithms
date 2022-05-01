class BubbleSort:
    def sort(self, array):
        for i in range(len(array)):
            isSorted =  True # Opitimization 1: if the array is sorted, stop
            for j in range(1, len(array)-i): # Optimization 2: no need to compare the sorted part and the end of the array
                if array[j] < array[j-1]:
                    self.swap(array, j, j-1)
                    isSorted = False
            if isSorted:
                return

    def swap(self, array, idx1, idx2):
        array[idx1], array[idx2] = array[idx2], array[idx1]

def main():
    sorter = BubbleSort()
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

class InsertionSort:
    def sort(self, array):
        for i in range(1, len(array)):
            current = array[i]
            j = i - 1
            while j >= 0 and array[j] > current: # Need to revisit the code
                array[j+1] = array[j]
                j -= 1
            array[j+1] = current

def main():
    sorter = InsertionSort()
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

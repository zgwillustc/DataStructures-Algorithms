class MergeSort:
    # My solution - return the sorted array
    def sortMy(self, array):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = self.sortMy(array[:middle])
        right = self.sortMy(array[middle:])
        return self.mergeMy(left, right)

    def mergeMy(self, array1, array2):
        result, l, r = [], 0, 0
        while l < len(array1) and r < len(array2):
            if array1[l] > array2[r]:
                result.append(array2[r])
                r += 1
            else:
                result.append(array1[l])
                l += 1
        if l < len(array1):
            result.extend(array1[l:])
        else:
            result.extend(array2[r:])
        return result

    # Mosh's solution - modified the orginial array, no return
    def sort(self, array):
        if len(array) < 2:
            return
        # Divide this array into half
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        # Sort each half
        self.sort(left)
        self.sort(right)
        # Merge the result
        self.merge(left, right, array)

    def merge(self, left, right, result):
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            result[k:] = left[i:]
        else:
            result[k:] = right[j:]

def main():
    sorter = MergeSort()
    numbers = [7, 3, 1, 4, 6, 2, 3]
    print(sorter.sortMy(numbers))
    numbers2 = [6]
    print(sorter.sortMy(numbers2))
    numbers3 = []
    print(sorter.sortMy(numbers3))
    numbers4 = [7, 3]
    print(sorter.sortMy(numbers4))

    sorter = MergeSort()
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

class CountingSort:
    def sort(self, array, max_val):
        counts = [0] * (max_val+1)
        for item in array:
            counts[item] += 1
        #print('Counts:', counts)

        k = 0
        for i in range(max_val+1):
            array[k:k+counts[i]+1] = [i] * counts[i]
            #print('Iteration {}'.format(i), array)
            k += counts[i]



def main():
    sorter = CountingSort()
    numbers = [7, 3, 1, 4, 6, 2, 3]
    sorter.sort(numbers, 7)
    print(numbers)
    numbers2 = [6]
    sorter.sort(numbers2, 6)
    print(numbers2)
    numbers3 = []
    sorter.sort(numbers3, 0)
    print(numbers3)
    numbers4 = [7, 3]
    sorter.sort(numbers4, 7)
    print(numbers4)

if __name__ == '__main__':
    main()

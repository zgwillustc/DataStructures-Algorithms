class BucketSort:
    def sort(self, array, numberOfBuckets = 3):
        buckets = self.createBuckets(array, numberOfBuckets)

        idx = 0
        for bucket in buckets:
            bucket.sort()
            array[idx:idx+len(bucket)+1] = bucket
            idx += len(bucket)

    def createBuckets(self, array, numberOfBuckets):
        buckets = [[] for _ in range(numberOfBuckets)]
        for item in array:
            buckets[item // numberOfBuckets].append(item)
        return buckets

def main():
    sorter = BucketSort()
    numbers = [7, 3, 1, 4, 6, 2, 3]
    sorter.sort(numbers, 4)
    print(numbers)
    numbers2 = [6]
    sorter.sort(numbers2, 3)
    print(numbers2)
    numbers3 = []
    sorter.sort(numbers3, 2)
    print(numbers3)
    numbers4 = [7, 3]
    sorter.sort(numbers4, 5)
    print(numbers4)

if __name__ == '__main__':
    main()

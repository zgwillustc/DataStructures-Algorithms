from Search import Search

nums1 = [7, 1, 3, 6, 5]
target1 = 3
search1 = Search(nums1, target1)
target2 = 4
search2 = Search(nums1, target2)

nums2 = [1, 3, 5, 6, 7]
target3 = 7
search3 = Search(nums2, target3)
nums3 = [5]
search4 = Search(nums3, target3)

print('\nCheck linear search:')
print(nums1)
print('\tIndex of {} is {}'.format(target1, search1.linearSearch()))
print('\tIndex of {} is {}'.format(target2, search2.linearSearch()))

print('\nCheck binary search using recursion:')
print(nums2)
print('\tIndex of {} is {}'.format(target3, search3.binarySearch()))
print(nums3)
print('\tIndex of {} is {}'.format(target3, search4.binarySearch()))

print('\nCheck binary search using iteration:')
print(nums2)
print('\tIndex of {} is {}'.format(target3, search3.binarySearchIter()))
print(nums3)
print('\tIndex of {} is {}'.format(target3, search4.binarySearchIter()))

print('\nCheck ternary search using recursion:')
print(nums2)
print('\tIndex of {} is {}'.format(target3, search3.ternarySearch()))
print(nums3)
print('\tIndex of {} is {}'.format(target3, search4.ternarySearch()))

print('\nCheck jump search:')
print(nums2)
print('\tIndex of {} is {}'.format(target3, search3.jumpSearchMo()))
print(nums3)
print('\tIndex of {} is {}'.format(target3, search4.jumpSearchMo()))

print('\nCheck exponential search:')
print(nums2)
print('\tIndex of {} is {}'.format(target3, search3.exponentialSearch()))
print(nums3)
print('\tIndex of {} is {}'.format(target3, search4.exponentialSearch()))

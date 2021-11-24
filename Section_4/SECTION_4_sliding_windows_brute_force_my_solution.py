# Given an array of integers of size N, find maximum sum of K consecutive  elements

# My Solution ---------------------------------------------------------------------
arr = [10, 20, 40, 49, 2390, 3290, 323409, 1, 23, 34, 234, 43, 234560, 34, 90]

k = 3
N = len(arr)
max_sum = 0

for index, element in enumerate(arr):
    temp_k = 0
    temp_sum = 0

    while temp_k < k:
        if temp_k+index < N:
            temp_sum += arr[index + temp_k]
        temp_k += 1
    max_sum = temp_sum if max_sum < temp_sum else max_sum

print(max_sum)




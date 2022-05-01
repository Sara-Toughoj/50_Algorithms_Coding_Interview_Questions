def searchForBiggestSumWithinWindow(arr, window_size):
    array_size = len(arr)
    window_sum = sum(arr[i] for i in range(window_size))
    max_sum = window_sum

    for i in range(array_size - window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(window_sum, max_sum)

    return max_sum


nums = [0, 1, 2, 4, 5, 7, 8, 9, 100, 200]

print(searchForBiggestSumWithinWindow(nums, 4))


def appendZeros(arr):
    arr_size = len(arr)
    target_array = [0]*arr_size

    pointer = 0

    for i in range(arr_size):
        if arr[i] != 0:
            target_array[pointer] = arr[i]
            pointer = pointer + 1

    return target_array


nums = [0, 1, 0, 3, 12]

print(appendZeros(nums))

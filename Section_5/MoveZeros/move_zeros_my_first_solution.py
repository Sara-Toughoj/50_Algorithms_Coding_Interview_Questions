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

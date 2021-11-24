def moveZeroes(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if (nums[j] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


array_sample = [1, 3, 6, 0, 5, 0, 0, 0, 8, 3, 5, 0, 3, 4]
print(moveZeroes(array_sample))

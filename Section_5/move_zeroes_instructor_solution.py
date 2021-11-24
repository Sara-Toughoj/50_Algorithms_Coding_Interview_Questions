# Given an array of integers , write a function to move all 0's to
# the end while maintaining the relative order of the other elements
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        array_length = len(nums)
        j = 0

        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1

        for i in range(j, array_length):
            nums[i] = 0

        return nums


array_sample = [1, 3, 6, 0, 5, 0, 0, 0, 8, 3, 5, 0, 3, 4]
print(Solution().moveZeroes(array_sample))


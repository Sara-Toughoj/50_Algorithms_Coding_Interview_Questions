# Given an array of integers of size N, find maximum sum of K consecutive  elements

# Instructor Solution (Sudo Code ) ---------------------------------------------------------------------
# Function maxSum(arr, k):
#     max_sum = NEGATIVE_INFINITY
#     n = arr.length
#     Loop as i in range 0<n-k+1
#         current_sum = 0
#         Loop as j in range 0<k:
#             current_sum += arr[i+j]
#
#         max_sum = max(current_sum , maxSum)
#     return max_sum
#

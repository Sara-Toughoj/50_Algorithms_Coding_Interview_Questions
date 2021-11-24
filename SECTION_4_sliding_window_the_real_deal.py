# Given an array of integers of size N, find maximum sum of K consecutive  elements

# (Sudo Code) ---------------------------------------------------------------------
# FUNCTION maxSum(arr , n, k):
#     window_sum = sum([arr[i] for i in range(k)])
#     max_sum = window_sum
#
#     Loop over 0<n-k with index i:
#         window_sum = window_sum - arr[i] + arr[i+k]
#         max_sum = max(max_sum , window_sum)
#
#     return max_sum
# (My Code) ---------------------------------------------------------------------

def maxSum(arr, window_size):
    arr_size = len(arr)
    window_sum = sum([arr[i] for i in range(window_size)])

    max_sum = window_sum

    for i in range(arr_size - window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(window_sum, max_sum)

    return max_sum

arr = [10, 20, 40, 49, 2390, 3290, 323409, 1, 23, 34, 234, 43, 234560, 34, 90]
k = 3
print(maxSum(arr, k))




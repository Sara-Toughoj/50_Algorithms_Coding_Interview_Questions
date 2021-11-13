
def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


arr = [1, 200, 350, 498, 590, 600, 712, 832, 956, 1075, 10000, 222222]
target = 956

result = binary_search(arr, target)
if result != -1:
    print("Element is present at middle %d" % result)
else:
    print("element is not present in the array")




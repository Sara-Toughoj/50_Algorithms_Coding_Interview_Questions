def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while right > left:
        mid = (right+left) // 2

        if target == arr[mid]:
            return mid

        if target > arr[mid]:
            left = left+1
            continue

        right = right-1

    return -1


arr = [1, 200, 350, 498, 590, 600, 712, 832, 956, 1075, 10000, 222222]
target = 956

result = binarySearch(arr, target)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("element is not present in the array")




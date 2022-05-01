def isValiMountain(arr):
    length = len(arr)

    if length < 3:
        return False

    for i in range(1, length):
        if arr[i] <= arr[i-1]:
            break

    if i == length or i ==1:
        return False

    for j in range(i-1, length-1):
        if arr[j] <= arr[j+1]:
            return False

    return True


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(isValiMountain(numbers))

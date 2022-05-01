def isValiMountain(arr):
    array_length = (len(arr))
    i = 1
        
    while i < array_length and arr[i] > arr[i-1]:
        i += 1
            
    if i == 1 or i == array_length:
        return 0
        
    while i < array_length and arr[i] < arr[i-1]:
        i += 1
        
    return i == array_length


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(isValiMountain(numbers))

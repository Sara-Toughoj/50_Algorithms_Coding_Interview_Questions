def containerWithMostWater(heights):
    left = 0
    right = len(heights) - 1
    max_water = 0

    while right > left:
        width = right - left
        height = min(heights[right], heights[left])
        container_space = width * height

        max_water = max(max_water, container_space)

        if height == heights[left]:
            left += 1
        else:
            right -= 1

    return max_water


heights_arr = [2,3,4,5,18,17,6]
print(containerWithMostWater(heights_arr))

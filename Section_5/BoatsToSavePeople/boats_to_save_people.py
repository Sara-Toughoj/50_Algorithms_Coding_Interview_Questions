# You are trying to add people in safety boats ,
# given an array people and an integer limit ,
# people array is an integer array of people's weights ,
# i-th pearson has a weight people[i] and each boat can carry at most limit,
# Each boat carries at most 2 people at the same time ,
# given that their weight is at most limit.
# Return the minimum number of boats to carry every given person .
# Note : It is guaranteed each person can be carried by a boat.

def minimumBoats(people, limit):
    people.sort()
    left = boats = 0
    right = (len(people)) - 1

    while left <= right:
        boats += 1
        if people[left] + people[right] > limit:
            right -= 1
            continue

        right -= 1
        left += 1

    return boats


weights = [1, 2]
print(minimumBoats(weights, 3))









































def minimumBoats(people, limit):
    people.sort()
    left_pointer = 0
    right_pointer = (len(people))-1
    boats_count = 0

    while left_pointer <= right_pointer:
        if people[left_pointer] + people[right_pointer] <= limit:
            left_pointer += 1

        right_pointer -= 1
        boats_count += 1

    return boats_count


limit = 3
people = [1, 3, 2, 2, 1, 1, 1, 1, 3, 2, 1, 2, 3, 1, 2, 2, 2, 3, 3, 1, 2]
print(minimumBoats(people, limit))

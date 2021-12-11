# You are trying to add people in safety boats ,
# given an array people and an integer limit ,
# people array is an integer array of people's weights ,
# i-th pearson has a weight people[i] and each boat can carry at most limit,
# Each boat carries at most 2 people at the same time ,
# given that their weight is at most limit.
# Return the minimum number of boats to carry every given person .
# Note : It is guaranteed each person can be carried by a boat.

def minimumBoats( people , limit):
    saved_people = 0
    number_of_boats = 0

    for index, i in enumerate(people):
        if i == -1:
            next()

        if i == limit:
            number_of_boats += 1
            next()






limit = 3
people = [1, 3, 2, 2, 1, 1, 1, 1, 3, 2, 1, 2, 3, 1, 2, 2, 2, 3, 3, 1, 2]
print(minimumBoats(people, limit))

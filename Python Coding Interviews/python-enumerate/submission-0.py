from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i,n in enumerate(nums):
        if n == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    i1 = None
    i2 = None
    for i, n in enumerate(nums):
        if n == 7:
            if i1 is None:
                i1 = i
                continue
            if i2 is None:
                i2 = i
                return i2 - i1
    return -1



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

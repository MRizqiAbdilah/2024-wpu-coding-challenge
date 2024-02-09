# WPU Coding Challenge 2024
# 9/366
# https://www.codewars.com/kata/577a98a6ae28071780000989


# way 1
def minimum(arr: list) -> int:
    return min(arr)


def maximum(arr: list) -> int:
    return max(arr)


# way 2

minimum = lambda arr: min(arr)
maximum = lambda arr: max(arr)

# way 3
minimum, maximum = lambda arr: min(arr), lambda arr: max(arr)

# way 4
minimum, maximum = min, max

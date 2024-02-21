# WPU Coding Challenge 2024
# 15/366
# https://www.codewars.com/kata/576b93db1129fcf2200001e6

# way 1
def sum_array(array):
    if array:
        sort = sorted(array)
        return sum(sort[1:-1])
    else:
        return 0

# way 2
def sum_array(array):
    return (sum(sorted(array)[1:-1])) if array else 0

# way 3
sum_array = lambda arr: sum(sorted(arr)[1:-1]) if arr else 0

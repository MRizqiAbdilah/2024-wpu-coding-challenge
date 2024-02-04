# WPU Coding Challenge 2024
# 1/366
# https://www.codewars.com/kata/57f780909f7e8e3183000078

# way 1
def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result


from math import prod

# way 2
def grow(arr):
    return prod(arr)

# way 3
grow = lambda arr: prod(arr)


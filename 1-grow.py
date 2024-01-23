# def grow(arr):
#     result = 1
#     for i in arr:
#         result *= i
#     return result


from math import prod

# def grow(arr):
#     return prod(arr)

grow = lambda arr: prod(arr)

print(grow([4, 1, 1, 1, 4]))


# WPU Coding Challenge 2024
# 19/366
# https://www.codewars.com/kata/57eaeb9578748ff92a000009

# way 1
def sum_mix(arr):
    result = []
    for i in arr:
        result.append(int(i))
    return sum(result) 

# way 2
def sum_mix(arr):
    return sum(int(i) for i in arr)

# way 3
sum_mix = lambda arr: sum(int(i) for i in arr)

# way 4
sum_mix = lambda arr: sum(map(int, arr))


print(sum_mix([1,2,"10", "20"]))

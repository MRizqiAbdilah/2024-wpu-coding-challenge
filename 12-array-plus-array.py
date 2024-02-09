# WPU Coding Challenge 2024
# 12/366
# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151

# way 1
def array_plus_array(arr1, arr2):
    result = 0
    for i in arr1:
        result += i
    for i in arr2:
        result += i
    return result

# way 2
def array_plus_array(arr1, arr2):
    result = 0
    for i in arr1 + arr2:
        result += i
    return result


# way 3
def array_plus_array(arr1, arr2):
    return sum(arr1 + arr2)


# way 4
array_plus_array = lambda arr1, arr2: sum(arr1 + arr2)




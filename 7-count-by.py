# WPU Coding Challenge 2024
# 7/366
# https://www.codewars.com/kata/5513795bd3fafb56c200049e

# way 1
def count_by(x, n):
    count = []
    for i in range(1, n + 1):
        counter = x * i
        count.append(counter)
    return count

# way 2
def count_by(x,n):
    return [i * x for i in range(1, n + 1)]

# way 3
count_by = lambda x, n: [i * x for i in range(1, n + 1)]

# way 4
count_by = lambda x, n: list(range(x, n * x + 1, x))

print(count_by(2,5))
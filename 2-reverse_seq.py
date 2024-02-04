# WPU Coding Challenge 2024
# 2/366
# https://www.codewars.com/kata/5a00e05cc374cb34d100000d

# check way
list = [n - 1 for n in range(1, 5)]
list.reverse()
print(list)
list.reverse()
for i in range(1, 5):
    list.append(i)
print(list)

# way 1
def reverse_seq(n):
    n = n + 1
    n_list = [n for n in range(1, n)]
    n_list.reverse()
    return n_list

# way 2
reverse_seq = lambda n: [n for n in range(1, n + 1)][::-1]

# way 3
reverse_seq = lambda n: list(range(n, 0, -1))


# WPU Coding Challenge 2024
# 8/366
# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077


# way 1
def count_sheep(n):
    sheep = ""
    if n != 0:
        for i in range(1, n + 1):
            sheep += f"{i} sheep..."

    return sheep


# way 2
def count_sheep(n):
    return "".join([f"{i} sheep..." if n != 0 else "" for i in range(1, n + 1)])


# way 3
count_sheep = lambda n: "".join(
    [f"{i} sheep..." if n != 0 else "" for i in range(1, n + 1)]
)

# way 4
count_sheep = lambda n: "".join([f"{i} sheep..." for i in range(1, n + 1)])

# way 5
count_sheep = lambda n: "".join(["{} sheep...".format(i) for i in range(1, n + 1)])

print(count_sheep(10))

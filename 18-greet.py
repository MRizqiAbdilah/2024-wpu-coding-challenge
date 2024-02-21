# WPU Coding Challenge 2024
# 18/366
# https://www.codewars.com/kata/5772da22b89313a4d50012f7

# way 1
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

# way 2
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

# way 3
greet = lambda name, owner: "Hello boss" if name == owner else "Hello guest"

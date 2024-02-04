# WPU Coding Challenge 2024
# 2/366
# https://www.codewars.com/kata/59ca8246d751df55cc00014c


# way 1
def hero(bullets, dragons):
    return True if dragons <= bullets / 2 else False


# way 2
hero = lambda bullets, dragons: True if dragons <= bullets / 2 else False

# way 3
hero = lambda b, d: d <= b / 2

# way 4
hero = lambda b, d: b // d > 1


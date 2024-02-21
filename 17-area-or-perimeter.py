# WPU Coding Challenge 2024
# 17/366
# https://www.codewars.com/kata/5ab6538b379d20ad880000ab

def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else: 
        return 2 * (l + w)

def area_or_perimeter(l,w):
    return l * w if l == w else 2 * (l + w )


area_or_perimeter = lambda l, w: l * w if l == w else 2 * (l + w)

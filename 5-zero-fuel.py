# WPU Coding Challenge 2024
# 5/366
# https://www.codewars.com/kata/5861d28f124b35723e00005e


# way 1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False


# way 2
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False


# way 3

zero_fuel = lambda distance_to_pump, mpg, fuel_left: mpg * fuel_left >= distance_to_pump

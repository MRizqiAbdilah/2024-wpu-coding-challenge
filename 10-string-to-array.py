# WPU Coding Challenge 2024
# 10/366
# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

# way 1
def string_to_array(s):
    string_array = []
    if s == "":
        string_array.append("")
    else:
        string_array = s.split()
    return string_array

# way 2
def string_to_array(s):
    return s.split(" ")

# way 3
string_to_array = lambda s: s.split(" ")

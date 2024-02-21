# WPU Coding Challenge 2024
# 16/366
# https://www.codewars.com/kata/563e320cee5dddcf77000158

# way 1
def get_average(marks):
    count = 0
    for i in marks:
        count += i
    return count // len(marks)

# way 2
def get_average(marks):
    return sum(marks) // len(marks)

# way 3
get_average = lambda marks: sum(marks) // len(marks)

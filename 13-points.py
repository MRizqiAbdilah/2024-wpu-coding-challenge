# WPU Coding Challenge 2024
# 13/366
# https://www.codewars.com/kata/5bb904724c47249b10000131


# # way 1
def points(games):
    score = 0
    for i in games:
        if i[0] > i[2]:
            score += 3
        elif i[0] == i[2]:
            score += 1
    return score


# way 2
def points(games):
    return sum(
        [
            3 if i[0] > i[2] else 1 if i[0] == i[2] else 0 if i[0] < i[2] else i
            for i in games
        ]
    )


# way 3
points = lambda games: sum(
    [
        3 if i[0] > i[2] else 1 if i[0] == i[2] else 0 if i[0] < i[2] else i
        for i in games
    ]
)

# way 4
points = lambda games: sum(
    [3 if i[0] > i[2] else 1 if i[0] == i[2] else 0 for i in games]
)

def points(games):
    # x >= y -> hasilnya bisa 0 atau 1
    # jika x == y, maka 0,
    # jika x > y, maka 1
    # (x >= y) + 2 * (x > y) -> prioritaskan perkalian dulu
    #  1 + 2 * 1 = 3 -> ketika x lebih besar dari y
    #  1 = 2 * 0 = 1 -> Ketika x sama dengan y
    #  0 + 2 * 0 = 0 -> ketika x lebih kecil dari y
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in games))

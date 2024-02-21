# WPU Coding Challenge 2024
# 14/366
# https://www.codewars.com/kata/55cbd4ba903825f7970000f5


# way 1
def get_grade(s1, s2, s3):
    result = (s1 + s2 + s3) / 3
    if result >= 90 and result <= 100:
        return "A"
    elif result >= 80 and result < 90:
        return "B"
    elif result >= 70 and result < 80:
        return "C"
    elif result >= 60 and result < 70:
        return "D"
    else:
        return "F"


# way 2
def get_grade(s1, s2, s3):
    result = (s1 + s2 + s3) / 3
    return "".join(
        [
            (
                "A"
                if result >= 90 and result <= 100
                else (
                    "B"
                    if result >= 80
                    else "C" if result >= 70 else "D" if result >= 60 else "F"
                )
            )
        ]
    )


# way 3
def get_grade(s1, s2, s3):
    """
    (s := sum(s1 + s2+ s3) / 3) -> assignment expression atau walrus operator yang diperkenalkan dalam Python 3.8.
    Assignment expression memungkinkan kita untuk menggabungkan operasi pengisian nilai variabel dengan ekspresi lain dalam satu baris.
    Keuntungan:
    Penggunaan assignment expression memungkinkan kita menghindari pengulangan perhitungan yang sama.
    Lebih ringkas dan memperpendek kode, terutama dalam situasi di mana kita ingin menggabungkan inisialisasi variabel dengan ekspresi lain.
    """
    return (
        "A"
        if (s := (s1 + s2 + s3) / 3) >= 90 and s <= 100
        else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F"
    )


# way 4
get_grade = lambda s1, s2, s3: (
    "A"
    if (s := (s1 + s2 + s3) / 3) >= 90 and s <= 100
    else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F"
)


def get_grade(*scores):
    return {6: "D", 7: "C", 8: "B", 9: "A", 10: "A"}.get(
        (sum(scores) / len(scores)) // 10, "F"
    )

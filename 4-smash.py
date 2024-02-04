# WPU Coding Challenge 2024
# 4/366
# https://www.codewars.com/kata/53dc23c68a0c93699800041d

# check away
array = ["Hello", "World"]
print(len(array))


def smash(words: list) -> str:
    result = ""
    for i in range(len(words)):
        result += words[i]
        result += " "
    return result


print(smash(["Hallo", "Nama", "Saya", "Muhammad", "Rizqi", "Abdilah"]))


# way 1
def smash(words):
    join_words = " ".join(words)
    return join_words


# way 2
def smash(words):
    return " ".join(words)


# way 3
smash = lambda words: " ".join(words)

# WPU Coding Challenge 2024
# 6/366
# https://www.codewars.com/kata/5556282156230d0e5e000089

# check way
word = "ASEPT"
print(word.split())
for i in word:
    if i == "T":
        i = "U"
    print(i)

word = "banana"
print("".join(["u" if i == "a" else "b" for i in word]))


#  way 1
def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i == "T":
            rna += "U"
        else:
            rna += i
    return rna


# way 2
def dna_to_rna(dna):
    return "".join(["U" if rna == "T" else rna for rna in dna])


# way 3
dna_to_rna = lambda dna: "".join(["U" if rna == "T" else rna for rna in dna])

# way 4
dna_to_rna = lambda dna: dna.replace("T", "U")

# way 5
dna_to_rna = lambda dna: "U".join(dna.split("T"))

print(dna_to_rna("TTTT"))

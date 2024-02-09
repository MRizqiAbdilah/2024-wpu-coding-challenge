# WPU Coding Challenge 2024
# 11/366
# https://www.codewars.com/kata/5672a98bdbdd995fad00000f


# way 1
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    else:
        return "Player 2 won!"


# way 2
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (
        p1 == "rock"
        and p2 == "scissors"
        or p1 == "paper"
        and p2 == "rock"
        or p1 == "scissors"
        and p2 == "paper"
    ):
        return "Player 1 won!"
    else:
        return "Player 2 won!"


# way 3
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    return (
        "Player 1 won!"
        if p1 == "rock"
        and p2 == "scissors"
        or p1 == "paper"
        and p2 == "rock"
        or p1 == "scissors"
        and p2 == "paper"
        else "Player 2 won!" "Draw!" if p1 == p2 else ""
    )


# way 4
def rps(p1, p2):
    return (
        "Player 1 won!"
        if p1 == "rock"
        and p2 == "scissors"
        or p1 == "paper"
        and p2 == "rock"
        or p1 == "scissors"
        and p2 == "paper"
        else "Player 2 won!" if p1 != p2 else "Draw!"
    )


# way 5
rps = lambda p1, p2: (
    "Player 1 won!"
    if p1 == "rock"
    and p2 == "scissors"
    or p1 == "paper"
    and p2 == "rock"
    or p1 == "scissors"
    and p2 == "paper"
    else "Player 2 won!" if p1 != p2 else "Draw!"
)

# way 6
def rps(p1, p2):
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "Draw!" if p1 == p2 else f"Player {'1' if rules[p1] == p2 else '2'} won!"

# way 7
def rps(p1, p2):
    return (
        "Draw!"
        if p1 == p2
        else f"Player {'1' if {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}[p1] == p2 else '2'} won!"
    )

# way 8
rps = lambda p1, p2:"Draw!" if p1 == p2 else f"Player {'1' if {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}[p1] == p2 else '2'} won!"



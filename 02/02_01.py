sum_score = 0
# Opp_Selection A=Rock, B=Paper, C=Scissors
# Own_selection X=Rock, Y=Paper, Z=Scissors

opp_selection = {"A": 1, "B": 2, "C": 3}
own_selection = {"X": 1, "Y": 2, "Z": 3}

# győzelem: 1 3, 2 1, 3 2

with open("input.txt", "r") as f:
    for x in f:
        # print(opp_selection[x.strip()[0]])
        sum_score += own_selection[x.strip()[2]]
        result = own_selection[x.strip()[2]] - opp_selection[x.strip()[0]]
        if  result == -2 or result == 1:
            sum_score += 6
        elif result == 0:
            sum_score += 3

print(sum_score)
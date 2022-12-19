sum_score = 0
# Opp_Selection A=Rock, B=Paper, C=Scissors
# Own_selection X=Rock, Y=Paper, Z=Scissors

selection = {"A": 1, "B": 2, "C": 3}
result = {"X": 0, "Y": 3, "Z": 6}

# győzelem: 1 3, 2 1, 3 2

with open("input.txt", "r") as f:
    for x in f:
        opp_selection = selection[x.strip()[0]]
        sum_score += result[x.strip()[2]]
        if x.strip()[2] == "X":  # Lose
            own_selection = list(selection.values())[opp_selection - 2]
            sum_score += own_selection
        elif x.strip()[2] == "Y":  # Tie
            sum_score += opp_selection
        else:  # Wi
            if opp_selection == 3:
                opp_selection = 0
            own_selection = list(selection.values())[opp_selection]
            sum_score += own_selection

print(sum_score)
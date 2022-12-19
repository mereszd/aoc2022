current_calories = 0
max_calories = [0, 0, 0]

with open("input.txt", "r") as f:
    for x in f:
        if x == '\n':
            if current_calories > max_calories[0]:
                max_calories[0] = current_calories
                max_calories.sort()
            current_calories = 0
        else:
            current_calories += int(x.strip())

if current_calories > max_calories[0]:
    max_calories[0] = current_calories
    max_calories.sort()

print(max_calories[0] + max_calories[1] + max_calories[2])
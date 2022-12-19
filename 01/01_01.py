current_calories = 0
max_calories = 0

with open("input.txt", "r") as f:
    for x in f:
        if x == '\n':
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(x.strip())

if current_calories > max_calories:
    max_calories = current_calories

print(max_calories)
sum = 0
counter = 0
rucksacks = ["", "", ""]

with open("input.txt", "r") as f:
    for x in f:
        if counter == 3:
            counter = 0
        rucksacks[counter] = x.strip()
        if counter == 2:
            first_set = set(rucksacks[0])
            second_set = set(rucksacks[1])
            third_set = set(rucksacks[2])
            intersect_temp = first_set.intersection(second_set)
            intersect = intersect_temp.intersection(third_set)
            intersect = str(intersect)[2]
            if intersect.isupper():
                value = ord(intersect) - ord('A') + 27
            else:
                value = ord(intersect) - ord('a') + 1
            sum += value
        counter += 1

print(sum)



# print(ord('a'))
# print(ord('B')-ord('A'))
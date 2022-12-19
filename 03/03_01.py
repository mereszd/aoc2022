sum = 0

with open("input.txt", "r") as f:
    for x in f:
        half = int(len(x)/2)
        first_half = x.strip()[0:half]
        second_half = x.strip()[half:len(x)]
        first_set = set(first_half)
        second_set = set(second_half)
        intersect = first_set.intersection(second_set)
        intersect = str(intersect)[2]
        if intersect.isupper():
            value = ord(intersect) - ord('A') + 27
        else:
            value = ord(intersect) - ord('a') + 1
        sum += value

print(sum)



# print(ord('a'))
# print(ord('B')-ord('A'))
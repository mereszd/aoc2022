sum = 0

with open("input.txt", "r") as f:
    for x in f:
        first_range, second_range = x.strip().split(',')
        f_s, f_e = first_range.split('-')
        s_s, s_e = second_range.split('-')
        first_set = set()
        second_set = set()
        for x in range(int(f_s), int(f_e)+1):
            first_set.add(x)
        for x in range(int(s_s), int(s_e)+1):
            second_set.add(x)

        if len(first_set.intersection(second_set)) > 0:
            sum += 1

print(sum)
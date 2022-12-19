sum = 0

with open("input.txt", "r") as f:
    for x in f:
        first_range, second_range = x.strip().split(',')
        f_s, f_e = first_range.split('-')
        s_s, s_e = second_range.split('-')
        if int(f_s) <= int(s_s) and int(f_e) >= int(s_e):
            sum += 1
        elif int(s_s) <= int(f_s) and int(s_e) >= int(f_e):
            sum += 1
print(sum)
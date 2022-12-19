phase = 'build'
stacks = [ [] for i in range(10)]  # [0] will be empty, so it's easier to manipulate 1-9

with open("input.txt", "r") as f:
    for x in f:
        if x == '\n':
            phase = 'orders'
            continue
        if phase == 'build':
            raw_crates = x
            if raw_crates[1] == '1':  # need to test for [0] because of the strip
                continue
            for i in range(9):
                if len(raw_crates) < 1+i*4:
                    continue
                if raw_crates[1+i*4] != " ":
                    stacks[i+1].append(raw_crates[1+i*4])
        if phase == 'orders':
            raw_order = x.strip().split(' ')
            move = int(raw_order[1])
            from_s = int(raw_order[3])
            to_s = int(raw_order[5])
            temp_list = []
            for i in range(move):
                popped = stacks[from_s].pop(0)
                temp_list.append(popped)
            for i in range(len(temp_list)):
                popped = temp_list.pop()
                stacks[to_s].insert(0, popped)

answer = ''
for stack in stacks:
    if stack == []:
        continue
    answer += stack[0]
print(answer)


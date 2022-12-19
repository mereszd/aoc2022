data_buffer = []

with open("input.txt", "r") as f:
    for x in f:
        datastream = x

for i in range(len(datastream)):
    if len(data_buffer) == 14:
        data_buffer.pop(0)
    data_buffer.append(datastream[i])
    data_set = set(data_buffer)
    if len(data_set) == 14:
        print("Found a unique number", data_set)
        print("The number is ", i+1)
        break
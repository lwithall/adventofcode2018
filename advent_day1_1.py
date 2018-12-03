frequency = 0

with open("input.txt") as f:
    for line in f:
        if line[0] == '-':
            frequency -= int(line[1:])
        else:
            frequency += int(line[1:])

print(frequency)

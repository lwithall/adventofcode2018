frequency = 0

found = False
seen = set()

while not found:
    with open("input.txt") as f:
        for line in f:
            seen.add(frequency)
            if line[0] == '-':
                frequency -= int(line[1:])
            else:
                frequency += int(line[1:])
                
            if frequency in seen:
                print(frequency)
                found = True
                break



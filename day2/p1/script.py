frequency = 0

with open("input.txt") as f:
    count2 = 0
    count3 = 0
    for line in f:
        m = {}
        for c in line:
            if c in m:
                m[c] = m[c] + 1
            else:
                m[c] = 1

        for _, v in m.items():
            if v == 2:
                count2 += 1
                break
        for _, v in m.items():
            if v == 3:
                count3 += 1
                break

print(count2 * count3)

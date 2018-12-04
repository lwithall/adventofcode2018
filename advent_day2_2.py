
def difference(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return False, []

    count = 0
    same = ""
    for i in range(0, len(s2)):
        if s1[i] != s2[i]:
            count += 1
        else:
            same += s1[i]
        if count > 1:
            return False, []
    return count == 1, same

def find(elements):
    for i in range(0, len(elements)):
        for j in range(i + 1, len(elements)):
            match, same = difference(elements[i], elements[j])
            if match:
                print(elements[i])
                print(elements[j])
                print(same)
                return

with open("input.txt") as f:
    elements = []
    for line in f:
        elements.append(line)

    find(elements)

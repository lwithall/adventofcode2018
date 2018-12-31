
def get_options():
    options = []
    for i in range(ord('a'), ord('z')+1):
        options.append(chr(i) + chr(i-32))
        options.append(chr(i-32) + chr(i))
    return options

with open("../input.txt") as f:

    block = f.read().splitlines()[0]

    options = get_options()

    applied = True
    while applied:
        applied = False

        prev = len(block)
        for option in options:
            block = block.replace(option, "")

        if prev > len(block):
            applied = True

    print(len(block))
    #print(count)

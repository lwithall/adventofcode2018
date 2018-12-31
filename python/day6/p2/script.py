
def get_options():
    options = []
    for i in range(ord('a'), ord('z')+1):
        options.append(chr(i) + chr(i-32))
        options.append(chr(i-32) + chr(i))
    return options

def get_length(options, block, i):

    block = block.replace(chr(i), '')
    block = block.replace(chr(i-32), '')

    applied = True
    while applied:
        applied = False

        prev = len(block)
        for option in options:
            block = block.replace(option, "")

        if prev > len(block):
            applied = True

    return len(block)

with open("../input.txt") as f:

    block = f.read().splitlines()[0]

    l = get_length(get_options(), block, ord('a'))

    for i in range(ord('b'), ord('z')+1):
        l = min(l, get_length(get_options(), block, i))

    print(l)

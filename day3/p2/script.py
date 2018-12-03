
def get_xy(str):
    #265,241:
    s = str.split(",")
    return int(s[0]), int(s[1][:len(s[1])-1])


def get_wh(str):
    #16x26
    s = str.split("x")
    return int(s[0]), int(s[1])


def get_elements(line):
    # #1 @ 265,241: 16x26
    s = line.split(" ")
    x, y = get_xy(s[2])
    width, height = get_wh(s[3])
    return x, y, width, height

class Square:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, line):
        self.x, self.y, self.width, self.height = get_elements(line)

with open("input.txt") as f:
    squares = []
    for line in f:
        squares.append(Square(line))

    width = squares[0].x + squares[0].width
    height = squares[0].y + squares[0].height

    for s in squares:
        width = max(width, s.x + s.width)
        height = max(height, s.y + s.height)

    m = []
    for i in range(0, width):
        m.append([0] * height)

    for s in range(0, len(squares)):
        square = squares[s]
        for i in range(square.x, square.x + square.width):
            for j in range(square.y, square.y + square.height):
                m[i][j] += 1

    count = 0
    for s in range(0, len(squares)):
        square = squares[s]
        all_one = True
        for i in range(square.x, square.x + square.width):
            for j in range(square.y, square.y + square.height):
                if m[i][j] != 1:
                    all_one = False
        if all_one:
            print(s+1)

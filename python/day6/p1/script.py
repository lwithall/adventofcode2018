
def get_min(point, points):

    x_min = (None, None)
    y_min = (None, None)
    x_max = (None, None)
    y_max = (None, None)

    for p in points:
        if p[0] < point[0] and x_min[0] is None or p[0] < x_min[0]:
            x_min = p
        if p[0] > point[0] and x_max[0] is None or p[0] > x_min[0]:
            x_max = p
        if p[1] < point[1] and y_min[1] is None or p[1] < y_min[1]:
            y_min = p
        if p[1] > point[1] and y_max[1] is None or p[1] > y_min[1]:
            y_max = p

    return x_min, y_min, x_max, y_max


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def get_size(point, x_min, y_min, x_max, y_max):

    print(x_min, y_min, x_max, y_max)

    largest = 0
    for i in range(x_min[0], x_max[0]):
        for j in range(y_min[0], y_max[0]):
            pt = (i, j)
            dist = distance(point, pt)
            if distance(y_min, pt) > dist and distance(y_max, pt) > dist and distance(x_min, pt) > dist and distance(x_max, pt) > dist:
                largest += 1
    return largest

with open("../input.txt") as f:

    points = []
    for line in f:
        elements = line.split(', ')
        points.append((int(elements[0]), int(elements[1])))

    largest = 0

    for point in points:
        x_min, y_min, x_max, y_max = get_min(point, points)

        if x_min[0] is None or x_max[0] is None or y_max[1] is None or y_min[1] is None:
            print("Skipping " + str(point))
            continue
        print(point)
        print(x_min, x_max, y_min, y_max)
        size = get_size(point, x_min, y_min, x_max, y_max)
        print(size)
        largest = max(largest, size)

    print(largest)

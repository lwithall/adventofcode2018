
import operator

elements_upper = "ABCDEFGHIJKLMNOP"
elements = "abcdefghijklmnop"

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def getClosest(x, y, points):
    distances = [(dist(x, y, points[i][0], points[i][1]), i) for i in range(len(points))]
    sorted_distances = sorted(distances, key=lambda x: x[0])

    if sorted_distances[0][0] == sorted_distances[1][0]:
        return -1
    return sorted_distances[0][1]

with open("../input.txt") as f:

    # Load points
    points = []
    for line in f:
        l = line.split(', ')
        points.append((int(l[0]), int(l[1])))

    x_min = points[0][0]
    x_max = points[0][0]
    y_min = points[0][1]
    y_max = points[0][1]
    for p in points:
        x_min = min(x_min, p[0])
        x_max = max(x_max, p[0])
        y_min = min(y_min, p[1])
        y_max = max(y_max, p[1])

    counts = {}
    for point in range(len(points)):
        counts[point] = 0

    lines = []
    for y in range(y_min-1, y_max+1):
        line = str(y) + ' '
        for x in range(x_min-1, x_max+1):
            i = getClosest(x, y, points)
            if i != -1:
                counts[i] += 1

    def isFinite(point):
        return x_min < point[0] < x_max and y_min < point[1] < y_max

    max_area = -1
    for c in range(len(counts)):
        if isFinite(points[c]):
            max_area = max(max_area, counts[c])
    print(counts)
    print(max_area)

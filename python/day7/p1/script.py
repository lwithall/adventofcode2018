
from string import ascii_uppercase
import re

def parse_line(line):
    reg = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."
    m = re.match(reg, line)

    return m.group(1), m.group(2)

def get_roots(nodes):
    return [n for n in sorted(nodes.keys()) if nodes[n].parent is None]

class Node:

    def __init__(self, c):
        self.c = c
        self.children = []
        self.seen = False
        self.parent = None

    def get_next(self, nodes):
        return [d for d in sorted(self.children) if not nodes[d].seen]

nodes = {}
for c in ascii_uppercase:
    nodes[c] = Node(c)

result = ''

with open("../input.txt") as f:

    for line in f:
        first, second = parse_line(line)

        nodes[first].children.append(second)
        nodes[second].parent = first

    queue = get_roots(nodes)
    while queue:
        c = queue.pop(0)
        if not nodes[c].seen:
            nodes[c].seen = True
            result += c
            for node in nodes[c].get_next(nodes):
                queue.append(node)

print result

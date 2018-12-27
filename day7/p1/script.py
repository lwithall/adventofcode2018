
from string import ascii_uppercase
import re

def parse_line(line):
    reg = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."
    m = re.match(reg, line)

    return m.group(1), m.group(2)

def get_roots(nodes):
    return [nodes[n] for n in nodes if not nodes[n].deps]

class Node:

    def __init__(self, c):
        self.c = c
        self.deps = []
        self.seen = False

    def get_next(self, nodes):
        return [nodes[d] for d in self.deps if not nodes[d].seen]

nodes = {}
for c in ascii_uppercase:
    nodes[c] = Node(c)

result = ''

with open("../input.txt") as f:

    for line in f:
        first, second = parse_line(line)

        nodes[second].deps.append(first)

    queue = get_roots(nodes)
    while queue:
        node = queue.pop(0)
        print(node.c)
        node.seen = True
        result += node.c
        for node in node.get_next(nodes):
            queue.append(node)

print result

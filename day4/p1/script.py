import re

# year-month-day hour:minute
# 1 = year, 2 = month, 3 = day
# 4 = hour, 5 = minute
# [1518-10-28 00:01]
date = "\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] "

# 6 = id
# [1518-10-28 00:01] Guard #2011 begins shift
begins = re.compile(date + "Guard \#(\d+) begins shift")
# [1518-10-28 00:01] wakes up
starts = re.compile(date + "falls asleep")
# [1518-10-28 00:01] falls asleep
ends = re.compile(date + "wakes up")

class Date:
    def __init__(self, match):
        self.year   = int(match.group(1))
        self.month  = int(match.group(2))
        self.day    = int(match.group(3))
        self.hour   = int(match.group(4))
        self.minute = int(match.group(5))

    def __str__(self):
        return "[" + str(self.year) + "-" + str(self.month) + "-" + str(self.day)\
                + " " + str(self.hour) + ":" + str(self.minute) + "]"

    def __repr__(self):
        return str(self)

class Guard:
    def __init__(self, id):
        self.id = id
        self.times = []

    def get_num_minutes(self):
        total = 0
        for start, end in self.times:
            for i in range(start.minute, end.minute):
                total += 1
        return total

    def get_minute(self):

        list = [0] * 59

        for start, end in self.times:
            print(str(start) + " to " + str(end))
            for i in range(start.minute, end.minute):
                list[i] += 1

        minute, index = list[0], 0
        for i in range(1, len(list)):
            if list[i] > minute:
                minute = list[i]
                index = i
        return index

    def add_sleep(self, start, end):
        assert(start is not None)
        assert(end is not None)
        self.times.append((start, end))

    def __lt__(self, other):
        return self.get_num_minutes() < other.get_num_minutes()

    def __eq__(self, other):
        return self.get_num_minutes() == other.get_num_minutes()

    def __str__(self):
        return str(self.id) + " for a total of " + str(self.get_num_minutes())

    def __repr__(self):
        return str(self)

def get_guard(id, guards):
    if id not in guards:
        guards[id] = Guard(id)
    return guards[id]

with open("../input.txt") as f:

    lines = []
    for line in f:
        lines.append(line)

    guards = {}
    guard = None
    start = None

    lines = sorted(lines)

    for line in lines:
        print(line)
        match = begins.match(line)
        if match is not None:
            id = match.group(6)
            guard = get_guard(id, guards)
        else:
            match = starts.match(line)
            if match is not None:
                start = Date(match)
            else:
                match = ends.match(line)
                if match is not None:
                    guard.add_sleep(start, Date(match))
                    start = None
                else:
                    print("ERROR")

    guards = sorted(guards.values())

    print(guards)

    print(guards[-1].id)
    print(guards[-1].get_minute())
    print(int(guards[-1].id)*int(guards[-1].get_minute()))

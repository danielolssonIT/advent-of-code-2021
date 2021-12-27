import re
from collections import Counter


def parse_input(example):
    filename = "ex.txt" if example else "input.txt"
    steps = []
    pattern = re.compile("([^\s]+) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)")
    with open(filename) as f:
        for line in f:
            match = pattern.search(line)
            if match:
                groups = match.groups()
                steps.append((groups[0], *map(int, groups[1:])))
    return steps


def solve_part1(example=False):
    steps = parse_input(example)
    cuboids = set()
    for cmd, xmin, xmax, ymin, ymax, zmin, zmax in steps:
        for i in range(max(xmin, -50), min(50, xmax + 1)):
            for j in range(max(ymin, -50), min(50, ymax + 1)):
                for k in range(max(zmin, -50), min(50, zmax + 1)):
                    if cmd == "on":
                        cuboids.add((i, j, k))
                    else:
                        if (i, j, k) in cuboids:
                            cuboids.remove((i, j, k))
    return len(cuboids)


def solve_part2(example=False):
    steps = parse_input(example)
    cuboids = Counter()
    for cmd, x1, x2, y1, y2, z1, z2 in steps:
        update = Counter()
        sign = 1 if cmd == "on" else -1
        for (ex1, ex2, ey1, ey2, ez1, ez2), count in cuboids.items():
            interval_x1, interval_x2 = max(x1, ex1), min(x2, ex2)
            interval_y1, interval_y2 = max(y1, ey1), min(y2, ey2)
            interval_z1, interval_z2 = max(z1, ez1), min(z2, ez2)
            if interval_x1 <= interval_x2 and interval_y1 <= interval_y2 and interval_z1 <= interval_z2:
                update[
                    (interval_x1, interval_x2, interval_y1, interval_y2, interval_z1, interval_z2)
                ] -= count
        if sign == 1:
            update[(x1, x2, y1, y2, z1, z2)] += sign
        cuboids.update(update)
    return sum(
        (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * sign for (x1, x2, y1, y2, z1, z2), sign in cuboids.items())


# print(solve_part1())
print(solve_part2())
# print(overlap_cuboids(a1, a2, b1, b2))

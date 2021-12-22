import re


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


print(solve_part1())

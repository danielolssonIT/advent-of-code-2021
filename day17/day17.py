import re


def parse_input(example=False):
    filename = "example.txt" if example else "day17.txt"
    with open(filename) as f:
        line = f.read().strip()
    pattern = re.compile("target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)")
    res = pattern.search(line)
    if res:
        return res.groups()
    return None


def solve_part1(example=False):
    min_x, max_x, min_y, max_y = parse_input(example)

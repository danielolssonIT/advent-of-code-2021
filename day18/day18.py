import ast
import functools
import itertools
import math


def add_leftmost(sn, rn):
    if rn is None:
        return sn
    if isinstance(sn, int):
        return sn + rn
    return [add_leftmost(sn[0], rn), sn[1]]


def add_rightmost(sn, rn):
    if rn is None:
        return sn
    if isinstance(sn, int):
        return sn + rn
    return [sn[0], add_rightmost(sn[1], rn)]


def split(sn):
    if isinstance(sn, int):
        if sn >= 10:
            half = sn / 2
            return True, [math.floor(half), math.ceil(half)]
        return False, sn

    is_split, res = split(sn[0])
    if is_split:
        return True, [res, sn[1]]
    is_split, res = split(sn[1])
    if is_split:
        return True, [sn[0], res]

    return False, sn


def explode(sn, level=1):
    if isinstance(sn, int):
        return False, None, sn, None
    if level > 4:
        return True, sn[0], 0, sn[1]

    exploded, left, mid, right = explode(sn[0], level + 1)
    if exploded:
        return True, left, [mid, add_leftmost(sn[1], right)], None
    exploded, left, mid, right = explode(sn[1], level + 1)
    if exploded:
        return True, None, [add_rightmost(sn[0], left), mid], right
    return False, None, sn, None


def reduce(sn):
    while True:
        exploded, _, sn, _ = explode(sn)
        if exploded:
            continue

        is_split, sn = split(sn)
        if not is_split:
            break
    return sn


def magnitude(sn):
    if isinstance(sn, int):
        return sn
    return 3 * magnitude(sn[0]) + 2 * magnitude(sn[1])


def parse_input(example=False):
    filename = "example.txt" if example else "day18.txt"
    with open(filename) as f:
        return [ast.literal_eval(line) for line in f]


def solve_part1(example=False):
    lines = parse_input(example)
    sn_sum = functools.reduce(lambda sn1, sn2: reduce([sn1, sn2]), lines)

    print(sn_sum)
    return magnitude(sn_sum)


def solve_part2(example=False):
    lines = parse_input(example)
    perms = itertools.permutations(lines, 2)
    return max(magnitude(reduce([sn1, sn2])) for sn1, sn2 in perms)


# print(solve_part1())
print(solve_part2())

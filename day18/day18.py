import ast
import functools
import math


def add_leftmost(sn, rn):
    if isinstance(sn, int):
        return sn + rn
    return [add_leftmost(sn[0], rn), sn[1]]


def add_rightmost(sn, rn):
    if isinstance(sn, int):
        return sn + rn
    return [sn[0], add_rightmost(sn[1], rn)]


def reduce(sn, level=1):
    if isinstance(sn, int):
        if sn >= 10:
            half = sn / 2
            return [math.floor(half), math.ceil(half)], True
        return sn, False

    if level >= 4:
        if isinstance(sn[0], list):
            new_list = [0, add_leftmost(sn[1], sn[0][1])]
            return new_list, True
        if isinstance(sn[1], list):
            new_list = [add_rightmost(sn[0], sn[1][0]), 0]
            return new_list, True


    left, left_reduced = reduce(sn[0], level + 1)
    if left_reduced:
        return [left, sn[1]], True

    right, right_reduced = reduce(sn[1], level + 1)
    if right_reduced:
        return [sn[0], right], True

    return [left, right], False


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
    # sn_sum = functools.reduce(lambda sn1, sn2: reduce(add(sn1, sn2)), lines)
    sn_sum = lines[0]
    for i in range(1, len(lines)):
        temp_sum = [sn_sum, lines[i]]
        sn_sum = reduce(temp_sum)
    sn_sum = reduce(sn_sum)

    print(sn_sum)
    return magnitude(sn_sum[0])


# s = [7,[6,[5,[4,[3,2]]]]]
# print(add_leftmost(s, 2))
print(solve_part1(True))

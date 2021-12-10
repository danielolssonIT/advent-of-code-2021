import collections

illegal_char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

closed_matching_open = {')': '(', ']': '[', '}': '{', '>': '<'}


def parse_input(example=False):
    filename = "example.txt" if example else "day10.txt"
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def solve_part1(example=False):
    data = parse_input(example)
    opening_symbols = {'(', '[', '{', '<'}
    first_illegal_chars = []
    for line in data:
        stack = collections.deque()
        for c in line:
            if c in opening_symbols:
                stack.append(c)
                continue
            last_opened_symbol = stack.pop()
            if closed_matching_open[c] != last_opened_symbol:
                first_illegal_chars.append(c)
                break
    return sum(illegal_char_points[c] for c in first_illegal_chars)


print(solve_part1())

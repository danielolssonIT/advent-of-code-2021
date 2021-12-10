import collections

illegal_char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_char_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

opening_symbols = {'(', '[', '{', '<'}
open_match_pair = {'(': ')', '[': ']', '{': '}', '<': '>'}


def parse_input(example=False):
    filename = "example.txt" if example else "day10.txt"
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def solve_part1(example=False):
    data = parse_input(example)
    first_illegal_chars = []
    for line in data:
        stack = collections.deque()
        for c in line:
            if c in opening_symbols:
                stack.append(c)
                continue
            last_opened_symbol = stack.pop()
            if open_match_pair[last_opened_symbol] != c:
                first_illegal_chars.append(c)
                break
    return sum(illegal_char_points[c] for c in first_illegal_chars)


def incomplete_lines(lines):
    incomplete = []
    for line in lines:
        corrupt = False
        stack = collections.deque()
        for c in line:
            if c in opening_symbols:
                stack.append(c)
                continue
            last_opened_symbol = stack.pop()
            if open_match_pair[last_opened_symbol] != c:
                corrupt = True
                break
        if not corrupt:
            incomplete.append(line)
    return incomplete


def solve_part2(example=False):
    incomplete = incomplete_lines(parse_input(example))
    total_scores = []
    for line in incomplete:
        stack = collections.deque()
        completion_chars = []
        for c in line:
            if c in opening_symbols:
                stack.append(c)
            else:
                stack.pop()

        while stack:
            opening_symbol = stack.pop()
            completion_chars.append(open_match_pair[opening_symbol])
        score = 0
        for c in completion_chars:
            score *= 5
            score += completion_char_points[c]
        total_scores.append(score)
    return sorted(total_scores)[len(total_scores) // 2]


print(solve_part1())
print(solve_part2())

def read_input_from_file():
    with open('../inputs/day3.txt') as f:
        return list(map(lambda s: s.strip(), f.readlines()))


def solve(lines):
    number_of_ones = dict((index, 0) for index in range(len(lines[0])))
    for line in lines:
        for i, c in enumerate(line):
            number_of_ones[i] += int(c)

    gamma = ""
    majority_limit = len(lines) // 2
    for n in number_of_ones:
        gamma += "1" if number_of_ones[n] >= majority_limit else "0"

    epsilon = int("".join("1" if d == "0" else "0" for d in gamma), 2)
    gamma = int(gamma, 2)
    return gamma * epsilon


def value_to_keep(lines, bit_position, most_common=True):
    number_of_ones = [line[bit_position] for line in lines].count("1")
    number_of_zeros = len(lines) - number_of_ones
    rating = "1" if number_of_ones >= number_of_zeros else "0"
    opposite = "1" if rating == "0" else "0"
    return rating if most_common else opposite


def solve_part2(lines):
    lines_left = lines.copy()
    for i in range(len(lines[0])):
        if len(lines_left) == 1:
            break
        lines_left = list(filter(lambda l: l[i] == value_to_keep(lines_left, i), lines_left))
    oxygen = int(lines_left[0], 2)

    lines_left = lines.copy()
    for i in range(len(lines[0])):
        if len(lines_left) == 1:
            break
        lines_left = list(filter(lambda l: l[i] == value_to_keep(lines_left, i, most_common=False), lines_left))
    co2 = int(lines_left[0], 2)
    return oxygen * co2


example_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]
print(solve_part2(read_input_from_file()))

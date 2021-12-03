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
print(solve(read_input_from_file()))

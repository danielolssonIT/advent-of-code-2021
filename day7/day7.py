import statistics


def parse_input(example=False):
    filename = "example.txt" if example else "day7.txt"
    with open(filename) as f:
        return list(map(int, f.read().split(",")))


def solve_part1(example=False):
    data = parse_input(example)
    least_fuel_position = int(statistics.median(data))
    alignment_fuel_spent = sum(abs(d - least_fuel_position) for d in data)
    return alignment_fuel_spent


print(solve_part1(False))

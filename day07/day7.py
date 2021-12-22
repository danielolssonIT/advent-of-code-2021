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


def solve_part2(example=False):
    data = parse_input(example)
    least_fuel_position = int(statistics.mean(data))

    def alignment_cost(from_pos):
        position_diff = abs(from_pos - least_fuel_position)
        return (position_diff * (position_diff + 1)) / 2

    alignment_fuel_spent = sum(alignment_cost(d) for d in data)
    return int(alignment_fuel_spent)


print(solve_part1(False))
print(solve_part2(False))

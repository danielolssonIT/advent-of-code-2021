def parse_input(example=False):
    filename = "example.txt" if example else "day6.txt"
    with open(filename) as f:
        return list(map(int, f.read().split(",")))


def solve_part1(days, example=False):
    lantern_fish = parse_input(example)
    start_day = 6
    new_fish_start_day = 8
    for sim_day in range(days):
        fish_to_create = 0
        for i, day in enumerate(lantern_fish):
            if day == 0:
                lantern_fish[i] = start_day
                fish_to_create += 1
            else:
                lantern_fish[i] -= 1
        for i in range(fish_to_create):
            lantern_fish.append(new_fish_start_day)
    return len(lantern_fish)


print(solve_part1(80, False))

import collections


def parse_input(example):
    filename = "example.txt" if example else "day11.txt"
    data = []
    with open(filename) as f:
        for line in f:
            data.append([int(n) for n in list(line.strip())])
    return data


def in_bounds(row, col):
    return 0 <= row < 10 and 0 <= col < 10


def adjacent_positions(row, col):
    adj_pos = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            same_pos = i == row and j == col
            if not same_pos and in_bounds(i, j):
                adj_pos.append((i, j))
    return adj_pos


def solve_part1(example=False):
    grid = parse_input(example)
    flash_count = 0
    for step in range(100):
        already_flashed = set()
        to_flash = collections.deque()

        def sim_step(row, col):
            grid[row][col] += 1
            if grid[row][col] > 9:
                to_flash.append((row, col))
                already_flashed.add((row, col))

        for i in range(10):
            for j in range(10):
                sim_step(i, j)

        while to_flash:
            r, c = to_flash.popleft()
            flash_count += 1
            grid[r][c] = 0
            adj_pos_not_flashed = filter(lambda p: p not in already_flashed, adjacent_positions(r, c))
            for ai, aj in adj_pos_not_flashed:
                sim_step(ai, aj)

    return flash_count


def solve_part2(example=False):
    grid = parse_input(example)
    step = 0
    while True:
        if all(all(n == 0 for n in row) for row in grid):
            return step

        already_flashed = set()
        to_flash = collections.deque()

        def sim_step(row, col):
            grid[row][col] += 1
            if grid[row][col] > 9:
                to_flash.append((row, col))
                already_flashed.add((row, col))

        for i in range(10):
            for j in range(10):
                sim_step(i, j)

        while to_flash:
            r, c = to_flash.popleft()
            grid[r][c] = 0
            adj_pos_not_flashed = filter(lambda p: p not in already_flashed, adjacent_positions(r, c))
            for ai, aj in adj_pos_not_flashed:
                sim_step(ai, aj)
        step += 1


print(solve_part1())
print(solve_part2())

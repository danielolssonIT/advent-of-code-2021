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


def print_grid(grid):
    s = ""
    for row in grid:
        s += ''.join(str(c) for c in row)
        s += '\n'
    print(s)


def solve_part1(example=False):
    grid = parse_input(example)
    flash_count = 0
    for step in range(100):
        already_flashed = set()
        to_flash = collections.deque()
        for i in range(10):
            for j in range(10):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    to_flash.append((i, j))
                    already_flashed.add((i, j))
        while to_flash:
            flash_count += 1
            r, c = to_flash.popleft()
            grid[r][c] = 0
            adj_pos_not_flashed = filter(lambda p: p not in already_flashed, adjacent_positions(r, c))
            for ai, aj in adj_pos_not_flashed:
                grid[ai][aj] += 1
                if grid[ai][aj] > 9:
                    to_flash.append((ai, aj))
                    already_flashed.add((ai, aj))
    return flash_count


print(solve_part1())

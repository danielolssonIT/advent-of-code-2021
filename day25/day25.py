from copy import deepcopy


def parse_input(example=False):
    filename = "ex.txt" if example else "input.txt"
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid


def next_pos(elem, row, col, grid_width, grid_height):
    next_row = row + 1 if elem == "v" else row
    next_col = col + 1 if elem == ">" else col
    if next_row >= grid_height:
        next_row = 0
    if next_col >= grid_width:
        next_col = 0
    return next_row, next_col


def move(symbol, grid):
    new_grid = deepcopy(grid)
    has_moved = False
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == symbol:
                next_i, next_j = next_pos(elem, i, j, len(row), len(grid))
                if grid[next_i][next_j] == ".":
                    new_grid[next_i][next_j] = symbol
                    new_grid[i][j] = "."
                    has_moved = True
    return has_moved, new_grid


def solve_part1(example=False):
    grid = parse_input(example)
    has_moved = True
    steps = 0
    while has_moved:
        moved1, new_grid = move(">", grid)
        moved2, new_grid = move("v", new_grid)
        grid = new_grid
        has_moved = moved1 or moved2
        steps += 1
    print('\n'.join(''.join(row) for row in grid))
    return steps


print(solve_part1())

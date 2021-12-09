def parse_input(example=False):
    filename = "example.txt" if example else "day9.txt"
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(list(map(int, line.strip())))
    return grid


def in_bounds(row, col, grid_rows, grid_columns):
    return 0 <= row < grid_rows and 0 <= col < grid_columns


def adjacent_heights(heightmap, row, col):
    adj_heights = []
    grid_rows = len(heightmap)
    grid_cols = len(heightmap[0])
    adj_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for r, c in adj_positions:
        if in_bounds(r, c, grid_rows, grid_cols) and not (r == row and c == col):
            adj_heights.append(heightmap[r][c])
    return adj_heights


def solve_part1(example=False):
    heightmap = parse_input(example)
    low_points_risk_levels = []
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            adj_heights = adjacent_heights(heightmap, i, j)
            if all(h > height for h in adj_heights):
                low_points_risk_levels.append(1 + height)
    return sum(low_points_risk_levels)


print(solve_part1())

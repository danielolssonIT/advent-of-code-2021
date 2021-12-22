import collections


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
    adj_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
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


def low_points_positions(heightmap):
    low_points_pos = []
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            adj_heights = adjacent_heights(heightmap, i, j)
            if all(h > height for h in adj_heights):
                low_points_pos.append((i, j))
    return low_points_pos


def adjacent_heights_positions(heightmap, row, col):
    adj_heights = []
    grid_rows = len(heightmap)
    grid_cols = len(heightmap[0])
    adj_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in adj_positions:
        if in_bounds(r, c, grid_rows, grid_cols) and not (r == row and c == col):
            adj_heights.append((r, c))
    return adj_heights


def solve_part2(example=False):
    heightmap = parse_input(example)
    low_points_pos = low_points_positions(heightmap)
    basin_sizes = []
    for row, col in low_points_pos:
        q = collections.deque([(row, col)])
        basin_size = 0
        visited = set()
        while q:
            i, j = q.popleft()
            if heightmap[i][j] == 9 or (i, j) in visited:
                continue
            q.extend(adjacent_heights_positions(heightmap, i, j))
            visited.add((i, j))
            basin_size += 1
        basin_sizes.append(basin_size)

    prod = 1
    three_largest_basins = sorted(basin_sizes)[-3:]
    for basin in three_largest_basins:
        prod *= basin
    return prod


print(solve_part1())
print(solve_part2())

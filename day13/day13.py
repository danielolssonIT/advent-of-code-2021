def parse_input(example=False):
    filename = "example.txt" if example else "day13.txt"
    with open(filename) as f:
        coords_str, folds_str = f.read().split('\n\n')
    coords = [s.split(',') for s in coords_str.split('\n')]
    for i in range(len(coords)):
        for j in range(2):
            coords[i][j] = int(coords[i][j])
    folds = [s.rsplit(' ', 1)[1] for s in folds_str.split('\n')]
    folds = [s.split('=') for s in folds]
    return coords, folds


def fold(coords, axis, line):
    if axis == 'y':
        return set((x, line - abs(y - line)) for x, y in coords)
    return set((line - abs(line - x), y) for x, y in coords)


def solve(example=False, num_folds=1):
    coords, folds = parse_input(example)
    for i in range(num_folds):
        axis, line = folds[i]
        coords = fold(coords, axis, int(line))
    dots_visible = len(coords)
    print_grid(coords)
    return dots_visible


def print_grid(coords):
    grid_width = max(c[0] for c in coords) + 1
    grid_height = max(c[1] for c in coords) + 1
    grid = [['.' for _ in range(grid_width)] for _ in range(grid_height)]
    for x, y in coords:
        grid[y][x] = '#'
    print('\n'.join(''.join(row) for row in grid))


#print(solve())
print(solve(num_folds=12))

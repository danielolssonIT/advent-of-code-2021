class Line:
    def __init__(self, start, stop):
        self.x1 = start[0]
        self.y1 = start[1]
        self.x2 = stop[0]
        self.y2 = stop[1]

    def __repr__(self):
        return f"({self.x1},{self.y1} -> {self.x2},{self.y2})"

    def points_on_line(self):
        min_x = min(self.x1, self.x2)
        max_x = max(self.x1, self.x2)
        min_y = min(self.y1, self.y2)
        max_y = max(self.y1, self.y2)

        x_step = 1 if self.x1 < self.x2 else -1
        y_step = 1 if self.y1 < self.y2 else -1
        x_values = range(self.x1, self.x2 + x_step, x_step)
        y_values = range(self.y1, self.y2 + y_step, y_step)
        # Vertical
        if min_y == max_y:
            points = [(x, max_y) for x in x_values]
        # Horizontal
        elif min_x == max_x:
            points = [(max_x, y) for y in y_values]
        # Diagonal
        else:
            points = [(x, y) for x, y in zip(x_values, y_values)]
        return points


def parse_input(example=False):
    filename = "example.txt" if example else "day5.txt"
    data = []
    with open(filename) as f:
        for line in f:
            parsed_line = line.strip().split(" -> ")
            start_end = list(map(int, parsed_line[0].split(",")))
            stop_end = list(map(int, parsed_line[1].split(",")))
            data.append(Line(start_end, stop_end))
    return data


def print_grid(grid):
    s = ""
    for row in grid:
        for c in row:
            s += c
        s += '\n'
    print(s)


def solve_part1(example=False):
    lines = parse_input(example)
    points = [p for line in lines for p in line.points_on_line()]
    grid_width = max(p[0] for p in points)
    grid_height = max(p[1] for p in points)
    grid = []
    for i in range(grid_height + 1):
        row = ['.' for _ in range(grid_width + 1)]
        grid.append(row)

    for p in points:
        y = p[0]
        x = p[1]
        if grid[x][y] == '.':
            grid[x][y] = '1'
        else:
            grid[x][y] = str(int(grid[x][y]) + 1)

    dangerous_points = sum(int(c) >= 2 for row in grid for c in row if c != '.')
    return dangerous_points


print(solve_part1(False))

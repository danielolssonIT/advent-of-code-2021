import networkx as nx


def in_bounds(row, col, max_row, max_col):
    return 0 <= row <= max_row and 0 <= col <= max_col


def adjacent_positions(row, col, max_row, max_col):
    adj_pos = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(i, j) for i, j in adj_pos if in_bounds(i, j, max_row, max_col)]


def create_graph(grid):
    graph = nx.DiGraph()
    max_rows = len(grid) - 1
    max_cols = len(grid[0]) - 1
    for row, line in enumerate(grid):
        for col, risk in enumerate(line):
            graph.add_node((row, col))
            for i, j in adjacent_positions(row, col, max_rows, max_cols):
                risk = int(grid[i][j])
                graph.add_edge((row, col), (i, j), weight=risk)
    return graph, max_rows, max_cols


def parse_input(example=False, full_map=False):
    filename = "example.txt" if example else "day15.txt"
    with open(filename) as f:
        grid = [line.strip() for line in f.readlines()]
    if full_map:
        extend_grid_full_map(grid)
    return create_graph(grid)


def inc_risk(risk, term):
    n = int(risk) + term
    return n if n <= 9 else n % 9


def inc_row(row, term):
    return ''.join(str(inc_risk(value, term)) for value in row)


def extend_grid_full_map(grid):
    for r, line in enumerate(grid):
        for term in range(1, 5):
            grid[r] += inc_row(line, term)

    row_count_before = len(grid)
    for term in range(1, 5):
        for i in range(row_count_before):
            grid.append(inc_row(grid[i], term))


def solve(example=False, full_map=False):
    graph, rows, cols = parse_input(example, full_map)
    return nx.dijkstra_path_length(graph, (0, 0), (rows, cols))


print(solve())
print(solve(full_map=True))

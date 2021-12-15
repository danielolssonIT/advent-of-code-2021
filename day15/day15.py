import networkx as nx

def in_bounds(row, col, max_row, max_col):
    return 0 <= row <= max_row and 0 <= col <= max_col


def adjacent_positions(row, col, max_row, max_col):
    adj_pos = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(i, j) for i, j in adj_pos if in_bounds(i, j, max_row, max_col)]


def parse_input(example=False):
    filename = "example.txt" if example else "day15.txt"
    graph = nx.DiGraph()
    with open(filename) as f:
        grid = [line.strip() for line in f.readlines()]
    max_rows = len(grid) - 1
    max_cols = len(grid[0]) - 1
    for row, line in enumerate(grid):
        for col, risk in enumerate(line):
            graph.add_node((row, col))
            for i, j in adjacent_positions(row, col, max_rows, max_cols):
                risk = int(grid[i][j])
                graph.add_edge((row, col), (i, j), weight=risk)
    return graph, max_rows, max_cols


def solve_part1(example=False):
    graph, rows, cols = parse_input(example)
    return nx.dijkstra_path_length(graph, (0, 0),  (rows, cols))


print(solve_part1())

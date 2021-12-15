import networkx as nx


def create_graph(grid):
    graph = nx.grid_2d_graph(len(grid), len(grid), create_using=nx.DiGraph)
    for s, t in graph.edges:
        graph[s][t]["weight"] = int(grid[t[0]][t[1]])
    return graph, len(grid) - 1, len(grid[0]) - 1


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

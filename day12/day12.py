import collections


def parse_input(example=False):
    filename = "example.txt" if example else "day12.txt"
    graph = {}
    with open(filename) as f:
        for line in f:
            from_node, to_node = line.strip().split('-', 1)

            def add_node(fr, to):
                if fr in graph:
                    graph[fr].append(to)
                else:
                    graph[fr] = [to]

            add_node(from_node, to_node)
            add_node(to_node, from_node)
    return graph


def solve_part1(example=False):
    graph = parse_input(example)
    q = collections.deque((cave, {"start"}) for cave in graph["start"])
    number_of_small_cave_paths = 0
    while q:
        cave, visited = q.popleft()
        if cave in visited:
            continue
        if cave == "end":
            if len(visited) >= 2:
                number_of_small_cave_paths += 1
            continue
        new_visited = visited.copy()
        if cave.islower():
            new_visited.add(cave)
        q.extend((c, new_visited) for c in graph[cave])
    return number_of_small_cave_paths


print(solve_part1())

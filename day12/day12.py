import collections


def parse_input(example=False):
    filename = "example.txt" if example else "day12.txt"
    graph = {}
    with open(filename) as f:
        for line in f:
            from_node, to_node = line.strip().split('-', 1)

            def add_node(fr, to):
                if to == "start":
                    return
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
        cave, visited = q.pop()
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


def solve_part2(example=False):
    graph = parse_input(example)
    # (cave str, visited set, single small cave visited twice)
    q = collections.deque((cave, {"start"}, False) for cave in graph["start"])
    number_of_paths = 0
    while q:
        cave, visited, small_cave_visited_twice = q.pop()
        if cave == "end":
            number_of_paths += 1
            continue
        new_small_cave_visited_twice = small_cave_visited_twice
        if cave in visited:
            if small_cave_visited_twice:
                continue
            else:
                new_small_cave_visited_twice = True
        new_visited = visited.copy()
        if cave.islower():
            new_visited.add(cave)
        q.extend((c, new_visited, new_small_cave_visited_twice) for c in graph[cave])
    return number_of_paths


print(solve_part1())
print(solve_part2())

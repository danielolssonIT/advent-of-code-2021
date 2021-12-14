import collections

def parse_input(example=False):
    filename = "example.txt" if example else "day14.txt"
    with open(filename) as f:
        template, pair_insertions_str = f.read().split("\n\n", 1)
        pair_insertions = (line.split(" -> ") for line in pair_insertions_str.split("\n"))
        rules = dict((a, b) for a, b in pair_insertions)
        return list(template), rules


def solve_part1(example=False):
    template, rules = parse_input(example)
    for step in range(10):
        elems_to_insert = []
        for i in range(1, len(template)):
            pair = template[i-1] + template[i]
            elem = rules.get(pair, "")
            if elem:
                elems_to_insert.append((i, elem))
        for j, elem in enumerate(elems_to_insert):
            insert_index = elem[0]
            c = elem[1]
            template.insert(insert_index + j, c)
    element_count = collections.Counter(template).most_common()
    return element_count[0][1] - element_count[-1][1]



print(solve_part1())

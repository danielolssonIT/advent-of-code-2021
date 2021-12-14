import collections


def parse_input(example=False):
    filename = "example.txt" if example else "day14.txt"
    with open(filename) as f:
        template, pair_insertions_str = f.read().split("\n\n", 1)
        pair_insertions = (line.split(" -> ") for line in pair_insertions_str.split("\n"))
        rules = dict((a, b) for a, b in pair_insertions)
        return template, rules


def solve(example=False, steps=1):
    template, rules = parse_input(example)
    pair_count = collections.defaultdict(int)
    element_count = collections.defaultdict(int)
    for i in range(1, len(template)):
        pair_count[template[i - 1:i + 1]] += 1
    for c in template:
        element_count[c] += 1

    for step in range(steps):
        pairs_to_add = collections.defaultdict(int)
        for pair, count in pair_count.items():
            if count == 0:
                continue
            pair_count[pair] = 0
            inserted_element = rules[pair]
            element_count[inserted_element] += count
            pair1 = pair[0] + inserted_element
            pair2 = inserted_element + pair[1]
            for p in [pair1, pair2]:
                pairs_to_add[p] += count
        for k, v in pairs_to_add.items():
            pair_count[k] += v

    sorted_elem_counts = sorted(element_count.values())
    return sorted_elem_counts[-1] - sorted_elem_counts[0]


print(solve(steps=10))
print(solve(steps=40))

segment_values = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}


def parse_input(example=False):
    filename = "example.txt" if example else "day8.txt"
    signal_patterns_output_pairs = []
    with open(filename) as f:
        for line in f:
            splitted_line = [s.strip() for s in line.split("|")]
            signal_patterns = [''.join(sorted(s)) for s in splitted_line[0].split()]
            output_values = [''.join(sorted(s)) for s in splitted_line[1].split()]
            signal_patterns_output_pairs.append((signal_patterns, output_values))
    return signal_patterns_output_pairs


def solve_part1(example=False):
    data = parse_input(example)
    unique_segment_count = 0
    nbr_of_segments_unique = {2, 3, 4, 7}
    for signal_patterns, output_values in data:
        unique_segment_count += sum(len(digit) in nbr_of_segments_unique for digit in output_values)
    return unique_segment_count


print(solve_part1())

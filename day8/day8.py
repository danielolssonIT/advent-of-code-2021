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


def diff_chars(s1, s2):
    return ''.join(set(s1).symmetric_difference(set(s2)))


def solve_part1(example=False):
    data = parse_input(example)
    unique_segment_count = 0
    nbr_of_segments_unique = {2, 3, 4, 7}
    for signal_patterns, output_values in data:
        unique_segment_count += sum(len(digit) in nbr_of_segments_unique for digit in output_values)
    return unique_segment_count


def solve_part2(example=False):
    data = parse_input(example)
    output_value_sum = 0
    for signal_patterns, output_values in data:
        # Top, topleft, topright, middle, bottomleft, bottomright, bottom
        keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        signal_wiring_segment = dict((el, '') for el in keys)

        sorted_signal_patterns = sorted(signal_patterns, key=len)
        topleft_middle = ['b', 'd']
        topright_bottomright = ['c', 'f']
        bottomleft_bottom = ['e', 'g']

        signal_wiring_segment['a'] = diff_chars(sorted_signal_patterns[1], sorted_signal_patterns[0])
        for i in topright_bottomright:
            signal_wiring_segment[i] = sorted_signal_patterns[0]

        rem_keys = diff_chars(sorted_signal_patterns[0], sorted_signal_patterns[2])
        for i in topleft_middle:
            signal_wiring_segment[i] = ''.join(rem_keys)

        locked_eight = ''.join(signal_wiring_segment[i] for i in ['a', 'b', 'c'])
        rem_keys = diff_chars(locked_eight, sorted_signal_patterns[-1])
        for i in bottomleft_bottom:
            signal_wiring_segment[i] = rem_keys

        rem_segments = [diff_chars(sorted_signal_patterns[-1], sorted_signal_patterns[i]) for i in range(6, 9)]
        rem_segments_keys = ['c', 'd', 'e']
        related_keys = {'c': 'f', 'd': 'b', 'e': 'g'}
        for rem in rem_segments:
            for key in rem_segments_keys:
                if rem in signal_wiring_segment[key]:
                    signal_wiring_segment[key] = rem
                    related_key = related_keys[key]
                    signal_wiring_segment[related_key] = signal_wiring_segment[related_key].replace(rem, "")
                    break

        digit = ""
        swapped_wiring_segment = dict((v, k) for k, v in signal_wiring_segment.items())
        for val in output_values:
            rerouted_val = ''.join(swapped_wiring_segment[c] for c in val)
            digit += str(segment_values[''.join(sorted(rerouted_val))])
        output_value_sum += int(digit)

    return output_value_sum


print(solve_part1())
print(solve_part2())

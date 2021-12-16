import functools

type_id_operator = {
    0: lambda a, b: a + b,
    1: lambda a, b: a * b,
    2: lambda a, b: min(a, b),
    3: lambda a, b: max(a, b),
    5: lambda a, b: int(a > b),
    6: lambda a, b: int(a < b),
    7: lambda a, b: int(a == b)
}


def parse_input(example=False):
    filename = "example.txt" if example else "day16.txt"
    with open(filename) as f:
        hex_message = f.read().strip()
    num_of_bits = 4 * len(hex_message)
    return bin(int(hex_message, 16))[2:].zfill(num_of_bits)


def packet_version_sum(message):
    if len(message) < 11:
        return 0

    version = int(message[:3], 2)
    type_id = int(message[3:6], 2)
    if type_id == 4:
        i = 6
        while message[i] != "0":
            i += 5
        return version + packet_version_sum(message[i + 11:])

    length_type_id = int(message[6])
    if length_type_id == 0:
        return version + packet_version_sum(message[22:])
    return version + packet_version_sum(message[18:])


def literal_packet_value(data, index):
    val = ""
    i = index + 6
    while data[i] != "0":
        val += data[i + 1:i + 5]
        i += 5
    val += data[i + 1:i + 5]
    return int(val, 2), i + 5


def evaluate_packet(data, index):
    if "1" not in data:
        return 0, 0

    type_id = int(data[index + 3:index + 6], 2)
    if type_id == 4:
        return literal_packet_value(data, index)

    subpacket_values = []
    length_type_id = int(data[index + 6], 2)
    if length_type_id == 0:
        subpacket_bits = int(data[index + 7:index + 22], 2)
        next_index = index + 22
        while next_index < index + 22 + subpacket_bits:
            val, next_index = evaluate_packet(data, next_index)
            subpacket_values.append(val)
    else:
        subpacket_count = int(data[index + 7:index + 18], 2)
        next_index = index + 18
        for i in range(subpacket_count):
            val, next_index = evaluate_packet(data, next_index)
            subpacket_values.append(val)
  
    return functools.reduce(type_id_operator[type_id], subpacket_values), next_index


def solve(example=False):
    bin_message = parse_input(example)
    return packet_version_sum(bin_message)


def solve_part2(example=False):
    bin_message = parse_input(example)
    return evaluate_packet(bin_message, 0)


print(solve())
print(solve_part2()[0])

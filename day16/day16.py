import re


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
        #nearest_four_multiple = (len(data) + 3) & ~0x03
        i = 6
        while message[i] != "0":
            i += 5
        return version + packet_version_sum(message[i+5:])

    length_type_id = int(message[6])
    if length_type_id == 0:
        #sub_packet_length_bits = int(message[7:22], 2)
        return version + packet_version_sum(message[22:])
    else:
        #sub_packet_count = int(message[7:18], 2)
        return version + packet_version_sum(message[18:])



def solve(example=False):
    bin_message = parse_input(example)
    return packet_version_sum(bin_message)




print(solve())
#print(packet_version_sum("00111000000000000110111101000101001010010001001000000000")) # = 9

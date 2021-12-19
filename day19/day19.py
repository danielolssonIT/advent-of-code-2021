

def parse_input(example=False):
    filename = "example.txt" if example else "day19.txt"
    beacon_pos = []
    with open(filename) as f:
        scanner_beacons = []
        for line in f:
            if ',' not in line:
                if scanner_beacons:
                    beacon_pos.append(scanner_beacons)
                scanner_beacons = []
            else:
                x, y = line.split(',')
                scanner_beacons.append((int(x), int(y)))
        beacon_pos.append(scanner_beacons)
    return beacon_pos


print(parse_input(True))

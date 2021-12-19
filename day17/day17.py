import re
import math


def parse_input(example=False):
    filename = "example.txt" if example else "day17.txt"
    with open(filename) as f:
        line = f.read().strip()
    pattern = re.compile("target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)")
    res = pattern.search(line)
    if res:
        return map(int, res.groups())
    return None


def solve_part1(example=False):
    min_x, max_x, min_y, max_y = parse_input(example)
    # vx^2 + vx - 2*min_x > 0
    vx = math.ceil((-1 / 2) + math.sqrt((1 / 4) + 2 * min_x))
    vy = abs(min_y) - 1

    return max_height(vy)


def solve_part2(example=False):
    min_x, max_x, min_y, max_y = parse_input(example)
    lowest_vx = math.ceil((-1 / 2) + math.sqrt((1 / 4) + 2 * min_x))
    highest_vy = abs(min_y) - 1
    highest_vx = max_x
    lowest_vy = min_y
    valid_velocities = 0
    for vx in range(lowest_vx, highest_vx + 1):
        for vy in range(lowest_vy, highest_vy + 1):
            if in_range((vx, vy), (min_x, min_y), (max_x, max_y)):
                valid_velocities += 1
    print(valid_velocities)


def max_height(vely):
    return vely * (vely + 1) // 2
    # 1+2+3+...+velx = vel


def in_range(velocity, minimum, maximum):
    pos = (0, 0)
    while True:
        x, y = pos
        if x in range(minimum[0], maximum[0] + 1) and y in range(minimum[1], maximum[1] + 1):
            return True

        velx, vely = velocity
        if (x < minimum[0] or x > maximum[0]) and velx == 0:
            return False
        if y < minimum[1]:
            return False

        pos = (x + velx, y + vely)
        if velx > 0:
            velx -= 1
        elif velx < 0:
            velx += 1
        vely -= 1
        velocity = (velx, vely)


print(solve_part1())
print(solve_part2())

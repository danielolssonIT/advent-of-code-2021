def pos_and_depth_mul(commands):
    horiz_pos = 0
    depth = 0
    aim = 0
    for cmd, unit in commands:
        if cmd == "forward":
            horiz_pos += unit
            depth += aim * unit
        elif cmd == "down":
            aim += unit
        else:
            aim -= unit

    return horiz_pos * depth


def format_input(text):
    commands = []
    for line in text:
        split_line = line.split()
        command = split_line[0]
        unit = int(split_line[1])
        commands.append((command, unit))
    return commands


def solution_from_file():
    with open('day2.txt', 'r') as f:
        cmds = format_input(f.readlines())

    return pos_and_depth_mul(cmds)


def solution_from_example():
    s = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]
    return pos_and_depth_mul(format_input(s))


print(solution_from_file())

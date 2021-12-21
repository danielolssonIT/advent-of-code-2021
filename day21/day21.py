def parse_input(example=False):
    filename = "example.txt" if example else "day21.txt"
    with open(filename) as f:
        player1, player2 = f.read().split('\n')
        player1_start_pos = player1.split(": ")[-1]
        player2_start_pos = player2.split(": ")[-1]
    return int(player1_start_pos), int(player2_start_pos)


def reset(n, divisor):
    return (n - 1) % divisor + 1


def solve_part1(example=False):
    p1_start_pos, p2_start_pos = parse_input(example)
    score = [0, 0]
    pos = [p1_start_pos, p2_start_pos]
    turn = 0
    die_value = 1
    die_rolls = 0
    while score[0] < 1000 and score[1] < 1000:
        die_sum = 0
        for _ in range(3):
            die_rolls += 1
            die_sum += die_value
            die_value = reset(die_value + 1, 100)
        steps_to_move = reset(die_sum, 10)
        pos[turn] = reset(pos[turn] + steps_to_move, 10)
        score[turn] += pos[turn]
        turn = 1 if turn == 0 else 0
    return min(score) * die_rolls


print(solve_part1())

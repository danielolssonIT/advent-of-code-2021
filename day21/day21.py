import functools
import itertools


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


@functools.cache
def wins(start_positions, score, turn):
    if score[0] >= 21:
        return 1, 0
    if score[1] >= 21:
        return 0, 1

    new_turn = 0 if turn == 1 else 1
    total_p1_wins = 0
    total_p2_wins = 0
    for die_values in itertools.product(range(1, 4), repeat=3):
        new_pos = list(start_positions)
        new_score = list(score)

        new_pos[turn] = reset(start_positions[turn] + sum(die_values), 10)
        new_score[turn] += new_pos[turn]

        p1_wins, p2_wins = wins(tuple(new_pos), tuple(new_score), new_turn)
        total_p1_wins += p1_wins
        total_p2_wins += p2_wins

    return total_p1_wins, total_p2_wins


def solve_part2(example=False):
    return wins(parse_input(example), (0, 0), 0)


# print(solve_part1())
print(solve_part2())

import numpy as np


class BingoNumber:
    def __init__(self, n):
        self.n = n
        self.marked = False


class BingoBoard:
    def __init__(self, grid):
        self.grid = grid

    def mark_number(self, x):
        for row in self.grid:
            for bingo_num in row:
                if x == bingo_num.n:
                    bingo_num.marked = True
                    return

    def sum_of_unmarked(self):
        all_unmarked_nums = filter(lambda x: not x.marked, (n for row in self.grid for n in row))
        return sum(bn.n for bn in all_unmarked_nums)

    def has_won(self):
        def won(grid):
            return any(all(n.marked for n in row) for row in grid)

        any_row_won = won(self.grid)
        any_col_won = won(np.transpose(self.grid))
        return any_row_won or any_col_won


def parse_input(example=False):
    filename = "day4.txt" if not example else "example.txt"
    with open(filename) as f:
        lines = f.read()

    s = lines.split('\n\n', 1)
    bingo_numbers = list(map(int, s[0].split(',')))
    remaining_inp = s[1].split('\n\n')

    def line_to_grid(line):
        return [[BingoNumber(int(n)) for n in row.split()] for row in line.split('\n')]

    bingo_boards = [BingoBoard(line_to_grid(row)) for row in remaining_inp]

    return bingo_numbers, bingo_boards


def winning_board(bingo_numbers, bingo_boards):
    for n in bingo_numbers:
        for board in bingo_boards:
            board.mark_number(n)
            if board.has_won():
                return board, n
    return None, None


def last_winning_board(bingo_numbers, bingo_boards):
    boards = bingo_boards.copy()
    for n in bingo_numbers:
        to_remove = []
        for board in boards:
            board.mark_number(n)
            if board.has_won():
                if len(boards) == 1:
                    return board, n
                to_remove.append(board)
        for b in to_remove:
            boards.remove(b)



    return None, None


def solve_part1(example=False):
    bingo_numbers, bingo_boards = parse_input(example)
    win_board, called_number = winning_board(bingo_numbers, bingo_boards)
    score = win_board.sum_of_unmarked() * called_number
    return score


def solve_part2(example=False):
    bingo_numbers, bingo_boards = parse_input(example)
    win_board, called_number = last_winning_board(bingo_numbers, bingo_boards)
    score = win_board.sum_of_unmarked() * called_number
    return score


print(solve_part2(example=False))

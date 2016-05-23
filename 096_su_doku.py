#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Poker hands" – Project Euler Problem No. 54
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=54


def load_sudoku_puzzles(filename):
    puzzles = []
    with open(filename, 'r') as filehandle:
        lines = filehandle.readlines()
        linenr = 0
        for line in lines:
            linenr += 1
            if linenr % 10 == 1:
                if linenr != 1:
                    puzzles.append(puzzle)
                puzzle = []
                continue
            puzzle = puzzle + map(int, list(line.strip()))
    puzzles.append(puzzle)
    return puzzles


def get_value(i, j, puzzle):
    return puzzle[9*i+j]


def set_value(i, j, puzzle, value):
    puzzle[9*i+j] = value


def get_row(nr, puzzle):
    ret = []
    for i in range(9):
        ret.append(get_value(nr, i, puzzle))
    return ret


def get_col(nr, puzzle):
    ret = []
    for i in range(9):
        ret.append(get_value(i, nr, puzzle))
    return ret


def get_box(i, j, puzzle):
    ret = []
    from_ii = 3*int(i/3)
    from_jj = 3*int(j/3)
    for ii in range(from_ii, from_ii+3):
        for jj in range(from_jj, from_jj+3):
            ret.append(get_value(ii, jj, puzzle))
    return ret


def row_missing_values(nr, puzzle):
    return set(range(1, 10)).difference(get_row(nr, puzzle))


def col_missing_values(nr, puzzle):
    return set(range(1, 10)).difference(get_col(nr, puzzle))


def box_missing_values(i, j, puzzle):
    return set(range(1, 10)).difference(get_box(i, j, puzzle))


def is_valid_row(nr, puzzle):
    return len(row_missing_values(nr, puzzle)) == 0


def is_valid_col(nr, puzzle):
    return len(col_missing_values(nr, puzzle)) == 0


def is_valid_box(i, j, puzzle):
    return len(box_missing_values(i, j, puzzle)) == 0


def is_solution(puzzle):
    if not puzzle:
        return False
    if 0 in puzzle:
        return False

    for i in range(9):
        if not is_valid_row(i, puzzle):
            print "invalid row", i
            return False
        if not is_valid_col(i, puzzle):
            print "invalid col", i
            return False

        ii = 3 * (i / 9)
        jj = 3 * (i % 9) % 9
        if not is_valid_box(ii, jj, puzzle):
            return False
    return True


def is_solution_to(solved_puzzle, puzzle):
    for i in range(9):
        for j in range(9):
            vt = get_value(i, j, puzzle)
            if vt == 0:
                continue
            vs = get_value(i, j, solved_puzzle)
            if vt != vs:
                return False
    return is_solution(solved_puzzle)


def possible_values(i, j, puzzle):
    if get_value(i, j, puzzle) != 0:
        return None  # value already set

    poss_row = row_missing_values(i, puzzle)
    poss_col = col_missing_values(j, puzzle)
    poss_box = box_missing_values(i, j, puzzle)

    poss = poss_row
    poss = poss.intersection(poss_col)
    poss = poss.intersection(poss_box)

    return list(poss)


def find_ij_with_possiblevalues(puzzle):
    ret = []
    for i in range(9):
        for j in range(9):
            poss = possible_values(i, j, puzzle)
            if poss:
                ret.append((i, j, poss))
    return ret


def show_puzzle(puzzle):
    tmp = ''
    i = 1
    for v in puzzle:
        tmp += " "
        if v != 0:
            tmp += str(v)
        else:
            tmp += "_"
        tmp += " "
        if i % 3 == 0 and i > 0:
            tmp += " "
        if i % 9 == 0 and i > 0:
            tmp += "\n"
        i = i + 1
    print tmp + "\n"


def solve_puzzle(puzzle):
    scratch = list(puzzle) # make a copy
    possible_values = find_ij_with_possiblevalues(scratch)
    if possible_values:
        possible_values = sorted(possible_values, key=lambda x: len(x[2])) # to get the fields with the least possible values first
        (i, j, poss) = possible_values[0]
        poss = sorted(list(poss)) # try inserting numbers at (i,j) in ascending order
        for value in poss:
            set_value(i, j, scratch, value)
            solved = solve_puzzle(scratch)
            if solved:
                return solved  # found a solution
            set_value(i, j, scratch, 0) # unset the value again

    if is_solution(scratch):
        return scratch

    return False


def get_corner_number(puzzle):
    return int("".join(map(str, puzzle[:3])))


# Testcase 1
test_puzzle = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
]
solved_puzzle = solve_puzzle(test_puzzle)
assert is_solution(solved_puzzle), "Testcase failed"

# Testcase 2
test_puzzle = [
    0, 0, 3, 0, 2, 0, 6, 0, 0,
    9, 0, 0, 3, 0, 5, 0, 0, 1,
    0, 0, 1, 8, 0, 6, 4, 0, 0,
    0, 0, 8, 1, 0, 2, 9, 0, 0,
    7, 0, 0, 0, 0, 0, 0, 0, 8,
    0, 0, 6, 7, 0, 8, 2, 0, 0,
    0, 0, 2, 6, 0, 9, 5, 0, 0,
    8, 0, 0, 2, 0, 3, 0, 0, 9,
    0, 0, 5, 0, 1, 0, 3, 0, 0,
]
expected_solution = [
    4, 8, 3, 9, 2, 1, 6, 5, 7,
    9, 6, 7, 3, 4, 5, 8, 2, 1,
    2, 5, 1, 8, 7, 6, 4, 9, 3,
    5, 4, 8, 1, 3, 2, 9, 7, 6,
    7, 2, 9, 5, 6, 4, 1, 3, 8,
    1, 3, 6, 7, 9, 8, 2, 4, 5,
    3, 7, 2, 6, 8, 9, 5, 1, 4,
    8, 1, 4, 2, 5, 3, 7, 6, 9,
    6, 9, 5, 4, 1, 7, 3, 8, 2,
]
assert get_corner_number(expected_solution) == 483, "Testcase failed"
assert is_solution(expected_solution), "Testcase failed"
assert is_solution_to(expected_solution, test_puzzle), "Testcase failed"

test_solution = solve_puzzle(test_puzzle)
assert get_corner_number(test_solution) == 483, "Testcase failed"
assert is_solution(test_solution), "Testcase failed"
assert is_solution_to(test_solution, test_puzzle), "Testcase failed"

assert test_solution == expected_solution, "Testcase failed"


# Solve
solution = 0
puzzles = load_sudoku_puzzles('096_sudoku.txt')
for puzzle in puzzles:
    print "Puzzle:\n"
    show_puzzle(puzzle)

    solved_puzzle = solve_puzzle(puzzle)
    assert is_solution(solved_puzzle)

    print "Solved:\n"
    show_puzzle(solved_puzzle)

    solution = solution + get_corner_number(solved_puzzle)

print "Solution:", solution

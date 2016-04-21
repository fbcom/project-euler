#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Square digit chains" – Project Euler Problem No. 92
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=92
#


def add_squares_of_digits(n):
    sumOfSquares = 0
    for digit in list(str(n)):
        sumOfSquares = sumOfSquares + int(digit)**2
    return sumOfSquares


def get_sequence(n):
    ret = [n]
    while ret[-1] not in [1, 89]:
        ret.append(add_squares_of_digits(ret[-1]))
    return ret


def get_end_of_sequence(n):
    return get_sequence(n)[-1]


# Testcase 1
expected_sequence = [44, 32, 13, 10, 1]
sequence = get_sequence(expected_sequence[0])
assert (len(sequence) == len(expected_sequence))
for i, m in enumerate(expected_sequence):
    assert (sequence[i] == m), "Testcase failed"

# Testcase 2
expected_sequence = [85, 89]
sequence = get_sequence(expected_sequence[0])
assert (len(sequence) == len(expected_sequence))
for i, m in enumerate(expected_sequence):
    assert (sequence[i] == m), "Testcase failed"

# Testcase 3
expected_sequence = [145, 42, 20, 4, 16, 37, 58, 89]
sequence = get_sequence(expected_sequence[0])
assert (len(sequence) == len(expected_sequence))
for i, m in enumerate(expected_sequence):
    assert (sequence[i] == m), "Testcase failed"

# Solve
counter = {
    "1": 0,
    "89": 0
}
maxn = 10000000 # ten million
for n in range(1, maxn):
    counter[str(get_end_of_sequence(n))] = counter[str(get_end_of_sequence(n))] + 1
    if n % 10000 == 0:
        print "Counter: ", counter
print "Counter: ", counter

print "Solution:", counter["89"]

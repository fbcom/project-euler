#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Pentagon numbers" – Project Euler Problem No. 44
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=44


def get_pentagonal_number(n):
    return int(n*(3*n-1)/2)


def is_pentagonal_number(n):
    tmp = (1 + (1.0+24*n)**0.5) / 6  # inverse function of n*(3n-1)
    return int(tmp) == tmp  # n is pentagonal if the inverse function yields an int

# Testcases
some_pentagonal_numbers = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
for n in some_pentagonal_numbers:
    assert is_pentagonal_number(n), "Testcase failed"
for n in range(1, 11):
    assert get_pentagonal_number(n) == some_pentagonal_numbers[n-1], "Testcase failed"

# Solve
solution = None
k = 0
while not solution:
    k += 1
    p_k = get_pentagonal_number(k)
    j = k
    while j > 1:
        j -= 1
        p_j = get_pentagonal_number(j)
        if is_pentagonal_number(p_k + p_j) and\
           is_pentagonal_number(p_k - p_j):
            solution = int(p_k - p_j)
            # print "p%d=%d, p%d=%d, solution=%d" % (k, p_k, j, p_j, solution)
            break

print "Solution:", solution

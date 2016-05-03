#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Permuted multiples" – Project Euler Problem No. 52
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=52


def same_digits_in_permuted_multiples(n, max_factor):
    chars = "".join(sorted(list(str(n))))
    for factor in range(1, max_factor+1):
        m = factor * n
        if chars != "".join(sorted(list(str(m)))):
            return False

    return True

# # Testcases
assert same_digits_in_permuted_multiples(125874, 2), "Testcase failed"

# Solve
solution = 1
while not same_digits_in_permuted_multiples(solution, 6):
    solution = solution + 1
print "Solution:", solution

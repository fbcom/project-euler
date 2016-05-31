#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Right triangles with integer coordinates" – Project Euler Problem No. 91
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=91


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solve(n):
    ret = 0
    if n > 0:
        for i in range(1, n+1):
            for j in range(1, n+1):
                d = gcd(i, j)
                ret += min(d*i/j, d*(n-j)/i)
        ret *= 2  # symmetry along diagonal
    ret += 3 * n**2  # how often the slope of the diagonal lies on the points of the grid
    return ret

# Testcases
assert 0 == solve(0), "Testcase failed"
assert 3 == solve(1), "Testcase failed"
assert 14 == solve(2), "Testcase failed"

# Solve
print "Solution:", solve(50)

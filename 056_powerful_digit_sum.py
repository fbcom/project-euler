#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Powerful digit sum" – Project Euler Problem No. 56
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=56


def sum_of_digits(n):
    sum = 0
    for digit in map(int, list(str(n))):
        sum = sum + digit
    return sum

# Testcase
assert sum_of_digits(100**100) == 1, "Testcase failed"

# Solve
solution = 0
for a in range(100):
    for b in range(100):
        n = a**b
        sum = sum_of_digits(n)
        if sum > solution:
            solution = sum

print "Solution:", solution

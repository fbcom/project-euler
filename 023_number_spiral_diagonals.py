#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Number spiral diagonals" – Project Euler Problem No. 28
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=28
#


def sum_of_diagonals(dim):
    ret = 1
    spiral_quadrant_width = (dim-1)/2  # excludes the center
    for i in range(spiral_quadrant_width):
        q2 = (1 + 2*i) ** 2 + (2 * (i+1))
        q3 = (1 + 2*i) ** 2 + (4 * (i+1))
        q4 = (1 + 2*i) ** 2 + (6 * (i+1))
        q1 = (1 + 2*i) ** 2 + (8 * (i+1))
        ret = ret + q1 + q2 + q3 + q4
    return ret

# Testcase
assert (101 == sum_of_diagonals(5)), "Testcase failed"

# Solve
print "Solution:", sum_of_diagonals(1001)

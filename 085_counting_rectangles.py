#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Counting rectangles" – Project Euler Problem No. 85
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=85


def num_rectangles_in_grid(n, m):
    # O(n*m) solution:
    # ret = 0
    # for i in range(n):
    #     for j in range(m):
    #         ret += (i+1)*(j+1)

    # O(1) solution:
    ret = n*(n+1) * m*(m+1) / 4
    return ret


def find_min_fitting_area(limit_rectangles):
    maximum = (0, 0)
    maximum_rectangles = num_rectangles_in_grid(*maximum)
    for n in range(limit_rectangles, 0, -1):

        m = 1
        while num_rectangles_in_grid(n, m) <= limit_rectangles:
            m = m + 1
        m = m - 1

        if num_rectangles_in_grid(n, m) > maximum_rectangles:
            maximum = (n, m)
            maximum_rectangles = num_rectangles_in_grid(*maximum)

        n = n - 1

    return maximum[0] * maximum[1]


# Testcases
assert num_rectangles_in_grid(2, 3) == 18, "Testcase failed"

# Solve
limit_rectangles = 2 * 1000*1000
solution = find_min_fitting_area(limit_rectangles)
print "Solution:", solution

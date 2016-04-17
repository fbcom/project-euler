#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Maximum path sum I" – Project Euler Problem No. 18
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=18
#


def get_triangular_list(str):
    ret = []
    tmp = []
    i = j = 1
    for n in str.split():
        tmp.append(int(n))
        j = j + 1
        if j > i:
            ret.append(tmp)
            tmp = []
            j = 1
            i = i + 1
    return ret


def find_max_path(nums, row, col):
    if row == len(nums):
        return 0
    n = nums[row][col]
    a = n + find_max_path(nums, row + 1, col + 0)
    b = n + find_max_path(nums, row + 1, col + 1)
    return max(a, b)

# Testrun
pyramid = """
3
7 4
2 4 6
8 5 9 3
"""

tri = get_triangular_list(pyramid)
assert (23 == find_max_path(tri, 0, 0)), "Testcase failed"

# Solve
pyramid = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

tri = get_triangular_list(pyramid)
print "Solution:", find_max_path(tri, 0, 0)

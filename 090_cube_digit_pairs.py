#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Cube digit pairs" – Project Euler Problem No. 90
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=90
import itertools

digits = map(str, range(10))
cubic_numbers = map(lambda n: "%02d" % (int(n)**2), digits)[1:]


def can_display(n_str, cube_a, cube_b):
    if int(n_str[0]) in cube_a and int(n_str[1]) in cube_b:
        return True
    if int(n_str[1]) in cube_a and int(n_str[0]) in cube_b:
        return True
    return False


def prepare_cube(cube):
    if 6 in cube and not 9 in cube:
        cube.append(9)
    if 9 in cube and not 6 in cube:
        cube.append(6)
    sorted(cube)
    return cube


def count_different_cube_pairs():
    ret = 0

    # generate all cubes
    cubes = []
    for selection in itertools.combinations(digits, 6):
        cube = prepare_cube(map(int, selection))
        cubes.append(cube)

    # cross product of all cubes
    all_cubes = list(itertools.product(cubes, cubes))

    visited = []  # to keep track of already seen cubes
    for (c1, c2) in all_cubes:
        # cubes must be different
        if c1 == c2:
            continue

        # check if we alredy tried this cube
        key = "".join(map(str, c1)+['-']+map(str, c2))
        if key in visited:
            continue
        else:
            visited.append(key)

        # check if all the cubic numbers can be formed using the the cubes
        for cubic_number in cubic_numbers:
            if not can_display(cubic_number, c1, c2):
                ret -= 1
                break
        ret += 1
    ret /= 2  # so that swapped cubes should not be counted
    return ret

# Testcases
cube_a = prepare_cube([0, 5, 6, 7, 8, 9])
cube_b = prepare_cube([1, 2, 3, 4, 8, 9])
for cubic_number in cubic_numbers:
    assert can_display(cubic_number, cube_a, cube_b), "Testcase failed"

# Solve
solution = count_different_cube_pairs()
print "Solution:", solution

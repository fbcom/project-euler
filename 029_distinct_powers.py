#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Distinct powers" – Project Euler Problem No. 29
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=29
#


def distinct_powers(max_a, max_b):
    powers = set()
    for a in range(2, max_a + 1):
        for b in range(2, max_b + 1):
            powers.add(a**b)
    return sorted(list(powers))

# Testcase
powers = distinct_powers(5, 5)
assert (len(powers) == 15), "Testcase failed"

# Solve
powers = distinct_powers(100, 100)
print "Solution:", len(powers)

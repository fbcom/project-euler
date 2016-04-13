#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Smallest multiple" – Project Euler Problem No. 5
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=5
#


def calc_smallest_multiple(numbers):
    factors = []
    for n in range(2, numbers+1):
        new_f = n
        for f in factors:
            if new_f % f == 0:
                new_f = new_f / f
        if new_f > 1:
            factors.append(new_f)
    return reduce(lambda product, factor: product * factor, factors)

assert (2520 == calc_smallest_multiple(10)), "Testcase failed."
print "Solution:", calc_smallest_multiple(20)

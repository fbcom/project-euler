#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Reciprocal cycles" – Project Euler Problem No. 26
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=26
#


def reciprocal(n):
    # we'll be doing manual division here
    # and find cycles along the way
    #
    # dividend : n = result
    #  divisor
    # --------
    #     rest
    #      ...
    rest = []
    result = 0
    dividend = 1
    digits = cycle = ""
    while dividend > 0:
        if dividend < n:
            result = result * 10
            dividend = dividend * 10
        else:
            result = result + (dividend // n)
            digits = "%s%s" % (digits, str((dividend // n)))
            dividend = dividend % n

        if dividend in rest:  # we found a cycle
            begin_of_cycle = rest.index(dividend)
            cycle = digits[begin_of_cycle:]
            break
        else:
            rest.append(dividend)
    return (result, cycle)

cycle_len_max = cycle_len_max_d = 0
for d in range(1, 1000):
    (decimal, cycle) = reciprocal(d)

    if cycle and len(cycle) > cycle_len_max:
        cycle_len_max = len(cycle)
        cycle_len_max_d = d

print "Solution: 1/%d has %d-digit recurring cycle" % (cycle_len_max_d, cycle_len_max)

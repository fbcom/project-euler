#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Digit fifth powers" – Project Euler Problem No. 30
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=30
#


def sum_of_powers_of_digits(exponent):
    max_n = 10**(exponent+1)
    ret = 0
    for n in range(10, max_n):  # ignore trivial cases
        breaking_flag = False
        number = 0
        for digit in str(n):
            number += int(digit)**exponent
            if number > n:
                breaking_flag = True
                break

        if breaking_flag:
            continue

        if number == n:
            # print n
            ret = ret + n
    return ret

# Testcase
assert(19316 == sum_of_powers_of_digits(4)), "Testcase failed"

# Solve
solution = sum_of_powers_of_digits(5)
print "Solution:", solution

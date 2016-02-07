#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Multiples of 3 and 5" – Project Euler Problem No. 1
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=1
#


def func(n):
    if n % 5 == 0:
        return True
    if n % 3 == 0:
        return True
    return False

# Finds the sum of all the multiples of 3 or 5 below 1000
result = reduce(lambda sum, add: sum+add, [x for x in range(0, 1000) if func(x)])
print "Solution:", result

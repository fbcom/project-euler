#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Ordered fractions" – Project Euler Problem No. 71
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=71

from fractions import Fraction

# Solve
limit = 1000*1000  # one million
solution = Fraction(0, 1)
for d in range(1, limit):
    n = int(d*3/7) - 1  # because n/d must be smaller than 3/7
    fraction = Fraction(n, d)
    if solution < fraction:
        solution = fraction

print "Solution:", solution.numerator

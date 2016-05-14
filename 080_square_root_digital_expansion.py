#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Square root digital expansion" – Project Euler Problem No. 80
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=80
from decimal import *
getcontext().prec = 102  # 2 places before the , and 100 decimal places after the ,


def sum_digits_of_sqrt(n):
    root = Decimal(n).sqrt()
    digits = str(root).replace('.', '')
    return sum(map(int, digits[:100]))

# Testcase
assert sum_digits_of_sqrt(2) == 475, "Testcase failed"

# Solve
solution = 0
for n in range(1, 101):
    if n**0.5 == int(n**0.5):
        continue  # not irrational
    solution += sum_digits_of_sqrt(n)
print "Solution:", solution

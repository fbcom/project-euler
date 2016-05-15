#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Square root convergents" – Project Euler Problem No. 57
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=57


def iterate(a, b):
    return (a+2*b, a+b)

# Solve
solution, a, b = 0, 3, 2
for i in range(1000):
    if len(str(a)) > len(str(b)):
        solution = solution + 1
    a, b = iterate(a, b)

print "Solution:", solution

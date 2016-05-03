#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Powerful digit counts" – Project Euler Problem No. 63
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=63

# Solve
solution = exponent = 0
while True:
    base = 0
    last_solution = solution
    while True:
        base = base + 1
        n = base**exponent
        l = len(str(n))
        if l == exponent:
            solution = solution + 1
            print "%d^%d = %d" % (base, exponent, n)
        elif l > exponent:
            break
    exponent = exponent + 1
    if last_solution == solution and base > 1:
        # no new solutions found, so we are done
        break

print "Solution:", solution

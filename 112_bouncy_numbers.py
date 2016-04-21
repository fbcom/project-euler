#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Bouncy numbers" – Project Euler Problem No. 112
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=112
#


def is_bouncy(n):
    min = max = lastv = int(str(n)[0])
    decreasing = None
    increasing = None
    for c in list(str(n))[1:]:
        v = int(c)
        if v > lastv:
            increasing = True
            if decreasing:
                return True
        if v < lastv:
            decreasing = True
            if increasing:
                return True
        if v != lastv:
            lastv = v
    return False


a = 0
b = c = n = 100
while True:
    n = n + 1
    c = c + 1
    if is_bouncy(n):
        a = a + 1
    else:
        b = b + 1
    percentage = 100.0 * a / c

    if percentage == 99:
        print "Solution:", n
        break

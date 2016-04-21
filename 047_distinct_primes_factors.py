#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Distinct prime factors" – Project Euler Problem No. 47
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=47
#


def factor(n):
    ret = []
    for d in [2] + range(3, int(n**0.5) + 2, 2):
        if n % d == 0:
            ret.append(d)
            while n % d == 0:
                n /= d
    if n > 1:
        ret.append(n)

    return ret

desiredfactorcount = 4
togo = desiredfactorcount
n = 0
while True:
    n = n + 1
    factorcount = len(factor(n))
    if factorcount == desiredfactorcount:
        togo = togo - 1
    else:
        togo = desiredfactorcount
    if togo == 0:
        break

print "Solution:"

for n in range(n - desiredfactorcount + 1, n + 1):
    factors = factor(n)
    print n, "has", len(factors), "factors", factors

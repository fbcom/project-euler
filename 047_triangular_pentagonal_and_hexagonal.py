#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Triangular, pentagonal and hexagonal" – Project Euler Problem No. 45
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=45


def get_triangular_number(n):
    return int(n*(n+1)/2)


def get_pentagonal_number(n):
    return int(n*(3*n-1)/2)


def get_hexagonal_number(n):
    return int(n*(2*n-1))

# Testcase and initialisation
n_t = 285
n_p = 165
n_h = 143
tn = get_triangular_number(n_t)
pn = get_pentagonal_number(n_p)
hn = get_hexagonal_number(n_h)
assert (40755 == tn), "Testcase failed"
assert (40755 == pn), "Testcase failed"
assert (40755 == hn), "Testcase failed"

# Solve
while True:
    n_h += 1  # grows the fastest, so inc it first
    hn = get_hexagonal_number(n_h)

    while pn < hn:
        n_p += 1
        pn = get_pentagonal_number(n_p)

    while tn < hn:
        n_t += 1
        tn = get_triangular_number(n_t)

    if hn == pn == tn:
        print "Solution: %d (T%d, P%d, H%d)" % (tn, n_t, n_p, n_h)
        break

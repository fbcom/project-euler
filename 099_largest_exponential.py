#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Largest exponential" – Project Euler Problem No. 99
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statemax_ent: https://projecteuler.net/problem=99


def load_exponentials(filename):
    ret = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            ret.append(map(int, line.strip().split(",")))
    return ret

exponentials = load_exponentials("099_base_exp.txt")

max_n = max_e = 0
i = max_i = 0
for (n, e) in exponentials:
    i = i + 1
    if i == 1:
        max_n = n
        max_e = e
        max_i = i
        continue

    if 0 < n**(1.0*e/max_e)-max_n:
        print "%3d: %d^%d" % (i, n, e) # new max in line i
        max_n = n
        max_e = e
        max_i = i

print "\nSolution:", max_i

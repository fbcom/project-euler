#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Longest Collatz sequence" – Project Euler Problem No. 14
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=14
#


def get_next(n):
    if n % 2 == 0:
        return n/2
    return 3*n+1


def build_collatz_sequence(n):
    ret = [n]
    print n
    while n != 1:
        n = get_next(n)
        ret.append(n)
    return ret

assert ([13, 40, 20, 10, 5, 16, 8, 4, 2, 1] == build_collatz_sequence(13)), "Testcase failed."

solution = 0
for n in range(1, 1000*1000):  # this might take quite some time ...
    seq = build_collatz_sequence(n)
    if len(seq) > solution:
        solution = len(seq)

print "Solution:", solution

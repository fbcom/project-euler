#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Odd period square roots" – Project Euler Problem No. 64
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=64


def iterate(S, m, d, a, a0):
    m_next = d * a - m
    d_next = (S - m_next**2) / d
    a_next = (a0 + m_next) / d_next
    return (S, m_next, d_next, a_next, a0)


def get_period_of_continued_fraction(S):
    ret = []

    a0 = int(S**0.5)
    if a0**2 == S:
        return None  # does not work for squares

    (m, d, a) = (0, 1, a0)
    while a != 2*a0:
        (_, m, d, a, _) = iterate(S, m, d, a, a0)
        ret.append(a)

    return ret


# Testcase
assert len(get_period_of_continued_fraction(23)) == 4, "Testcase failed"
assert len(get_period_of_continued_fraction(114)) == 6, "Testcase failed"

# Solve
solution = 0
for n in range(1, 10001):
    if int(n**0.5) == n**0.5:
        continue
    if len(get_period_of_continued_fraction(n)) % 2 == 1:
        solution += 1

print "Solution:", solution

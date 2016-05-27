#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Convergents of e" – Project Euler Problem No. 65
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=65


def iterate(S, m, d, a, a0):
    m_next = d * a - m
    d_next = (S - m_next**2) / d
    a_next = (a0 + m_next) / d_next
    return (S, m_next, d_next, a_next, a0)


def get_sum_of_digits_of_convergent(n, convergent_limit):
    convergent, d = n, 1
    for i in range(2, convergent_limit + 1):
        temp, d, c = d, convergent, 1
        if i % 3 == 0:
            c = 2*(i/3)
        convergent = c * convergent + temp
    return sum(map(int, list(str(convergent))))


# Solve
solution = get_sum_of_digits_of_convergent(2, 100)
print "Solution:", solution

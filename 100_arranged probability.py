#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Arranged probability" – Project Euler Problem No. 100
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=100


def iterate(B, N):
    # Using the input equations:
    #
    # (1) 0.5 == (B**2 - B) / (B*(B+2*R-1) + R*(R-1)))
    # (2) N = R+B
    #
    # and inserting (2) in (1) yields the
    # diophantine quadratic equation:
    #
    # (3) 0.5 = (B**2 - B) / (N**2-N)
    #
    # Which can be expressed iteratively
    #
    # (4) B_next = 3*B + 2*N - 2
    # (5) N_next = 4*B + 3*N - 3
    #
    B_next = 3*B + 2*N - 2
    N_next = 4*B + 3*N - 3
    return (B_next, N_next)

# Solve
B = N = 1
while True:
    (B, N) = iterate(B, N)
    if N > 10**12:
        solution = B
        break

print "Solution:", solution

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Lattice Path" – Project Euler Problem No. 13
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=13
#


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))

# @see problem statement
grid_width = 2
print "Example: ", binomial_coefficient(2 * grid_width, grid_width)

grid_width = 20
print "Solution: ", binomial_coefficient(2 * grid_width, grid_width)

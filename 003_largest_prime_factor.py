#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Largest Prime Factor" – Project Euler Problem No. 3
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=3
#
from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    for d in [2] + range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def find_largest_prime_factor(n):
    # eleminate two as a factor to speed up the while loop below
    if n % 2 == 0:
        while n % 2 == 0:
            n = n / 2
        factor = find_largest_prime_factor(n)  # now we only need to get the largest prime factor of the remainder
        return factor if factor > 1 else 2  # if we get 1 as a result for the remainder then 2 is the largest prime factor of n

    factor = int(sqrt(n))
    factor = factor + 1 - factor % 2  # factor cannot be even
    while factor > 1:
        if n % factor == 0:
            if is_prime(factor):
                return factor
        factor = factor - 2  # skip even factors
    return n  # n itself is prime

n = 600851475143
print "Solution:", find_largest_prime_factor(n)

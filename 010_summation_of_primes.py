#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Largest Prime Factor" – Project Euler Problem No. 3
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=3
from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    for d in [2] + range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def sum_of_primes_below(n):
    result = 2  # 2 is our first prime
    for m in range(3, n, 2):
        if is_prime(m):
            result = result + m
    return result

n = 2000000
print "Solution:", sum_of_primes_below(n)

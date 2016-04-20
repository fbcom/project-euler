#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Quadratic primes" – Project Euler Problem No. 27
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=27
#


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in [2] + range(3, int(n**0.5) + 2, 2):
        if n % d == 0:
            return False
    return True


def compute_quadratic_form(a, b, n):
    return n**2 + a*abs(n) + b

# Solve
temp = [0, 0, 0]
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime(compute_quadratic_form(a, b, n)):
            n = n + 1
        if n > temp[0]:
            temp = [n, a, b]

print "Solution:", temp[1] * temp[2]

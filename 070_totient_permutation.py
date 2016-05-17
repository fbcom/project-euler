#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Totient permutation" – Project Euler Problem No. 70
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=70


def is_permutation_of(n, m):
    n, m = str(n), str(m)
    if len(m) != len(n):
        return False
    else:
        for digit in n:
            if n.count(digit) != m.count(digit):
                return False
        return True

# Solve

# Use a sieve to compute phi[n] for all n < limit
limit = 10**7
phi = range(0, limit+1)
for i in range(2, limit+1):
    if phi[i] == i:
        for j in range(i, limit+1, i):
            phi[j] = phi[j] / i * (i - 1)  # @see definition of phi(n)

# Find the minimum n/phi[n] where n is a permutation of phi[n]
solution = None
n, max_n, minimum = 1, limit-1, 2.0
while n < max_n:
    n = n + 1
    ratio = 1.0 * n / phi[n]
    if ratio < minimum:
        if is_permutation_of(n, phi[n]):
            solution, minimum = n, ratio

print "Solution:", solution

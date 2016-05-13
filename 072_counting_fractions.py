#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Counting fractions" – Project Euler Problem No. 72
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=72


def get_distinct_prime_factors(n):
    ret = []
    if n > 1:
        for d in [2] + range(3, 1+int(n**0.5), 2):
            if n % d == 0:
                ret.append(d)
            while n % d == 0:
                n = n / d
            if n <= 1:
                break
    if n > 1:
        ret.append(n)
    return ret


def phi(n):
    # Euler's totient function:
    # phi(n) := counts how many numbers k < n have gcd(n,k) = 1
    ret = n
    for p in get_distinct_prime_factors(n):
        ret = ret - ret / p
    return ret


def count_reduced_proper_fractions(limit):
    # turns out the solution is equal to the sum of phi(i) for i in [2,...,limit]
    ret = 0
    for n in range(2, limit+1):
        ret += phi(n)
    return ret

# Testcase
assert count_reduced_proper_fractions(8) == 21, "Testcase failed"

# Solve
limit = 1000*1000  # one million
solution = count_reduced_proper_fractions(limit)
print "Solution:", solution

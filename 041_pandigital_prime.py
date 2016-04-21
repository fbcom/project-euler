#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Pandigital prime" – Project Euler Problem No. 41
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=41
#


import itertools


def is_prime(n):
    if n == 2:
        return True
    for d in [2] + range(3, int(n**0.5) + 2, 2):
        if n % d == 0:
            return False
    return True

def find_largest_n_digit_pandigital_prime(numdigits):
    ret = 0
    digits = map(str, range(1, numdigits))
    for permutation in itertools.permutations(digits):
        n = int("".join(permutation))
        if is_prime(n):
            print n, "is a", numdigits, "digit pandigital prime"
            ret = n
    return ret

# Testcase
assert(is_prime(2143)), "Testcase failed"
assert(2143 != find_largest_n_digit_pandigital_prime(4))

# Solve
solution = 0
for numdigits in range(2, 10):
    prime = find_largest_n_digit_pandigital_prime(numdigits)
    if prime > solution:
        solution = prime

print "Solution: The largest pandigital prime is", solution

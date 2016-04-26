#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Sub-string divisibility" – Project Euler Problem No. 43
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=43
import itertools


def is_substring_divisible(n):
    n = str(n)
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i, prime in enumerate(primes):
        substring = n[i+1:i+1+3]
        assert(len(substring) == 3), "Substring must be of length 3"
        if int(substring) % prime != 0:
            return False
    return True

# Testcase
assert is_substring_divisible(1406357289), "Testcase failed"

# Solve
sum = 0
for permutation in itertools.permutations("1234567890"):
    n = int("".join(permutation))
    if len(str(n)) == 10:
        if is_substring_divisible(n):
            # print "%d is asubstring divisible." % n
            sum = sum + n

print "Solution:", sum

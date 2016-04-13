#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "10001st prime" – Project Euler Problem No. 7
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=7
#


from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    for d in [2] + range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def nth_prime(n):
    if n <= 1:
        return 2
    prime = 3
    for i in range(2, n):
        prime = prime + 2
        while not is_prime(prime):  # skip to the next prime
            prime = prime + 2
    return prime

assert (2 == nth_prime(1)), "Testcase failed."
assert (3 == nth_prime(2)), "Testcase failed."
assert (5 == nth_prime(3)), "Testcase failed."
assert (7 == nth_prime(4)), "Testcase failed."
assert (11 == nth_prime(5)), "Testcase failed."
print "Solution:", nth_prime(10001)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Goldbach's other conjecture" – Project Euler Problem No. 46
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=46


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0:
            return False
    return True


def can_be_written_as_sum_of_prime_and_twice_a_square(n):
    for s in range(1, int(n**0.5)+1):
        p = n - 2*s**2
        if is_prime(p):
            print "%d = %d + 2*%d^2" % (n, p, s)  # this is how n can be written
            return True
    return False

n = 13
while True:
    n = n + 2
    if not is_prime(n):  # n must be composite
        if not can_be_written_as_sum_of_prime_and_twice_a_square(n):
            print "Solution:", n
            break

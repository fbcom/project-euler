#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Circular primes" – Project Euler Problem No. 35
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=35


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


def cycles_of_n(n):
    ret = [n]
    n = str(n)
    for i in range(len(n)):
        ret.append(int(n[i:] + n[:i]))
    return ret


def is_circular_prime(n):
    for n in cycles_of_n(n):
        if not is_prime(n):
            return False
    return True


def count_circular_primes(limit):
    ret = 0
    for n in range(limit):
        if is_circular_prime(n):
            ret = ret + 1
    return ret

# Testcases
assert (True == is_circular_prime(197)), "Testcase failed"
assert (13 == count_circular_primes(100)), "Testcase failed"

# Solve
print "Solution:", count_circular_primes(1000*1000)

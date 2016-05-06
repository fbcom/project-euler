#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Totient maximum" – Project Euler Problem No. 69
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=69


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

# Solve
solution = n = i = 2  # starting with a prime
while n < 1000*1000:
    i = i + 1
    while not is_prime(i):
        i += 1
    solution = n
    n = n * i  # n can only have prime factors (then it has the most amount of coprime numbers)

print "Solution:", solution

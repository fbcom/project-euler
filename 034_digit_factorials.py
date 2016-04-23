#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Digit factorials" – Project Euler Problem No. 34
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=34
#


def factorial(n, limit=False):
    ret = 1
    while n > 0:
        ret *= n
        if limit and ret > limit:
            return 0
        n -= 1
    return ret

factorials = [factorial(n) for n in range(10)]

numbers = list()
for n in range(3, 100000):
    sum = 0
    for digit in [int(digit) for digit in str(n)]:
        sum += factorials[digit]
        if sum > n:
            break
    if sum == n:
        numbers.append(n)

solution = reduce(lambda a, b: a + b, numbers)
print "Solution:", solution

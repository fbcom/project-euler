#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Amicable numbers" – Project Euler Problem No. 21
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=21
#


def get_proper_divisors(n):
    ret = [1]
    for d in range(2, n/2+1):
        if n % d == 0:
            ret.append(d)
    return ret


def d(n):
    return reduce(lambda sum, num: sum + num, get_proper_divisors(n))


def is_amicable_number(n):
    a = d(n)
    if a == n:
        return False
    return n == d(a)

# Testcases
assert (284 == d(220)), "Testcase failed"

# Solve
sum = 0
for n in range(1, 10000):
    if is_amicable_number(n):
        print "%d is amicable number with %d" % (n, d(n))
        sum = sum + n
print "Solution:", sum

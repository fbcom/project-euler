#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Counting partitions" – Project Euler Problem No. 78
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=78


def next_k(k):
    return -k + (1 if k < 0 else 0)


def g(k):
    return (3*(k**2) - k) / 2

cache = {}  # for storing previously computed p(n) values


def p(n):
    global cache
    if n in cache:
        return cache[n]
    if n < 0:
        ret = 0
    elif n == 0:
        ret = 1
    else:
        ret = 0
        i = k = 1
        while True:
            gk = g(k)
            if n-g(k) < 0:
                break
            sign = int((-1)**(int((i-1)/2)))
            ret = ret + sign * p(n-gk)
            k = next_k(k)
            i = i + 1
    cache[n] = ret
    return ret

# Testcases
assert p(1) == 1, "Testcase failed"
assert p(2) == 2, "Testcase failed"
assert p(3) == 3, "Testcase failed"
assert p(4) == 5, "Testcase failed"
assert p(5) == 7, "Testcase failed"

# Solve
solution = 0
while True:
    if p(solution) % (1000*1000) == 0:
        break
    solution = solution + 1
print "Solution:", solution

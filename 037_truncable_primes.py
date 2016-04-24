#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Truncable primes" – Project Euler Problem No. 37
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=37


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


def get_truncs(n, next_trunc=0):
    ret = [n]
    n = str(n)
    for i in range(len(n)-1):
        if i == 0:
            tleft = n[1:]
            tright = n[:-1]
        else:
            tleft = tleft[1:]
            tright = tright[:-1]
        ret.append(int(tleft))
        ret.append(int(tright))

    return ret


def is_truncable_prime(n):
    for m in get_truncs(n):
        if not is_prime(m):
            return False
    return True

# Testcase
n = 3797
assert (True == is_prime(n)), "Testcase failed"
assert (set([n, 797, 97, 7, 379, 37, 3]) == set(get_truncs(n))), "Testcase failed"
assert (True == is_truncable_prime(n)), "Testcase failed"

# Solve
n = 9  # skipping single digit primes
sum = counter = 0
while counter < 11:
    n += 2
    if is_truncable_prime(n):
        counter += 1
        print "%d: %d" % (counter, n)
        sum = sum + n

print "Solution:", sum

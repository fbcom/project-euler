#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Prime power triples" – Project Euler Problem No. 87
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=87


primes = []


def init_prime_array(limit):
    global primes
    primes = [2]
    q = 3
    while q < limit:
        flag = True
        for p in primes:
            if q % p == 0:
                flag = False
                break
            if p**2 > q:
                break
        if flag:
            primes.append(q)
        q = q + 2


def how_many_below(limit):
    global primes
    init_prime_array(int(limit**0.5)+1)

    found = set()
    for p1 in primes:
        pow2 = p1**2
        for p2 in primes:
            pow3 = p2**3
            summation = pow2 + pow3
            if summation > limit:
                break
            for p3 in primes:
                pow4 = p3**4
                summation = pow2 + pow3 + pow4
                if summation > limit:
                    break
                found.add(summation)

    return len(found)


# Testcase
assert how_many_below(50) == 4, "Testcase failed"

# Solve
limit = 50*1000*1000
solution = how_many_below(limit)
print "Solution:", solution

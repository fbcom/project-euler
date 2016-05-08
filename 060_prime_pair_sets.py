#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Prime pair sets" – Project Euler Problem No. 60
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=60


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


def all_concaternations_are_prime(primes):
    # pick two of n
    for p1 in primes:
        for p2 in primes:
            if p1 == p2:
                continue
            q = int(str(p1)+str(p2))
            if not is_prime(q):
                return False
    return True


def solve():
    global primes
    # the primes 2 and 5 cannot be part of a solution because as a last digit of a number n > 10, n would be divisible by 2 or 5
    skip_primes = [0, 2]
    for a in range(len(primes)-5):
        if a in skip_primes:
            continue
        for b in range(a+1, len(primes)-5+1):
            if b in skip_primes:
                continue
            tmp = [primes[index] for index in [a, b]]
            if not all_concaternations_are_prime(tmp):
                continue
            for c in range(b+1, len(primes)-5+2):
                tmp = [primes[index] for index in [a, b, c]]
                if not all_concaternations_are_prime(tmp):
                    continue
                for d in range(c+1, len(primes)-5+3):
                    tmp = [primes[index] for index in [a, b, c, d]]
                    if not all_concaternations_are_prime(tmp):
                        continue
                    for e in range(d+1, len(primes)-5+4):
                        tmp = [primes[index] for index in [a, b, c, d, e]]
                        if all_concaternations_are_prime(tmp):
                            return tmp
    return None


# Testcase
test_primes = [3, 7, 109, 673]
assert 792 == sum(test_primes), "Testcase failed"
assert True == all_concaternations_are_prime(test_primes), "Testcase failed"

# Solve
limit = 10
solution = None
while not solution:
    limit = limit * 10
    init_prime_array(limit)
    print "Searching for a solution in %d primes below %d" % (len(primes), limit)
    solution = solve()

print "\nSolution:", sum(solution), solution

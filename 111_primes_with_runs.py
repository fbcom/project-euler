#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Primes with runs" – Project Euler Problem No. 111
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=111


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


def M(n, d):
    # Maximum number of repreated digit d of an n-digit prime
    digit = str(d)
    max_counter = 0
    for p in primes:
        if p <= 10**(n-1):
            continue
        if p >= 10**(n):
            break
        q = str(p)
        max_counter = max(max_counter, q.count(digit))
    return max_counter


def N(n, d):
    # Maximum number of repreated digit d of an n-digit prime
    # return len(S(n,d))
    max = M(n, d)
    digit = str(d)
    max_counter = 0
    for p in primes:
        if p <= 10**(n-1):
            continue
        if p >= 10**(n):
            break
        q = str(p)
        if q.count(digit) == max:
            max_counter += 1
    return max_counter


def S(n, d):
    ret = []
    max = M(n, d)
    digit = str(d)
    max_counter = 0
    for p in primes:
        if p <= 10**(n-1):
            continue
        if p >= 10**(n):
            break
        q = str(p)
        if q.count(digit) == max:
            ret.append(p)
    return sum(ret)


def solve(digits, d):
    pass

# Testcase
digits = 4
limit = 10**(digits+1)  # 4 digit primes
init_prime_array(limit)

assert M(digits, 0) == 2, "Testcase failed"
assert M(digits, 1) == 3, "Testcase failed"
assert M(digits, 2) == 3, "Testcase failed"
assert M(digits, 3) == 3, "Testcase failed"
assert M(digits, 4) == 3, "Testcase failed"
assert M(digits, 5) == 3, "Testcase failed"
assert M(digits, 6) == 3, "Testcase failed"
assert M(digits, 7) == 3, "Testcase failed"
assert M(digits, 8) == 3, "Testcase failed"
assert M(digits, 9) == 3, "Testcase failed"

assert N(digits, 0) == 13, "Testcase failed"
assert N(digits, 1) == 9, "Testcase failed"
assert N(digits, 2) == 1, "Testcase failed"
assert N(digits, 3) == 12, "Testcase failed"
assert N(digits, 4) == 2, "Testcase failed"
assert N(digits, 5) == 1, "Testcase failed"
assert N(digits, 6) == 1, "Testcase failed"
assert N(digits, 7) == 9, "Testcase failed"
assert N(digits, 8) == 1, "Testcase failed"
assert N(digits, 9) == 7, "Testcase failed"

assert S(digits, 0) == 67061, "Testcase failed"
assert S(digits, 1) == 22275, "Testcase failed"
assert S(digits, 2) == 2221, "Testcase failed"
assert S(digits, 3) == 46214, "Testcase failed"
assert S(digits, 4) == 8888, "Testcase failed"
assert S(digits, 5) == 5557, "Testcase failed"
assert S(digits, 6) == 6661, "Testcase failed"
assert S(digits, 7) == 57863, "Testcase failed"
assert S(digits, 8) == 8887, "Testcase failed"
assert S(digits, 9) == 48073, "Testcase failed"

# Solve
digits = 10
limit = 10**(digits+1)
init_prime_array(limit)
for d in range(digits):
    solution = solution + S(digits, d)

print "Solution:", solution

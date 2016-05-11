#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Primes with runs" – Project Euler Problem No. 111
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=111


primes = []


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


def is_prime_quick(n):
    global primes
    if n in primes:
        return True
    if n < primes[-1]:
        return False
    for d in primes:
        if n % d == 0:
            return False
    return True


def init_prime_array(limit):
    print "Initializing prime array up to", limit
    global primes
    primes = [2]
    q = 3

    percent_last = 0
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
            percent = 100 * (1.0*q/limit)
            if int(percent) > percent_last:
                print "%3.0f%s %d" % (percent, '%', q)
                percent_last = int(percent)
        q = q + 2
    print "Done initializing prime array up to", limit


def solve(digits):
    global primes
    limit = int(((10**digits)-1)**0.5)
    init_prime_array(limit)
    counter = [0]*10
    max_counter = [0]*10
    found_primes = [[]]*10
    sums = [0]*10
    n = 10**(digits-1)-1
    max_n = 10**digits
    while n < max_n:
        n = n + 2
        nstr = str(n)
        if not is_prime_quick(n):
            continue
        flag = False
        for digit in range(10):
            count = nstr.count(str(digit))
            if count > max_counter[digit]:
                max_counter[digit] = count
                counter[digit] = 0
                sums[digit] = 0
                found_primes[digit] = []

            if count == max_counter[digit]:
                counter[digit] += 1
                sums[digit] += n
                found_primes[digit].append(n)
                flag = True

    return sum(sums)

# Testcase
digits = 4
assert 273700 == solve(digits), "Testcase failed"

# Solve
digits = 10
solution = solve(digits)
print "Solution:", solution

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Consecutive prime sum" – Project Euler Problem No. 50
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=50

primes = []


def build_primes(limit):  # for caching
    global primes
    primes = [2]
    for n in range(3, limit+1):
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
            if p*p > n:
                break
        if is_prime:
            primes.append(n)


def build_sums_of_consecutive_primes(start=0):
    global primes
    ret = [primes[start]]
    for index in range(start+1, len(primes)):
        ret.append(ret[-1] + primes[index])
    return ret


def find_longest_prime_sum_of_consecutive_primes(limit):
    global primes
    build_primes(limit)  # store found primes to speed things up a tiny bit

    length = length_max = max_prime_sum = 0
    s_primes = set(primes)
    length_max = 0
    for i in range(len(primes)):
        sums = build_sums_of_consecutive_primes(i)

        for prime_sum in set(sums).intersection(s_primes):  # only consider sums that are primes
            j = sums.index(prime_sum)
            length = i - len(primes) + len(sums) + j + 1
            if length > length_max:
                length_max = length
                max_prime_sum = prime_sum
                print "%d is a prime below %d and the sum of %d consecutive primes" % (sums[length_max-1], limit, length_max)

    return (max_prime_sum, length_max)


# Testcase
limit = 1000
(testcase_solution, length) = find_longest_prime_sum_of_consecutive_primes(limit)
assert (953 in primes), "Testcase failed"
assert (testcase_solution == 953), "Testcase failed"
assert (length == 21), "Testcase failed"

# Solve
limit = 1000*1000  # one million
(solution, length) = find_longest_prime_sum_of_consecutive_primes(limit)
print "Solution: %d (length=%d)" % (solution, length)

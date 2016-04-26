#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Prime permutations" – Project Euler Problem No. 49
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=49


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


def is_permutation_of(a, b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False
    for letter in a:
        if a.count(letter) != b.count(letter):
            return False
    return True

# Solve
primes = []
for n in range(1000, 10000):  # get all 4-digit primes
    if is_prime(n):
        primes.append(n)

solution = ""
for i in range(primes.index(1487)+1, len(primes)):
    pi = primes[i]
    for j in range(i+1, len(primes)):
        pj = primes[j]
        if is_permutation_of(pi, pj):
            diff = pj - pi
            pk = pj + diff
            if is_permutation_of(pj, pk):
                if pk in primes:
                    solution = "%s%s%s" % (pi, pj, pk)
                    break
    if solution:
        break
print "Solution:", solution

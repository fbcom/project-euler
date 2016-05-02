#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Combinatoric selections" – Project Euler Problem No. 53
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=53

from fractions import gcd


def number_of_ways_to_select_k_from_n(k, n):
    # before doing the multiplication and division
    # we are going to remove common factors
    # from the nominator and the denominator
    nominator = range(1, n+1)
    denominator = range(1, k+1) + range(1, n-k+1)

    # remove common factors
    remove = []
    for i in nominator:
        if i in denominator:
            remove.append(i)
    for i in remove:
        del nominator[nominator.index(i)]
        del denominator[denominator.index(i)]
    del remove

    # divide factors by their greatest common divisors
    for i in range(len(nominator)):
        a = nominator[i]
        for j in range(len(denominator)):
            b = denominator[j]
            if b == 1:
                continue
            d = gcd(a, b)
            if d > 1:
                nominator[i] /= d
                denominator[j] /= d
                break

    # perform the multiplication and division using the remainding factors
    ret = 1
    for m in nominator:
        ret = ret * m
    for m in denominator:
        ret = ret / m
    return ret

# # Testcases
assert number_of_ways_to_select_k_from_n(3, 5) == 10, "Testcase failed"
assert number_of_ways_to_select_k_from_n(10, 23) == 1144066, "Testcase failed"


# Solve
solution = 0
for n in range(1, 101):
    for k in range(0, n):
        if number_of_ways_to_select_k_from_n(k, n) > 1000*1000:
            solution = solution + 1

print "Solution:", solution

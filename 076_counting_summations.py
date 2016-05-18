#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Counting summations" – Project Euler Problem No. 76
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=76


def count_summations(n):
    """
    Counting the number of ways to represent n as a sum of integers < n is
    equivalent to computing the sum of the sum of the partitions of 1 to n.
    """
    partitions = [1] + [0] * n
    for i in range(1, n+1):
        summation = 0
        j = k = 1
        while j > 0:
            sign = 1
            if k % 2 == 0:
                sign = -1

            j = i - (3 * k**2 + k) / 2
            if j >= 0:
                summation += sign * partitions[j]

            j = i - (3 * k**2 - k) / 2
            if j >= 0:
                summation += sign * partitions[j]

            k = k+1
        partitions[i] = summation
    return partitions[n] - 1

# Testcases
assert 6 == count_summations(5), "Testcase Failed"

# Solve
solution = count_summations(100)
print "Solution:", solution

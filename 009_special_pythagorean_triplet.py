#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Special Pythagorean triplet" – Project Euler Problem No. 9
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=9
#


def isPythagoreanTriple(a, b, c):
    if a < b < c:
        return a**2 + b**2 == c**2
    return False


def findTipleHavingSum(sum):
    # small problem size -> brute force it
    for a in range(1, sum):
        for b in range(a, sum - a + 1):
            for c in range(b, sum - b + 1):
                if a+b+c == sum:
                    if isPythagoreanTriple(a, b, c):
                        return (a, b, c)

sum = 1000
triple = findTipleHavingSum(sum)
print "Triple:", triple
print "Solution:", reduce(lambda product, factor: product * factor, triple)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Largest Palindrome Product" – Project Euler Problem No. 4
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=4
#


def findpalin(digits):
    result = []
    from_n = 10**(digits-1)
    to_n = 10**digits
    for n in range(to_n, from_n, -1):
        for m in range(n, to_n):
            p = n * m
            q = int(str(p)[::-1])  # reverse p
            if p == q:
                result.append(p)  # yup, we got a palindrome
    return result

digits = 3
print "Solution:", max(findpalin(digits))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Highly divisible triangular number" – Project Euler Problem No. 12
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=12
#

i = n = 0
while True:
    i = i + 1
    n = i*(i+1)/2   # sum of 1 to i
    counter = 2     # 1 and n are two trivial factors of n
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            counter = counter + 2
    if counter > 500:
        break

print "Solution: %d has %d factors" % (n, counter)

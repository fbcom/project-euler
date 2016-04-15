#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "1000-digit Fibonacci number" – Project Euler Problem No. 25
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=25
#

fib = [0, 1]
index = result = solution = 0
while len(str(fib[index])) < 1000:
    solution = solution + 1
    fib[index] = sum(fib)
    if fib[index] % 2 == 0:
        result = result + fib[index]
    index = (index + 1) % 2

print "Solution:", solution

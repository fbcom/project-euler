#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Even Fibonacci Numbers" – Project Euler Problem No. 2
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=2
#
fib = [0, 1]  # the first two fibonacci numbers
index = 0  # fib[index] contains the current fibonacci number
result = 0
while fib[index] < 4*1000000:
    fib[index] = sum(fib)  # computes the next fibobacci number
    if fib[index] % 2 == 0:  # checking if current fibonacci number is even
        result = result + fib[index]
    index = (index + 1) % 2

print "Solution:", result

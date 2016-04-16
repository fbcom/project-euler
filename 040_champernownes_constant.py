#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Champernowne's constant" – Project Euler Problem No. 40
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=40
#


product = 1
n = count = 0
n_str = "0."
while True:
    n = n + 1
    count = count + 1
    n_str = n_str + str(n)
    if count in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        digit = int(n_str[count+1])
        product *= digit
    if count > 1000000:
        break

print "Solution", product

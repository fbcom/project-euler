#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Factorial digit sum" – Project Euler Problem No. 20
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=20
#

from math import factorial
solution = reduce(lambda sum, digit: sum + digit, map(int, list(str(factorial(100)))))
print "Solution:", solution

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Power digit sum" – Project Euler Problem No. 16
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=16
#

sum = reduce(lambda sum, digit: sum + digit, map(int, list(str(2**1000))))
print "Solution:", sum

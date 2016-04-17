#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Self powers" – Project Euler Problem No. 48
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=48
#

print "Solution", reduce(lambda sum, n: sum + n**n, range(1, 1000+1)) % 10**10

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Cubic permutations" – Project Euler Problem No. 62
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=62

permutations = {}
n = 0
while True:
    n = n + 1
    cube = str(n**3)
    digits = "".join(sorted(cube))  # use the sorted list of digits as key
    if digits in permutations:
        permutations[digits].append(n)
    else:
        permutations[digits] = [n]

    if len(permutations[digits]) == 5:
        print "The digits of these numbers cubed are permutations of each other:", permutations[digits]
        print "Solution:", permutations[digits][0]**3
        break

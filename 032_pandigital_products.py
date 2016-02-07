#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Pandigital Products" – Project Euler Problem No. 32
# by Florian Buetow
#
# "Sometimes coding a solution fast beats fast code"
# Article: http://blog.florianbuetow.de/pandigital-products-project-euler-problem-no-32/
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=32
#
from itertools import permutations

digits = "123456789"
n = len(digits)
products = set()

for permutation in [''.join(perm) for perm in permutations(digits)]:
    if permutation[0] == 5:
        break
    for i in range(1, n/2):  # n/2 because: a factor can not have more digits than the product
        for j in range(i+1, n-i):  # n-i because: the number of digits of the two factors can not be more than that of the product
            a = int(permutation[:i])
            b = int(permutation[i:j])
            c = int(permutation[j:])
            if a * b == c:
                print "%d * %d = %d" % (a, b, c)
                products.add(c)

print "Solution:", sum(products)

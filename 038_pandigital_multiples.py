#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Pandigital multiples" – Project Euler Problem No. 38
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=38


def is_pandigital(n):
    # checks if n = 1 to 9 pandigital with length 9
    n = str(n)
    if len(n) != 9:
        return False
    for digit in '123456789':
        if digit not in n:
            return False
    return True


def concaternatedproduct(number, maxdigits=9):
    ret = ""
    n = 0
    while len(ret) < maxdigits:
        n = n + 1
        # print number, n, ret
        ret = ret + str(number * n)
    if n < 2 or len(ret) != maxdigits:  # n must be larger than 1 and length must be 9
        return (False, 0)
    return (int(ret), n)


# Testcase
assert (192384576 == concaternatedproduct(192)[0]), "Testcase failed"
assert (is_pandigital(concaternatedproduct(192)[0])), "Testcase failed"


solution = 0
for number in range(2, 10**5):  # since n > 1 number can at most have 9/2 = 4 digits
    (concatproduct, n) = concaternatedproduct(number)
    if concatproduct and is_pandigital(concatproduct):
        # print "%d * (1,...,%d) = %d" % (number,n,solution)
        if concatproduct > solution:
            solution = concatproduct

# Solve
print "Solution:", solution

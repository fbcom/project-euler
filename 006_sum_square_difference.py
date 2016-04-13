#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Sum square difference" – Project Euler Problem No. 6
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=6
#


def sum_of_squares(n):
    return reduce(lambda sum, number: sum + number**2, range(1, n+1))


def square_of_the_sum(n):
    return reduce(lambda sum, number: sum + number, range(1, n+1))**2

assert (2640 == (square_of_the_sum(10))-sum_of_squares(10)), "Testcase failed."
print "Solution:", square_of_the_sum(100)-sum_of_squares(100)

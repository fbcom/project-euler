#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Lychrel numbers" – Project Euler Problem No. 55
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=55


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_lychrel_number(n, iteration=0):
    if iteration >= 50:
        return False
    n += int(str(n)[::-1])
    if is_palindrome(n):
        return True
    else:
        return is_lychrel_number(n, iteration + 1)

# Testcases
assert is_lychrel_number(47), "Testcase failed"
assert is_lychrel_number(349), "Testcase failed"
assert not is_lychrel_number(196), "Testcase failed"

# Solve
solution = 0
for n in range(10*1000):
    if not is_lychrel_number(n):
        solution = solution + 1

print "Solution:", solution

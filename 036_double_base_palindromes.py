#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Double-base panindromes" – Project Euler Problem No. 36
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=36


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


def dec2bin(n):
    ret = ""
    while n > 0:
        ret = str(n % 2) + ret
        n = n // 2
    return ret

# Testcases
n = 585
assert ("1001001001" == dec2bin(n)), "Testcase failed"
assert (True == is_palindrome(n)), "Testcase failed"
assert (True == is_palindrome(dec2bin(n))), "Testcase failed"

# Solve
sum = 0
for n in range(1000*1000):
    if is_palindrome(n):
        n_bin = dec2bin(n)
        if is_palindrome(n_bin):
            sum = sum + n

print "Solution:", sum

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Number letter counts" – Project Euler Problem No. 17
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=17
#


def int_to_text(n, prefixStr=""):
    """
    dealing with irregular things like number to text conversion
    always seems to require a seemlingly messy collection of if-statements
    """
    if n <= 0:
        return ""
    if n > 0 and n < 10:
        return prefixStr + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][n-1]
    if n > 10 and n < 20:
        return prefixStr + ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n-11]
    if n < 100 and n % 10 == 0:
        return prefixStr + ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n/10-1]
    if n < 100:
        rest = n % 10
        return prefixStr + int_to_text(n-rest) + " " + int_to_text(rest)
    if n < 1000:
        rest = n % 100
        return prefixStr + int_to_text((n-rest)/100) + " hundred" + int_to_text(rest, " and ")

    # for fun lets go up to millions
    if n < 1000000:
        rest = n % 1000
        return prefixStr + int_to_text((n-rest)/1000) + " thousand" + int_to_text(rest, " and ")
    if n < 1000000000:
        rest = n % 1000000
        return prefixStr + int_to_text((n-rest)/1000000) + " million" + int_to_text(rest, " and ")
    return None

sum = 0
for n in range(1, 10000+1):
    str = int_to_text(n)
    sum = sum + len("".join(str.split()))
    print "%d = %s" % (n, str)

print "Solution:", sum

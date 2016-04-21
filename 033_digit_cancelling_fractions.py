#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Digit cancelling fractions" – Project Euler Problem No. 33
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=33

from fractions import Fraction

non_trivial_digit_cancelling_fractions = list()
for numerator in range(10, 100):  # two digits
    for denominator in range(10, 100):  # two digits

        # eleminate trivial examples and 0/x, x/0 fractions
        if numerator % 10 == 0:
            continue
        if denominator % 10 == 0:
            continue

        # fraction must be < 1
        if numerator >= denominator:
            continue

        common_digits = set(str(numerator)) & set(str(denominator))
        for digit in common_digits:
            # replace common digit in numerator and denominator
            numerator_short = str(numerator).replace(digit, '')
            denominator_short = str(denominator).replace(digit, '')

            # if not-empty convert to int
            if denominator_short and numerator_short:
                numerator_short = int(numerator_short)
                denominator_short = int(denominator_short)

            if not denominator_short or not numerator_short:  # neither can be 0
                continue

            n = Fraction(numerator, denominator)
            m = Fraction(numerator_short, denominator_short)
            if m == n:  # compare original fraction with digit cancelled fraction
                non_trivial_digit_cancelling_fractions.append((numerator, denominator, numerator_short, denominator_short))


product = Fraction(1, 1)
for numerator, denominator, numerator_short, denominator_short in non_trivial_digit_cancelling_fractions:
    print "%d/%d = %d/%d" % (numerator, denominator, numerator_short, denominator_short)
    product = product * Fraction(numerator, denominator)

print "Solution:", product.denominator

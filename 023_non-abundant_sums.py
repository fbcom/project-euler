#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Non-abundant sums" – Project Euler Problem No. 23
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=23
#


def get_proper_divisors(n):
    ret = [1]
    for d in range(2, n/2+1):
        if n % d == 0:
            ret.append(d)
    return ret


def get_sum_of_proper_divisor(n):
    return reduce(lambda sum, digit: sum + digit, get_proper_divisors(n))


def is_abundant_number(n):
    return n < get_sum_of_proper_divisor(n)


# Testcases
assert (28 == get_sum_of_proper_divisor(28)), "Testcase failed"

for n in range(1, 12):
    assert (False == is_abundant_number(n)), "Testcase failed"

assert (True == is_abundant_number(12)), "Testcase failed"


# Solve
limit = 28123
abundant_numbers = []
for n in range(1, limit):  # find all abundant numbers below the limit
    if is_abundant_number(n):
        abundant_numbers.append(n)

print "Found %d abundant numbers below %d" % (len(abundant_numbers), limit)

sums_of_two_abundant_numbers = []
for first_number in abundant_numbers:
    for second_number in abundant_numbers:
        if first_number+second_number < limit:
            sums_of_two_abundant_numbers.append(first_number + second_number)

not_sums_of_two_abundant_numbers = [n for n in range(1, limit) if n not in sums_of_two_abundant_numbers]

print "%d integers below %d can be written as the sum of two abundant numbers" % (len(sums_of_two_abundant_numbers), limit)
print "%d integers below %d can not be written as the sum of two abundant numbers" % (len(not_sums_of_two_abundant_numbers), limit)

sum = reduce(lambda sum, digit: sum + digit, not_sums_of_two_abundant_numbers)
print "Solution: The sum of all integers below %d that can not be written as the sum of two abundant numbers is %d" % (sum, limit)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Spiral primes" – Project Euler Problem No. 58
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=58


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0:
            return False
    return True


def get_numbers_on_diagonals_at_radius(radius):
    if radius < 1:
        return []

    if radius == 1:
        return[1]

    top_left = (2*(radius-1))**2 + 1
    bottom_right = (2*(radius-1)+1)**2
    top_right = top_left - 2*(radius-1)
    bottom_left = top_left + 2*(radius-1)

    return [top_right, top_left, bottom_left, bottom_right]


def get_primes_on_diagonals_at_radius(radius):
    ret = []
    for n in get_numbers_on_diagonals_at_radius(radius):
        if is_prime(n):
            ret.append(n)
    return ret


def find_sidelength(percent_max):
    return get_sidelength(find_radius(percent_max))


def get_sidelength(radius):
    return max(0, 2*radius - 1)


def find_radius(percent_max):
    sum_numbers_on_diagonals = 0
    sum_number_of_primes_on_diagonals = 0
    radius = 0
    while True:
        radius = radius + 1
        sum_numbers_on_diagonals += len(get_numbers_on_diagonals_at_radius(radius))
        sum_number_of_primes_on_diagonals += len(get_primes_on_diagonals_at_radius(radius))
        if sum_number_of_primes_on_diagonals > 0:
            percent = 100*(1.0*sum_number_of_primes_on_diagonals/sum_numbers_on_diagonals)
            if percent < percent_max and radius > 3:  # skip the first (and only) dip in percentage
                return radius

# Testcases
assert [3, 5, 7, 9] == get_numbers_on_diagonals_at_radius(2), "Testcase failed"
assert [3, 5, 7] == get_primes_on_diagonals_at_radius(2), "Testcase failed"
assert [13, 17, 21, 25] == get_numbers_on_diagonals_at_radius(3), "Testcase failed"
assert [13, 17] == get_primes_on_diagonals_at_radius(3), "Testcase failed"

sum_numbers_on_diagonals = 0
sum_number_of_primes_on_diagonals = 0
for radius in range(5):
    sum_numbers_on_diagonals += len(get_numbers_on_diagonals_at_radius(radius))
    sum_number_of_primes_on_diagonals += len(get_primes_on_diagonals_at_radius(radius))

assert 8 == sum_number_of_primes_on_diagonals, "Testcase failed"
assert 13 == sum_numbers_on_diagonals, "Testcase failed"
assert 62 > 100*(1.0*sum_number_of_primes_on_diagonals/sum_numbers_on_diagonals), "Testcase failed"
assert 4 == find_radius(62), "Testcase failed"

assert 1 == get_sidelength(1), "Testcase failed"
assert 3 == get_sidelength(2), "Testcase failed"
assert 5 == get_sidelength(3), "Testcase failed"
assert 7 == get_sidelength(4), "Testcase failed"

# Solve
solution = find_sidelength(10)
print "Solution:", solution

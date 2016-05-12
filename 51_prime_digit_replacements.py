#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Prime digit relacements" – Project Euler Problem No. 51
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=51


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


def get_power_set(elements):
    ret = [[]]
    for element in elements:  # gradually build up the power set
        ret = ret + [subset + list(element) for subset in ret]
    return ret


def find_family(family_size):
    n = 1
    while True:
        n = n + 2
        if not is_prime(n):
            continue # n needs to be a prime to start with

        power_set = get_power_set(map(str, range(len(str(n)))))
        for subset in power_set: # the subsets of the powerset tell us which places in n to swap out
            if not subset:
                continue  # skip the empty subset
            subset = map(int, subset)

            family_primes = []
            for digit in map(str, range(10)): # for each digit: swap out digits in n according to the positions indicated by the current subset
                m_list = list(str(n))
                for pos in subset:
                    m_list[pos] = digit
                m = int(''.join(m_list))
                if len(str(m)) != len(str(n)):
                    continue  # skip if we have leading zeros

                if is_prime(m):
                    family_primes.append(m)

            if len(family_primes) == family_size:
                if n not in family_primes:
                    continue # n needs to be in the family
                return family_primes

# Testcase 1
expected = [13, 23, 43, 53, 73, 83]
result = find_family(6)
assert len(result) == 6, "Testcase failed"
assert len(expected) == 6, "Testcase failed"
assert result[0] == expected[0], "Testcase failed"
for p in expected:
    assert p in result, "Testcase failed"

# Testcase 2
expected = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
result = find_family(7)
assert len(result) == 7, "Testcase failed"
assert len(expected) == 7, "Testcase failed"
assert result[0] == expected[0], "Testcase failed"
for p in expected:
    assert p in result, "Testcase failed"

# Solve
solution = find_family(8)
print "Primes  :", solution
print "Solution:", solution[0]

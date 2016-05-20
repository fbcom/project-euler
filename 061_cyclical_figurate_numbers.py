#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Cyclical figurate numbers" – Project Euler Problem No. 61
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=61


def p(s, n):
    return (s-2) * n*(n-1) / 2 + n


def get_polygonal_numbers(from_s, to_s, digits):
    """
    computes all from_s- to to_s-polygonal numbers with exactly 'digits' digits
    and returns the result as a dict where each key is a value of s
    and each value is a list of (n, s-polygonal-number) of the n-th polygonal number
    with 'digits' number of digits
    """
    ret = {}
    for s in range(from_s, to_s+1):
        ret[s] = []
        n = 1
        while True:
            psn = p(s, n)
            if psn >= 10**digits:
                break
            if psn >= 10**(digits-1):
                ret[s].append((n, psn))
            n = n + 1
    return ret


def find_cycle_in_polygonal_numbers(polygonal_numbers, digits):
    for key in polygonal_numbers:
        pass
        # print key, polygonal_numbers[key]

    start_s = min(polygonal_numbers.keys())
    start_cycle = []
    return find_connecting_polygonal_numbers(start_s, polygonal_numbers, digits)


def is_chain(n, m, overlap):
    n = str(n)[overlap:]
    m = str(m)[:overlap]
    return n == m


def find_connecting_polygonal_numbers(s, polygonal_numbers, digits, cycle=[], visited_s=[]):
    if cycle:
        (prev_s, prev_n, prev_psn) = cycle[-1]

    for (n, psn) in polygonal_numbers[s]:
        if cycle:
            if n == prev_n:
                continue
            if not is_chain(prev_psn, psn, digits/2):
                continue

        extended_cycle = cycle + [(s, n, psn)]
        extended_visited_s = visited_s + [s]

        if len(extended_visited_s) == len(polygonal_numbers.keys()):
            # check if start and end of cycle form a chain
            (first_s, first_n, first_psn) = extended_cycle[0]
            (last_s, last_n, last_psn) = extended_cycle[-1]
            if is_chain(last_psn, first_psn, digits/2):
                return extended_cycle  # found a cycle
            return None  # no cycle
        else:
            # find the next, connecting polygonal number
            for next_s in polygonal_numbers.keys():
                if next_s == s:
                    continue
                if next_s in visited_s:
                    continue
                found_cycle = find_connecting_polygonal_numbers(next_s, polygonal_numbers, digits, extended_cycle, extended_visited_s)
                if found_cycle:
                    return found_cycle

    return None  # no cycle found


def find_max_in_connecting_polygonal_numbers(from_s, to_s, digits):
    polygonal_numbers = get_polygonal_numbers(from_s, to_s, digits)
    cycle = find_cycle_in_polygonal_numbers(polygonal_numbers, digits)
    ret = 0
    for (s, n, psn) in cycle:
        ret = ret + psn
    return ret


# Testcase
digits = 4
cycle = [8128, 2882, 8281]
for i in range(len(cycle)):
    assert is_chain(cycle[i], cycle[(i+1) % len(cycle)], digits/2), "Testcase failed"
assert sum(cycle) == find_max_in_connecting_polygonal_numbers(3, 5, digits), "Testcase failed"

# Solve
digits = 4
solution = find_max_in_connecting_polygonal_numbers(3, 8, digits)
print "Solution:", solution

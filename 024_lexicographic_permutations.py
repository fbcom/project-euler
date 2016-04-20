#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Lexicographic permutations" – Project Euler Problem No. 24
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=24
#


def get_permutations(str):
    if len(str) == 1:
        return [str]
    ret = []
    for i in range(0, len(str)):
        char = str[i]
        sub_str = str[0:i] + str[i+1::]
        sub_perm = get_permutations(sub_str)
        ret.extend(map(lambda str: char+str, sub_perm))
    return ret

# Testcase
str = "012"
perm = get_permutations(str)
assert (6 == len(set(perm))), "Testcase failed"
assert ("012" == perm[0]), "Testcase failed"
assert ("021" == perm[1]), "Testcase failed"
assert ("102" == perm[2]), "Testcase failed"
assert ("120" == perm[3]), "Testcase failed"
assert ("201" == perm[4]), "Testcase failed"
assert ("210" == perm[5]), "Testcase failed"

# Solve
str = "0123456789"  # digits must be in sorted order to preserve lexicograpic order
perm = get_permutations(str)
nth = 1000000
print "There are %d permutation of the digits '%s'" % (len(perm), str)
print "Solution: The %d-th permutation of the digits '%s' : %s" % (nth, str, perm[nth - 1])

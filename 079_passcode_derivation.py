#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Passcode derivation" – Project Euler Problem No. 79
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=79
#
import operator


def load_logincodes(filename):
    ret = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            ret.append(map(int, list(line.strip())))
    return ret


def how_many_before(digit, logins):
    # find out how many digits appear before 'digit' in the list of logins
    before = set()
    before.add(digit)
    while True:
        len_before = len(before)
        for login in logins:
            for i in range(len(login)):
                if login[i] in before:
                    for j in range(i):
                        before.add(login[j])
        if len(before) == len_before:
            # no more changes detected, so we are done
            break
    return len(before)-1


def solve(logins):
    tmp = []  # store pairs of (digit, number of digits before before)
    for digit in range(10):
        x = how_many_before(digit, logins)
        tmp.append((digit, x))
    print
    tmp.sort(key=operator.itemgetter(1))  # sort by num digits before

    solution = []
    previous = tmp[0]
    for i in range(1, len(tmp)):
        if previous[1] != tmp[i][1]:  # skip digits with the same amount of digits before it
            solution.append(previous[0])
        previous = tmp[i]
    solution.append(previous[0])

    return "".join(map(str, solution))

# Solve
logins = load_logincodes('079_keylog.txt')
solution = solve(logins)
print "Solution:", solution

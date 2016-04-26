#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Integer right triangles" – Project Euler Problem No. 39
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=39


def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2  # c must be the hypothenuse

# Solve
solution = counter = max_counter = 0
for p in range(1, 1000+1):
    break
    counter = 0
    for a in range(1, p-1):
        for b in range(1, p-1-a):
            if a > b:
                continue  # because we want only unique answers
            c = p-(a+b)  # because perimeter p := a+b+c
            if is_right_triangle(a, b, c):
                counter += 1
                if counter > max_counter:
                    max_counter = counter
                    solution = p

print "Solution:", solution

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Names scores" – Project Euler Problem No. 22
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=22
#


def load_names(filename):
    with open(filename) as f:
        names = f.read().replace("\"", "").split(",")
    return names


def calc_alphabetical_value(str):
    ret = 0
    for char in str.upper():
        ret = ret + ord(char) - 64
    return ret

def sum_namescores(names):
    ret = i = 0
    for i, name in enumerate(names):
        v = calc_alphabetical_value(name)
        #print "%d: Alphabetical value of '%s' is %d" % (i, name, v)
        ret = ret + i * v
    return ret

names = sorted(load_names("022_names.txt"))
print "Solution:", sum_namescores(names)

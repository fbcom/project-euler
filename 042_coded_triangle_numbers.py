#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Coded triangle numbers" – Project Euler Problem No. 42
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=42
import string


def load_words(filename):
    with open(filename) as f:
        names = f.read().replace("\"", "").split(",")
    return names


def calc_word_number(word):
    ret = 0
    for letter in word:
        letter_value = 1 + string.ascii_uppercase.index(letter)
        ret += letter_value
    return ret


def calc_term(n):
    return int(0.5*(n*(n+1)))


# Solve
n = 1
tn = calc_term(n)
triangular_numbers = [tn]  # use this to lookup previously computed triangular numbers

solution = 0
words = sorted(load_words("042_words.txt"))
for word in words:
    word_number = calc_word_number(word)
    while word_number > tn:  # compute more triangular numbers
        n = n + 1
        tn = calc_term(n)
        triangular_numbers.append(tn)

    if word_number in triangular_numbers:
        # print "%s=%d is the %d. triangular number (%d)." % (word, word_number, n, tn)
        solution += 1

print "Solution:", solution

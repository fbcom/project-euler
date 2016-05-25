#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Roman numerals" – Project Euler Problem No. 89
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=89


def load_roman_numerals(filename):
    with open(filename) as f:
        numerals = f.read().split("\n")
    return numerals


def get_symtab():
    return {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }


def numeral2decimal(n):
    symtab = get_symtab()
    ret = i = 0
    while len(str(n)) > i:
        letter = n[i]
        value = symtab[letter]
        if i < len(n):
            substr = n[i:i+2]
            i += 1
            if substr == 'IV':
                value = 4
            elif substr == 'IX':
                value = 9
            elif substr == 'XL':
                value = 40
            elif substr == 'XC':
                value = 90
            elif substr == 'CD':
                value = 400
            elif substr == 'CM':
                value = 900
            else:
                i -= 1
        ret += value
        i += 1
    return ret


def decimal2numeral(n):
    ret = ''
    symtab_dict = get_symtab()
    symtab = [(letter, value) for letter, value in symtab_dict.iteritems()]
    symtab = sorted(symtab, key=lambda x: x[1], reverse=True)
    for symbol, value in symtab:
        while value <= n:
            if 4 == n:
                value = n
                symbol = 'IV'
            if 9 == n:
                value = n
                symbol = 'IX'
            if 50 > n and n >= 40:
                value = 40
                symbol = 'XL'
            if 100 > n and n >= 90:
                value = 90
                symbol = 'XC'
            if 500 > n and n >= 400:
                value = 400
                symbol = 'CD'
            if 1000 > n and n >= 900:
                value = 900
                symbol = 'CM'
            n -= value
            ret += symbol
    return ret


def minimize_numeral(numeral):
    return decimal2numeral(numeral2decimal(numeral))


# Testcases
assert minimize_numeral('XIIIIII') == 'XVI'
for i in range(1, 10000):
    assert numeral2decimal(decimal2numeral(i)) == i

# Solve
solution = 0
numerals = load_roman_numerals('089_roman.txt')
for numeral in numerals:
    minimal_numeral = minimize_numeral(numeral)
    solution += len(numeral) - len(minimal_numeral)
print "Solution:", solution

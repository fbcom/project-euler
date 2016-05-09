#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "XOR decryption" – Project Euler Problem No. 59
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=59


def load_codes(filename):
    with open(filename, 'r') as filehandle:
        line = filehandle.readlines()[0].strip()
        codes = map(int, line.split(','))
        return codes


def xor_codes(txt_codes, pw_codes):
    ret = []
    for i, textcode in enumerate(txt_codes):
        xored = textcode ^ pw_codes[i % len(pw_codes)]
        ret.append(xored)
    return ret


def codes2ascii(codes):
    ret = ''
    for code in codes:
        ret += chr(code)
    return ret


def crack(codes, commonword, commonword_treshold):
    from_ord = ord('a')
    to_ord = ord('z')
    for c1 in range(from_ord, to_ord+1):
        for c2 in range(from_ord, to_ord+1):
            for c3 in range(from_ord, to_ord+1):
                pw_codes = [c1, c2, c3]
                clear_codes = xor_codes(codes, pw_codes)
                clear_text = codes2ascii(clear_codes)
                if clear_text.count(commonword) > commonword_treshold:
                    return (clear_codes, clear_text, pw_codes)
    return None

# Solve
txt_codes = load_codes('059_cipher.txt')
(clear_codes, clear_text, pw_codes) = crack(txt_codes, 'the', 10)
print "Decrypted:", clear_text
print "Password :", codes2ascii(pw_codes)
print "Solution :", sum(clear_codes)

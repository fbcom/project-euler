#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Counting Sundays" – Project Euler Problem No. 19
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=19
#

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def get_days_in_month(month, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]
    if month == 1 and is_leap_year(year):
        days = 29
    return days


days_total = sundays = 0
for year in range(1900, 2001): # just iterate over all years and months and count
    for month in range(0, 12):
        days_total = days_total + get_days_in_month(month, year)
        if year > 1900 and days_total % 7 == 6:
            sundays = sundays + 1

print "Solution:", sundays


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Coin sums" – Project Euler Problem No. 31
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=31
#


def count_ways(amount, coins):
    coins = [coin for coin in coins if coin <= amount]  # remove coins > amount
    if coins:
        ret = 0
        visited = []
        for coin in coins:
            visited.append(coin)
            left_coins = [left_coin for left_coin in coins if left_coin not in visited]
            times = amount // coin
            for x in range(times, 0, -1):
                ret = ret + count_ways(amount - coin * x, left_coins)
    else:
        if amount > 0:
            ret = 0
        else:
            ret = 1
    return ret

coins = [200, 100, 50, 20, 10, 5, 2, 1]

# Testcases
assert (1 == count_ways(1, [1])), "Testcase failed"
assert (1 == count_ways(2, [1])), "Testcase failed"
assert (2 == count_ways(2, [2, 1])), "Testcase failed"
assert (3 == count_ways(4, [2, 1])), "Testcase failed"
assert (4 == count_ways(5, [5, 2, 1])), "Testcase failed"

# Solve
solution = count_ways(200, coins)
print "Solution:", solution

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Prime summations" – Project Euler Problem No. 77
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=77


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0:
            return False
    return True

primes = [2]


def find_more_primes(upto, primes):
    n = primes[-1]
    while upto > n:
        n = n + 1
        if is_prime(n):
            primes.append(n)
    return primes


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

# Solve
solution = 2
while count_ways(solution, primes) <= 5000:
    solution = solution + 1
    primes = find_more_primes(solution, primes)
print "Solution:", solution

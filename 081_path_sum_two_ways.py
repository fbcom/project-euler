#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A Solution to "Path sum: two ways" – Project Euler Problem No. 81
# by Florian Buetow
#
# Sourcecode: https://github.com/fbcom/project-euler
# Problem statement: https://projecteuler.net/problem=81


def load_matrix(filename):
    ret = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            ret += map(int, line.split(','))
    return ret


def shortest_path(matrix):
    dimension = int(len(matrix) ** 0.5)
    assert dimension**2 == len(matrix), "Not a square matrix"

    min_cost_matrix = list(matrix)  # use a min_cost matrix to compute the solution with dp

    # starting point is the upper left cell in the matrix
    for i in range(1, dimension):
        min_cost_matrix[i] += min_cost_matrix[i-1]
        min_cost_matrix[i*dimension] += min_cost_matrix[(i-1)*dimension]

    # compute minimum cost for reaching every cell in the matrix
    for i in range(1, dimension):
        for j in range(1, dimension):
            cost_right = min_cost_matrix[(i-1) + j*dimension]  # cost of going right
            cost_down = min_cost_matrix[i + (j-1)*dimension]  # cost of going down
            min_cost_matrix[i + j*dimension] += min(cost_right, cost_down)

    return min_cost_matrix[-1]


# Testcase
matrix = [
    131, 673, 234, 103, 18,
    201, 96, 342, 965, 150,
    630, 803, 746, 422, 111,
    537, 699, 497, 121, 956,
    805, 732, 524, 37, 331
]
assert shortest_path(matrix) == 2427, "Testcase failed"

# Solve
matrix = load_matrix('081_matrix.txt')
solution = shortest_path(matrix)
print "Solution:", solution

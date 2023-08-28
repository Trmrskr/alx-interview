#!/usr/bin/python3
""" This script solves the Island Perimeter"""


def island_perimeter(grid):
    """function that solves the island perimeter problem"""

    def dfs(i, j):
        """Performs depth first search"""
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or \
                grid[i][j] == 0:
            return 1
        if grid[i][j] == 1:
            grid[i][j] = 2
            # returns sum of traversal up, left, right, down
            return dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1)
        return 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (grid[i][j]):
                return dfs(i, j)

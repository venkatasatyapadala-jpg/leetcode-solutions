class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, bal):
            # If balance goes negative, invalid
            if bal < 0:
                return False
            # If at end, check balance == 0
            if i == m - 1 and j == n - 1:
                return bal == 0

            # Next moves
            res = False
            if i + 1 < m:
                res |= dfs(i + 1, j, bal + (1 if grid[i+1][j] == '(' else -1))
            if j + 1 < n:
                res |= dfs(i, j + 1, bal + (1 if grid[i][j+1] == '(' else -1))
            return res

        # Start with initial balance
        if grid[0][0] == ')':
            return False
        return dfs(0, 0, 1)

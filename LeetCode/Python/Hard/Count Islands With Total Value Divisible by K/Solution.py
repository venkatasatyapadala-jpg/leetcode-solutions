1class Solution:
2    def helpIslands(self, grid, i, j, m, n, sum_ref):
3        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
4            return
5
6        sum_ref[0] += grid[i][j]
7        grid[i][j] = 0
8
9        self.helpIslands(grid, i - 1, j, m, n, sum_ref)
10        self.helpIslands(grid, i + 1, j, m, n, sum_ref)
11        self.helpIslands(grid, i, j - 1, m, n, sum_ref)
12        self.helpIslands(grid, i, j + 1, m, n, sum_ref)
13
14    def countIslands(self, grid, k):
15        m, n = len(grid), len(grid[0])
16        count = 0
17
18        for i in range(m):
19            for j in range(n):
20                if grid[i][j] > 0:
21                    sum_ref = [0]
22                    self.helpIslands(grid, i, j, m, n, sum_ref)
23                    if sum_ref[0] % k == 0:
24                        count += 1
25        return count
1class Solution:
2    def closedIsland(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        count = 0
5        
6        def dfs(i, j):
7            if i < 0 or j < 0 or i >= rows or j >= cols:
8                return False
9            if grid[i][j] == 1:
10                return True
11            grid[i][j] = 1 # mark as visited
12            left = dfs(i, j-1)
13            right = dfs(i, j+1)
14            up = dfs(i-1, j)
15            down = dfs(i+1, j)
16            return left and right and up and down
17        
18        for i in range(rows):
19            for j in range(cols):
20                if grid[i][j] == 0 and dfs(i, j):
21                    count += 1
22        
23        return count
24
25
26
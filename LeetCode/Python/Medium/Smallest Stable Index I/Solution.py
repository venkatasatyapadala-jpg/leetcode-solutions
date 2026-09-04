1class Solution:
2    def firstStableIndex(self, nums, k):
3        n = len(nums)
4
5        suffix_min = [0] * n
6        suffix_min[n - 1] = nums[n - 1]
7
8        for i in range(n - 2, -1, -1):
9            suffix_min[i] = min(nums[i], suffix_min[i + 1])
10
11        prefix_max = nums[0]
12
13        for i in range(n):
14            prefix_max = max(prefix_max, nums[i])
15
16            if prefix_max - suffix_min[i] <= k:
17                return i
18
19        return -1
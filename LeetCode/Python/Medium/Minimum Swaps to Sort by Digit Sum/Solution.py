1class Pair:
2    def __init__(self, d, val, idx):
3        self.dsum = d
4        self.val = val
5        self.idx = idx
6
7class Solution:
8    def digitSum(self, num):
9        return sum(int(d) for d in str(num))
10
11    def minSwaps(self, nums):
12        n = len(nums)
13        pairs = [Pair(self.digitSum(nums[i]), nums[i], i) for i in range(n)]
14
15        pairs.sort(key=lambda x: (x.dsum, x.val))
16
17        i = 0
18        cnt = 0
19        while i < n:
20            if pairs[i].idx != i:
21                cnt += 1
22                j = pairs[i].idx
23                pairs[i], pairs[j] = pairs[j], pairs[i]
24            else:
25                i += 1
26        return cnt
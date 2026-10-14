1class Solution:
2    def maxSumOfSquares(self, n: int, s: int) -> str:
3        if s > n * 9: return ''
4        q, r = divmod(s, 9)
5        res = '9' * q + (str(r) if r else '')
6        return res + '0' * (n - len(res))
7        
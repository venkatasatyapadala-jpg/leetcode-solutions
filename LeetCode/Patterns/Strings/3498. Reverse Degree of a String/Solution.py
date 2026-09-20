class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            position = i + 1

            ans += value * position

        return ans
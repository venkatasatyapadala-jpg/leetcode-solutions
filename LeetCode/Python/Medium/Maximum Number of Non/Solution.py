1class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        n = len(s)
4
5        dp = [0] * (n + 1)
6
7        def isPalindrome(left, right):
8            if left < 0:
9                return False
10
11            while left < right:
12                if s[left] != s[right]:
13                    return False
14                left += 1
15                right -= 1
16
17            return True
18
19        for i in range(k, n + 1):
20
21            # Don't choose a palindrome ending at i-1
22            dp[i] = dp[i - 1]
23
24            # Check palindrome of length k
25            if isPalindrome(i - k, i - 1):
26                dp[i] = max(dp[i], dp[i - k] + 1)
27
28            # Check palindrome of length k + 1
29            if isPalindrome(i - k - 1, i - 1):
30                dp[i] = max(dp[i], dp[i - k - 1] + 1)
31
32        return dp[n]
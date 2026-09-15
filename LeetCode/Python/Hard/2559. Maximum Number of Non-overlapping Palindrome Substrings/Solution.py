class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        dp = [0] * (n + 1)

        def isPalindrome(left, right):
            if left < 0:
                return False

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        for i in range(k, n + 1):

            # Don't choose a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Check palindrome of length k
            if isPalindrome(i - k, i - 1):
                dp[i] = max(dp[i], dp[i - k] + 1)

            # Check palindrome of length k + 1
            if isPalindrome(i - k - 1, i - 1):
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]
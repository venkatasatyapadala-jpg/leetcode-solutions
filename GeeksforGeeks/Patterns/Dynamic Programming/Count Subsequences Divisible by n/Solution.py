class Solution:
    def countSubsequences(self, s, n):
        MOD = 10**9 + 7

        dp = [0] * n

        for ch in s:
            d = int(ch)

            # Copy old subsequences
            new_dp = dp[:]

            # Start a new subsequence with this digit
            new_dp[d % n] = (new_dp[d % n] + 1) % MOD

            # Append current digit to existing subsequences
            for r in range(n):
                if dp[r]:
                    new_r = (r * 10 + d) % n
                    new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD

            dp = new_dp

        return dp[0]
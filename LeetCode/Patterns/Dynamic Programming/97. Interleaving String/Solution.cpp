class Solution {
public:
    bool helper(string& s1, string& s2, string& s3, vector<vector<int>>& dp,
                int m, int n, int x) {
        if (m == 0 && n == 0 && x == 0) {
            return true;
        }
        if (x == 0) {
            return false;
        }
        if (dp[m][n] != -1) {
            return dp[m][n];
        }
        bool take1 = false;
        bool take2 = false;
        if (m > 0 && s1[m - 1] == s3[x - 1]) {
            take1 = helper(s1, s2, s3, dp, m - 1, n, x - 1);
        }
        if (n > 0 && s2[n - 1] == s3[x - 1]) {
            take2 = helper(s1, s2, s3, dp, m, n - 1, x - 1);
        }

        return dp[m][n] = (take1 || take2);
    }

    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size();
        int n = s2.size();
        int x = s3.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return helper(s1, s2, s3, dp, m, n, x);
    }
};
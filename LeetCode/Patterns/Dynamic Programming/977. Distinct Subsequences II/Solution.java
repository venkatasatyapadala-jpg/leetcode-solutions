class Solution {
    public int distinctSubseqII(String s) {
        long MOD = 1000000007;
        
        long dp = 1;
        long[] last = new long[26];

        for (char ch : s.toCharArray()) {
            int i = ch - 'a';

            long oldDp = dp;

            dp = (2 * dp - last[i] + MOD) % MOD;

            last[i] = oldDp;
        }

        return (int)((dp - 1 + MOD) % MOD);
    }
}
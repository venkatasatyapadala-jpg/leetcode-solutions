1class Solution {
2    public int distinctSubseqII(String s) {
3        long MOD = 1000000007;
4        
5        long dp = 1;
6        long[] last = new long[26];
7
8        for (char ch : s.toCharArray()) {
9            int i = ch - 'a';
10
11            long oldDp = dp;
12
13            dp = (2 * dp - last[i] + MOD) % MOD;
14
15            last[i] = oldDp;
16        }
17
18        return (int)((dp - 1 + MOD) % MOD);
19    }
20}
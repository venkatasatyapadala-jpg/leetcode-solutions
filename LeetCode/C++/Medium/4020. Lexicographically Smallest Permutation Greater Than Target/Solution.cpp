class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();
        vector<int> cnt(26, 0);

        for (char c : s)
            cnt[c - 'a']++;

        string prefix = "";

        for (int i = 0; i < n; i++) {
            int x = target[i] - 'a';

            // Try to keep prefix equal to target
            if (cnt[x] > 0) {
                prefix += target[i];
                cnt[x]--;
            } 
            else {
                // Find the smallest character > target[i]
                for (int c = x + 1; c < 26; c++) {
                    if (cnt[c] > 0) {
                        string ans = prefix;
                        ans += char('a' + c);
                        cnt[c]--;

                        // Add remaining characters in sorted order
                        for (int j = 0; j < 26; j++) {
                            while (cnt[j] > 0) {
                                ans += char('a' + j);
                                cnt[j]--;
                            }
                        }

                        return ans;
                    }
                }

                // Need to backtrack
                break;
            }
        }

        // Backtrack
        for (int i = prefix.size() - 1; i >= 0; i--) {
            cnt[prefix[i] - 'a']++;

            int x = target[i] - 'a';

            // Find smallest available character greater than target[i]
            for (int c = x + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    string ans = target.substr(0, i);
                    ans += char('a' + c);
                    cnt[c]--;

                    // Remaining characters in sorted order
                    for (int j = 0; j < 26; j++) {
                        while (cnt[j] > 0) {
                            ans += char('a' + j);
                            cnt[j]--;
                        }
                    }

                    return ans;
                }
            }
        }

        return "";
    }
};
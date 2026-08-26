class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        string ans = "";

        for (int i = 0; i < s.length(); i++) {
            int ones = 0;

            for (int j = i; j < s.length(); j++) {
                if (s[j] == '1') {
                    ones++;
                }

                if (ones == k) {
                    string sub = s.substr(i, j - i + 1);

                    if (ans == "" ||
                        sub.length() < ans.length() ||
                        (sub.length() == ans.length() && sub < ans)) {
                        ans = sub;
                    }
                }
                else if (ones > k) {
                    break;
                }
            }
        }

        return ans;
    }
};
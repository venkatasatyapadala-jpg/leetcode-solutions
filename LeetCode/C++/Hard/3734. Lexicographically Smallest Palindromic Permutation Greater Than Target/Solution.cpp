class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();

        vector<int> cnt(26, 0);
        for (char c : s)
            cnt[c - 'a']++;

        // A palindrome can have at most one odd frequency.
        int odd = 0;
        char middle = 0;

        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2) {
                odd++;
                middle = 'a' + i;
            }
        }

        if (odd > 1)
            return "";

        int halfLen = n / 2;

        // Characters available for the first half.
        vector<int> halfCnt(26);
        for (int i = 0; i < 26; i++)
            halfCnt[i] = cnt[i] / 2;

        // Build palindrome from a given first half.
        auto build = [&](string half) {
            string ans = half;

            if (n % 2)
                ans += middle;

            for (int i = halfLen - 1; i >= 0; i--)
                ans += half[i];

            return ans;
        };

        /*
            We construct the first half.

            If we make the first half equal to target's first half,
            the complete palindrome may be > target because of the
            middle/right half.

            Otherwise, we find the first position where our palindrome
            becomes greater and then make the remaining part smallest.
        */

        string prefix;
        vector<int> remaining = halfCnt;

        // Try to match target's first half as long as possible.
        for (int i = 0; i < halfLen; i++) {
            int c = target[i] - 'a';

            if (remaining[c] > 0) {
                prefix += target[i];
                remaining[c]--;
            } else {
                break;
            }
        }

        // Case 1: Entire first half matches target.
        if ((int)prefix.size() == halfLen) {
            string candidate = build(prefix);

            if (candidate > target)
                return candidate;
        }

        /*
            We need to increase some position.

            Start from the rightmost position that can be increased.
            This keeps the resulting string lexicographically smallest.
        */

        string cur = prefix;
        vector<int> rem = remaining;

        int pos = (int)cur.size() - 1;

        while (pos >= 0) {
            int current = cur[pos] - 'a';

            // Restore the character at this position.
            rem[current]++;

            // Try the smallest character greater than current.
            for (int c = current + 1; c < 26; c++) {
                if (rem[c] == 0)
                    continue;

                string half = cur.substr(0, pos);
                half += char('a' + c);

                rem[c]--;

                // Fill the rest with smallest characters.
                for (int x = 0; x < 26; x++) {
                    half += string(rem[x], char('a' + x));
                }

                string candidate = build(half);

                if (candidate > target)
                    return candidate;

                rem[c]++;
            }

            if (pos == 0)
                break;

            // Remove the previous fixed character from cur.
            pos--;
            cur.pop_back();
        }

        /*
            Special case:
            We could not match even one character, so try the smallest
            available character greater than target[0].
        */
        if (halfLen > 0 && cur.empty()) {
            for (int c = target[0] - 'a' + 1; c < 26; c++) {
                if (halfCnt[c] == 0)
                    continue;

                string half;
                half += char('a' + c);

                halfCnt[c]--;

                for (int x = 0; x < 26; x++)
                    half += string(halfCnt[x], char('a' + x));

                string candidate = build(half);

                if (candidate > target)
                    return candidate;

                halfCnt[c]++;
            }
        }

        // n = 1 case
        if (halfLen == 0) {
            string candidate(1, middle);
            if (candidate > target)
                return candidate;
        }

        return "";
    }
};
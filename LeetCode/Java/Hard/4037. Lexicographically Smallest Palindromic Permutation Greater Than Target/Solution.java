class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();

        // Count characters
        int[] cnt = new int[26];

        for (char ch : s.toCharArray()) {
            cnt[ch - 'a']++;
        }

        // Check whether palindrome is possible
        int odd = 0;
        char middle = 0;

        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2 == 1) {
                odd++;
                middle = (char) ('a' + i);
            }
        }

        if (odd > 1) {
            return "";
        }

        int half = n / 2;

        // Count available characters for first half
        int[] halfCnt = new int[26];

        for (int i = 0; i < 26; i++) {
            halfCnt[i] = cnt[i] / 2;
        }

        // Try to make first half equal to target's first half
        int[] remaining = halfCnt.clone();
        boolean possible = true;

        for (int i = 0; i < half; i++) {
            int x = target.charAt(i) - 'a';

            if (remaining[x] == 0) {
                possible = false;
                break;
            }

            remaining[x]--;
        }

        if (possible) {
            String firstHalf = target.substring(0, half);

            // Even length
            if (n % 2 == 0) {
                String candidate = makePalindrome(firstHalf, "");
                if (candidate.compareTo(target) > 0) {
                    return candidate;
                }
            }

            // Odd length
            else {
                for (int c = 0; c < 26; c++) {
                    if (cnt[c] % 2 == 1) {
                        String mid = String.valueOf((char) ('a' + c));

                        String candidate =
                                makePalindrome(firstHalf, mid);

                        if (candidate.compareTo(target) > 0) {
                            return candidate;
                        }
                    }
                }
            }
        }

        // Need to make first half greater than target
        for (int i = half - 1; i >= 0; i--) {

            remaining = halfCnt.clone();

            boolean valid = true;

            // Match target[0 ... i-1]
            for (int j = 0; j < i; j++) {
                int x = target.charAt(j) - 'a';

                if (remaining[x] == 0) {
                    valid = false;
                    break;
                }

                remaining[x]--;
            }

            if (!valid) {
                continue;
            }

            // Choose smallest character greater than target[i]
            int start = target.charAt(i) - 'a' + 1;

            for (int c = start; c < 26; c++) {

                if (remaining[c] == 0) {
                    continue;
                }

                int[] rem = remaining.clone();
                rem[c]--;

                // Fill remaining positions with smallest characters
                StringBuilder firstHalf = new StringBuilder();

                firstHalf.append(target, 0, i);
                firstHalf.append((char) ('a' + c));

                for (int x = 0; x < 26; x++) {
                    while (rem[x] > 0) {
                        firstHalf.append((char) ('a' + x));
                        rem[x]--;
                    }
                }

                String mid = (n % 2 == 1)
                        ? String.valueOf(middle)
                        : "";

                String candidate =
                        makePalindrome(firstHalf.toString(), mid);

                if (candidate.compareTo(target) > 0) {
                    return candidate;
                }
            }
        }

        return "";
    }

    private String makePalindrome(String firstHalf, String middle) {
        StringBuilder result = new StringBuilder();

        result.append(firstHalf);
        result.append(middle);
        result.append(new StringBuilder(firstHalf).reverse());

        return result.toString();
    }
}
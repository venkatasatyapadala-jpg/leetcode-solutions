class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether a palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        half_len = n // 2

        # Characters available for first half
        half_cnt = [x // 2 for x in cnt]

        def build(half):
            # First half + middle + reverse(first half)
            return half + middle + half[::-1]

        # Try to match target's first half
        prefix = []
        remaining = half_cnt[:]

        for i in range(half_len):
            c = ord(target[i]) - ord('a')

            if remaining[c] > 0:
                prefix.append(target[i])
                remaining[c] -= 1
            else:
                break

        # If complete first half matches target's first half,
        # check the resulting palindrome.
        if len(prefix) == half_len:
            half = ''.join(prefix)
            candidate = build(half)

            if candidate > target:
                return candidate

        # Try changing a position from right to left.
        cur = prefix[:]
        rem = remaining[:]

        pos = len(cur) - 1

        while pos >= 0:
            current = ord(cur[pos]) - ord('a')

            # Put this character back
            rem[current] += 1

            # Try the smallest character greater than current
            for c in range(current + 1, 26):
                if rem[c] == 0:
                    continue

                half = ''.join(cur[:pos])
                half += chr(ord('a') + c)

                rem[c] -= 1

                # Fill remaining positions with smallest characters
                for x in range(26):
                    half += chr(ord('a') + x) * rem[x]

                candidate = build(half)

                if candidate > target:
                    return candidate

                rem[c] += 1

            pos -= 1
            cur.pop()

        # If no prefix could be matched, try the smallest
        # character greater than target[0].
        if half_len > 0 and len(prefix) == 0:
            first = ord(target[0]) - ord('a')

            for c in range(first + 1, 26):
                if half_cnt[c] == 0:
                    continue

                half = chr(ord('a') + c)

                half_cnt[c] -= 1

                for x in range(26):
                    half += chr(ord('a') + x) * half_cnt[x]

                candidate = build(half)

                if candidate > target:
                    return candidate

                half_cnt[c] += 1

        # n = 1
        if half_len == 0:
            candidate = middle
            if candidate > target:
                return candidate

        return ""
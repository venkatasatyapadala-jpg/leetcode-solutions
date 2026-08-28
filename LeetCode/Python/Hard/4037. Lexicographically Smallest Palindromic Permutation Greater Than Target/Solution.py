class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd count
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # For a palindrome, first half contains count // 2
        half_cnt = [x // 2 for x in cnt]
        half_len = n // 2

        def make_palindrome(half):
            return half + middle + half[::-1]

        # Build the smallest possible half
        half = []
        for i in range(26):
            half.extend([chr(ord('a') + i)] * half_cnt[i])

        half = ''.join(half)

        # If the smallest palindrome is already greater
        candidate = make_palindrome(half)
        if candidate > target:
            return candidate

        # We need the smallest half whose palindrome > target.
        # Since palindrome comparison is determined by the first half,
        # find the next permutation of half that is > target's first half.

        target_half = target[:half_len]

        # We need a half >= target_half.
        # Try to construct the smallest half greater than target_half.

        remaining = half_cnt[:]
        prefix = []

        # Match target_half as long as possible
        for ch in target_half:
            x = ord(ch) - ord('a')

            if remaining[x] > 0:
                prefix.append(ch)
                remaining[x] -= 1
            else:
                break

        # If we matched the whole target half,
        # the exact half may still produce a palindrome <= target.
        if len(prefix) == half_len:
            candidate = make_palindrome(''.join(prefix))

            if candidate > target:
                return candidate

        # Backtrack from the last matched position.
        for pos in range(len(prefix) - 1, -1, -1):

            # Return the character used at this position
            old = ord(prefix[pos]) - ord('a')
            remaining[old] += 1

            # Try the smallest character greater than it
            for c in range(old + 1, 26):

                if remaining[c] == 0:
                    continue

                new_half = prefix[:pos] + [chr(ord('a') + c)]

                remaining[c] -= 1

                # Append all remaining characters in sorted order
                for x in range(26):
                    new_half.extend(
                        [chr(ord('a') + x)] * remaining[x]
                    )

                half_string = ''.join(new_half)
                candidate = make_palindrome(half_string)

                if candidate > target:
                    return candidate

                remaining[c] += 1

        return ""
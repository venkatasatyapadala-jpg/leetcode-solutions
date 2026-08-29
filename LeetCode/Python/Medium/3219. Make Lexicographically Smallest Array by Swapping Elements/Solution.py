class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        result = [0] * n

        left = 0

        while left < n:
            right = left

            # Find one connected group
            while right + 1 < n and arr[right + 1][0] - arr[right][0] <= limit:
                right += 1

            # Get indices and values of this group
            indices = sorted(arr[i][1] for i in range(left, right + 1))
            values = sorted(arr[i][0] for i in range(left, right + 1))

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                result[idx] = value

            left = right + 1

        return result
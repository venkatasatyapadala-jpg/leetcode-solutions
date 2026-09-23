class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        left = 0
        current_sum = 0
        longest = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return len(nums) - longest
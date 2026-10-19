1class Solution:
2    def targetIndices(self, nums: List[int], target: int) -> List[int]:
3        nums.sort()
4        return [i for i in range(len(nums)) if nums[i]==target]
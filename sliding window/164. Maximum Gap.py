"""
  https://leetcode.com/problems/maximum-gap/
"""


def maximumGap(self, nums: List[int]) -> int:
    nums.sort()
    maxDiff = 0
    if len(nums) < 2:
        return 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        maxDiff = max(maxDiff, diff)
    return maxDiff

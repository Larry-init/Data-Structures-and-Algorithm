"""
  https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1658362873/
"""



def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    counter = 0
    left = 0
    min_len = float('inf')
    for right in range(len(nums)):
        counter += nums[right]
        while counter >= target:
            min_len = min(min_len, right - left + 1)
            counter -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

"""
  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    left, right = 0, n-1
    while left < right:
        total = numbers[right] + numbers[left]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left +=1
        else:
            right -=1
    return [left+1, right+1]

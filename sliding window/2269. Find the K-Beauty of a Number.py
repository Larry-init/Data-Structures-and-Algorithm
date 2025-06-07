"""
https://leetcode.com/problems/find-the-k-beauty-of-a-number/
"""


def divisorSubstrings(self, num: int, k: int) -> int:
        n = str(num)
        count = 0
        for i in range(len(n) - k + 1):
            window = n[i:i+k]
            intWindow = int(window)
            if intWindow != 0 and num%intWindow == 0:
                count += 1
        return count

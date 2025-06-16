"""
  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""

def lengthOfLongestSubstring(self, s: str) -> int:
    longestStr = ""
    maxCount = 0

    for i in range(len(s)):
        if s[i] not in longestStr:
            longestStr += s[i]
        elif s[i] in longestStr:
            maxCount = max(maxCount, len(longestStr))
            while s[i] in longestStr:
                longestStr= longestStr[1:]
            longestStr += s[i]
            
    maxCount = max(maxCount, len(longestStr))
    return maxCount



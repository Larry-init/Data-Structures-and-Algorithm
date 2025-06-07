"""
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""

def minimumRecolors(self, blocks: str, k: int) -> int:
    minWs = k
    for i in range(len(blocks)-k+1):
        window = blocks[i:i+k]
        whiteWindow = window.count("W")
        minWs = min(whiteWindow, minWs)
    return minWs

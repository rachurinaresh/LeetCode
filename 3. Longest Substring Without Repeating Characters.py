class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        d = {}
        ml = 0
        start = 0
        for i, char in enumerate(s):
            if char in d and d[char] >= start:
                start = d[char] + 1
            d[char] = i 
            ml = max(ml, i - start + 1)
        return ml
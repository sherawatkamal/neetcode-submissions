class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        maxLen, l, r = 1, 0, 0

        char_set = set()

        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            maxLen  = max(maxLen, r - l + 1)
            r += 1
        return maxLen
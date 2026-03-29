class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        d = {}

        for r in range(len(s)):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]] + 1

            d[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans
        
        